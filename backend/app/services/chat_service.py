# from sqlalchemy.orm import Session

# from app.core.config import settings
# from app.services.groq_service import generate_rag_reply
# from app.services.retrieval_service import retrieve_similar_chunks
# from app.services.session_service import (
#     get_or_create_session,
#     get_recent_messages,
#     save_message,
#     update_session_title_if_needed,
# )


# MEMORY_KEYWORDS = [
#     "what did i ask earlier",
#     "what did i ask before",
#     "what did i say earlier",
#     "what did i say before",
#     "what was my previous question",
#     "what was my last question",
#     "what did we discuss earlier",
#     "continue from before",
#     "continue from earlier",
#     "what were we talking about",
#     "summarize our conversation",
#     "summarize this chat",
#     "what did we talk about",
# ]


# def is_memory_question(user_message: str) -> bool:
#     normalized = user_message.strip().lower()
#     return any(keyword in normalized for keyword in MEMORY_KEYWORDS)


# def process_chat_message(
#     db: Session,
#     user_message: str,
#     k: int = 4,
#     session_id: str | None = None,
# ) -> dict:
#     session = get_or_create_session(
#         db=db,
#         session_id=session_id,
#         first_user_message=user_message,
#     )

#     session = update_session_title_if_needed(
#         db=db,
#         session=session,
#         first_user_message=user_message,
#     )

#     conversation_history = get_recent_messages(
#         db=db,
#         session_id=session.id,
#         limit=settings.CHAT_HISTORY_LIMIT
#     )

#     memory_mode = is_memory_question(user_message)

#     if memory_mode:
#         retrieval_result = {
#             "query": user_message,
#             "count": 0,
#             "results": []
#         }
#     else:
#         retrieval_result = retrieve_similar_chunks(query=user_message, k=k)

#     retrieved_chunks = retrieval_result["results"]

#     bot_reply = generate_rag_reply(
#         user_message=user_message,
#         retrieved_chunks=retrieved_chunks,
#         conversation_history=conversation_history,
#     )

#     seen = set()
#     sources = []

#     for chunk in retrieved_chunks:
#         page_id = chunk.get("page_id", "")
#         page_title = chunk.get("page_title", "")
#         source_url = chunk.get("source_url", "")

#         source_key = (page_id, source_url)

#         if source_key not in seen:
#             seen.add(source_key)
#             sources.append(
#                 {
#                     "page_id": page_id,
#                     "page_title": page_title,
#                     "source_url": source_url,
#                 }
#             )

#     save_message(
#         db=db,
#         session_id=session.id,
#         role="user",
#         content=user_message,
#         sources=[],
#     )
#     save_message(
#         db=db,
#         session_id=session.id,
#         role="assistant",
#         content=bot_reply,
#         sources=sources,
#     )

#     return {
#         "session_id": session.id,
#         "user_message": user_message,
#         "bot_reply": bot_reply,
#         "sources": sources,
#         "retrieved_chunk_count": retrieval_result["count"],
#     }

from sqlalchemy.orm import Session

from app.langchain.chains import build_answer_chain, build_query_rewrite_chain
from app.langchain.formatters import (
    extract_sources_from_documents,
    format_documents_for_prompt,
)
from app.langchain.history import load_session_history_messages
from app.services.retrieval_service import search_retrieved_documents
from app.services.session_service import (
    get_or_create_session,
    save_message,
    update_session_title_if_needed,
)


UNKNOWN_ANSWER = "I don't know based on the retrieved Confluence documents."


def _rewrite_query(
    user_message: str,
    chat_history,
) -> str:
    normalized_user_message = (user_message or "").strip()

    if not normalized_user_message:
        return ""

    if not chat_history:
        return normalized_user_message

    try:
        rewrite_chain = build_query_rewrite_chain()
        rewritten_query = rewrite_chain.invoke(
            {
                "chat_history": chat_history,
                "input": normalized_user_message,
            }
        )
    except Exception:
        return normalized_user_message

    if not isinstance(rewritten_query, str):
        return normalized_user_message

    rewritten_query = rewritten_query.strip()

    if not rewritten_query:
        return normalized_user_message

    return rewritten_query


def _generate_answer_from_documents(
    user_message: str,
    context_text: str,
) -> str:
    normalized_user_message = (user_message or "").strip()

    if not normalized_user_message or not context_text.strip():
        return UNKNOWN_ANSWER

    try:
        answer_chain = build_answer_chain()
        answer = answer_chain.invoke(
            {
                "input": normalized_user_message,
                "context": context_text,
            }
        )
    except Exception:
        return UNKNOWN_ANSWER

    if not isinstance(answer, str):
        return UNKNOWN_ANSWER

    answer = answer.strip()

    if not answer:
        return UNKNOWN_ANSWER

    return answer


def process_chat_message(
    db: Session,
    user_message: str,
    k: int = 4,
    session_id: str | None = None,
) -> dict:
    normalized_user_message = (user_message or "").strip()

    if not normalized_user_message:
        raise ValueError("Message cannot be empty")

    session = get_or_create_session(
        db=db,
        session_id=session_id,
        first_user_message=normalized_user_message,
    )

    session = update_session_title_if_needed(
        db=db,
        session=session,
        first_user_message=normalized_user_message,
    )

    chat_history = load_session_history_messages(
        db=db,
        session_id=session.id,
    )

    rewritten_query = _rewrite_query(
        user_message=normalized_user_message,
        chat_history=chat_history,
    )

    documents = search_retrieved_documents(
        query=rewritten_query,
        k=k,
    )

    if not documents:
        bot_reply = UNKNOWN_ANSWER
        sources = []
        retrieved_chunk_count = 0
    else:
        context_text = format_documents_for_prompt(documents)
        bot_reply = _generate_answer_from_documents(
            user_message=normalized_user_message,
            context_text=context_text,
        )
        sources = extract_sources_from_documents(documents)
        retrieved_chunk_count = len(documents)

    save_message(
        db=db,
        session_id=session.id,
        role="user",
        content=normalized_user_message,
        sources=[],
    )
    save_message(
        db=db,
        session_id=session.id,
        role="assistant",
        content=bot_reply,
        sources=sources,
    )

    return {
        "session_id": session.id,
        "user_message": normalized_user_message,
        "bot_reply": bot_reply,
        "sources": sources,
        "retrieved_chunk_count": retrieved_chunk_count,
    }