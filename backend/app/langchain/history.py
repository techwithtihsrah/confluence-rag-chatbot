from typing import Iterable

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.messages.utils import trim_messages
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.chat_memory import ChatMessage


def _to_langchain_message(role: str, content: str) -> BaseMessage:
    normalized_role = (role or "").strip().lower()
    normalized_content = (content or "").strip()

    if normalized_role == "assistant":
        return AIMessage(content=normalized_content)

    if normalized_role == "system":
        return SystemMessage(content=normalized_content)

    return HumanMessage(content=normalized_content)


def _convert_db_messages_to_langchain(messages: Iterable[ChatMessage]) -> list[BaseMessage]:
    converted: list[BaseMessage] = []

    for message in messages:
        if not message.content or not message.content.strip():
            continue

        converted.append(
            _to_langchain_message(
                role=message.role,
                content=message.content,
            )
        )

    return converted


def load_session_history_messages(
    db: Session,
    session_id: str,
    limit: int | None = None,
) -> list[BaseMessage]:
    max_messages = limit if limit is not None else settings.CHAT_HISTORY_LIMIT

    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
        .all()
    )

    langchain_messages = _convert_db_messages_to_langchain(messages)

    if max_messages is None or max_messages <= 0:
        return langchain_messages

    if not langchain_messages:
        return []

    try:
        trimmed_messages = trim_messages(
            messages=langchain_messages,
            token_counter=len,
            max_tokens=max_messages,
            strategy="last",
            start_on="human",
            include_system=True,
            allow_partial=False,
        )
        return list(trimmed_messages)
    except Exception:
        return langchain_messages[-max_messages:]