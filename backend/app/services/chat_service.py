# # from app.services.groq_service import get_chat_reply


# # def process_chat_message(user_message: str) -> dict:
# #     bot_reply = get_chat_reply(user_message)

# #     return {
# #         "user_message": user_message,
# #         "bot_reply": bot_reply,
# #         "sources": []
# #     }

# from app.services.groq_service import generate_rag_reply
# from app.services.retrieval_service import retrieve_similar_chunks


# def process_chat_message(user_message: str, k: int = 4) -> dict:
#     retrieval_result = retrieve_similar_chunks(query=user_message, k=k)
#     retrieved_chunks = retrieval_result["results"]

#     bot_reply = generate_rag_reply(
#         user_message=user_message,
#         retrieved_chunks=retrieved_chunks
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

#     return {
#         "user_message": user_message,
#         "bot_reply": bot_reply,
#         "sources": sources,
#         "retrieved_chunk_count": retrieval_result["count"],
#     }

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

#     retrieval_result = retrieve_similar_chunks(query=user_message, k=k)
#     retrieved_chunks = retrieval_result["results"]

#     bot_reply = generate_rag_reply(
#         user_message=user_message,
#         retrieved_chunks=retrieved_chunks,
#         conversation_history=conversation_history,
#     )

#     save_message(db=db, session_id=session.id, role="user", content=user_message)
#     save_message(db=db, session_id=session.id, role="assistant", content=bot_reply)

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

#     return {
#         "session_id": session.id,
#         "user_message": user_message,
#         "bot_reply": bot_reply,
#         "sources": sources,
#         "retrieved_chunk_count": retrieval_result["count"],
#     }

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

#     save_message(db=db, session_id=session.id, role="user", content=user_message)
#     save_message(db=db, session_id=session.id, role="assistant", content=bot_reply)

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

#     return {
#         "session_id": session.id,
#         "user_message": user_message,
#         "bot_reply": bot_reply,
#         "sources": sources,
#         "retrieved_chunk_count": retrieval_result["count"],
#     }

from sqlalchemy.orm import Session

from app.core.config import settings
from app.services.groq_service import generate_rag_reply
from app.services.retrieval_service import retrieve_similar_chunks
from app.services.session_service import (
    get_or_create_session,
    get_recent_messages,
    save_message,
    update_session_title_if_needed,
)


MEMORY_KEYWORDS = [
    "what did i ask earlier",
    "what did i ask before",
    "what did i say earlier",
    "what did i say before",
    "what was my previous question",
    "what was my last question",
    "what did we discuss earlier",
    "continue from before",
    "continue from earlier",
    "what were we talking about",
    "summarize our conversation",
    "summarize this chat",
    "what did we talk about",
]


def is_memory_question(user_message: str) -> bool:
    normalized = user_message.strip().lower()
    return any(keyword in normalized for keyword in MEMORY_KEYWORDS)


def process_chat_message(
    db: Session,
    user_message: str,
    k: int = 4,
    session_id: str | None = None,
) -> dict:
    session = get_or_create_session(
        db=db,
        session_id=session_id,
        first_user_message=user_message,
    )

    session = update_session_title_if_needed(
        db=db,
        session=session,
        first_user_message=user_message,
    )

    conversation_history = get_recent_messages(
        db=db,
        session_id=session.id,
        limit=settings.CHAT_HISTORY_LIMIT
    )

    memory_mode = is_memory_question(user_message)

    if memory_mode:
        retrieval_result = {
            "query": user_message,
            "count": 0,
            "results": []
        }
    else:
        retrieval_result = retrieve_similar_chunks(query=user_message, k=k)

    retrieved_chunks = retrieval_result["results"]

    bot_reply = generate_rag_reply(
        user_message=user_message,
        retrieved_chunks=retrieved_chunks,
        conversation_history=conversation_history,
    )

    seen = set()
    sources = []

    for chunk in retrieved_chunks:
        page_id = chunk.get("page_id", "")
        page_title = chunk.get("page_title", "")
        source_url = chunk.get("source_url", "")

        source_key = (page_id, source_url)

        if source_key not in seen:
            seen.add(source_key)
            sources.append(
                {
                    "page_id": page_id,
                    "page_title": page_title,
                    "source_url": source_url,
                }
            )

    save_message(
        db=db,
        session_id=session.id,
        role="user",
        content=user_message,
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
        "user_message": user_message,
        "bot_reply": bot_reply,
        "sources": sources,
        "retrieved_chunk_count": retrieval_result["count"],
    }