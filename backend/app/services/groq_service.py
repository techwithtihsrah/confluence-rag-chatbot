# from groq import Groq
# from app.core.config import settings


# def _get_client() -> Groq:
#     if not settings.GROQ_API_KEY:
#         raise ValueError("GROQ_API_KEY is missing in .env file")

#     return Groq(api_key=settings.GROQ_API_KEY)


# def _build_rag_context(retrieved_chunks: list[dict]) -> str:
#     context_parts = []

#     for index, chunk in enumerate(retrieved_chunks, start=1):
#         context_parts.append(
#             f"""[Chunk {index}]
# Title: {chunk.get("page_title", "")}
# Source URL: {chunk.get("source_url", "")}
# Content:
# {chunk.get("content", "")}"""
#         )

#     return "\n\n".join(context_parts)


# def generate_rag_reply(
#     user_message: str,
#     retrieved_chunks: list[dict],
#     conversation_history: list[dict] | None = None,
# ) -> str:
#     client = _get_client()

#     has_retrieval = len(retrieved_chunks) > 0
#     has_history = bool(conversation_history)

#     if has_history and not has_retrieval:
#         system_prompt = """
# You are a helpful internal company assistant.

# This question is about the current chat session memory.

# Rules:
# - Answer using only the conversation history.
# - Do not say there is no prior conversation if history is provided.
# - Do not use outside knowledge.
# - Be direct and specific.
# """
#         messages = [
#             {"role": "system", "content": system_prompt.strip()},
#         ]

#         messages.extend(conversation_history)

#         messages.append(
#             {
#                 "role": "user",
#                 "content": f"""
# User question:
# {user_message}

# Answer only from the earlier conversation in this session.
# """.strip(),
#             }
#         )

#         completion = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=messages,
#             temperature=0.1,
#         )

#         return completion.choices[0].message.content or "No response generated."

#     system_prompt = """
# You are a helpful internal company assistant.

# Rules:
# - For company knowledge questions, answer from the retrieved internal context.
# - If the retrieved context is incomplete, say what is missing clearly.
# - Prefer practical and step-by-step answers when setup instructions are available.
# - Do not invent company-specific details.
# - Do not mention chunks or prompt internals.
# """

#     messages = [
#         {"role": "system", "content": system_prompt.strip()},
#     ]

#     if conversation_history:
#         messages.extend(conversation_history)

#     if has_retrieval:
#         context_text = _build_rag_context(retrieved_chunks)
#         user_prompt = f"""
# User question:
# {user_message}

# Retrieved internal context:
# {context_text}

# Answer the question using the retrieved internal context.
# """
#     else:
#         user_prompt = f"""
# User question:
# {user_message}

# No relevant internal context was retrieved from Confluence.
# If conversation history is relevant, use it.
# Otherwise, clearly say you could not find relevant internal documentation.
# """

#     messages.append({"role": "user", "content": user_prompt.strip()})

#     completion = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=messages,
#         temperature=0.1,
#     )

#     return completion.choices[0].message.content or "No response generated."