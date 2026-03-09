# from datetime import datetime

# from sqlalchemy.orm import Session

# from app.models.chat_memory import ChatMessage, ChatSession


# def _generate_title_from_message(message: str) -> str:
#     cleaned = " ".join(message.strip().split())

#     if not cleaned:
#         return "New Chat"

#     if len(cleaned) <= 60:
#         return cleaned

#     return cleaned[:60].rstrip() + "..."


# def create_session(db: Session, title: str | None = None) -> ChatSession:
#     session = ChatSession(
#         title=title.strip() if title and title.strip() else "New Chat"
#     )
#     db.add(session)
#     db.commit()
#     db.refresh(session)
#     return session


# def get_session_by_id(db: Session, session_id: str) -> ChatSession | None:
#     return (
#         db.query(ChatSession)
#         .filter(ChatSession.id == session_id)
#         .first()
#     )


# def list_sessions(db: Session, limit: int = 50) -> list[ChatSession]:
#     return (
#         db.query(ChatSession)
#         .order_by(ChatSession.updated_at.desc(), ChatSession.created_at.desc())
#         .limit(limit)
#         .all()
#     )


# def get_or_create_session(
#     db: Session,
#     session_id: str | None = None,
#     first_user_message: str | None = None,
# ) -> ChatSession:
#     if session_id:
#         session = get_session_by_id(db, session_id)
#         if not session:
#             raise ValueError("Session not found")
#         return session

#     title = _generate_title_from_message(first_user_message or "")
#     return create_session(db, title=title)


# def update_session_title_if_needed(
#     db: Session,
#     session: ChatSession,
#     first_user_message: str,
# ) -> ChatSession:
#     has_messages = (
#         db.query(ChatMessage)
#         .filter(ChatMessage.session_id == session.id)
#         .count()
#     )

#     if session.title == "New Chat" and has_messages == 0:
#         session.title = _generate_title_from_message(first_user_message)
#         session.updated_at = datetime.utcnow()
#         db.commit()
#         db.refresh(session)

#     return session


# def save_message(db: Session, session_id: str, role: str, content: str) -> ChatMessage:
#     message = ChatMessage(
#         session_id=session_id,
#         role=role,
#         content=content,
#     )
#     db.add(message)

#     session = get_session_by_id(db, session_id)
#     if session:
#         session.updated_at = datetime.utcnow()

#     db.commit()
#     db.refresh(message)
#     return message


# def get_recent_messages(db: Session, session_id: str, limit: int = 6) -> list[dict]:
#     messages = (
#         db.query(ChatMessage)
#         .filter(ChatMessage.session_id == session_id)
#         .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
#         .all()
#     )

#     if limit > 0:
#         messages = messages[-limit:]

#     return [
#         {
#             "role": message.role,
#             "content": message.content
#         }
#         for message in messages
#     ]


# def get_session_messages(db: Session, session_id: str) -> list[ChatMessage]:
#     return (
#         db.query(ChatMessage)
#         .filter(ChatMessage.session_id == session_id)
#         .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
#         .all()
#     )
# working without delete button
# import json
# from datetime import datetime

# from sqlalchemy.orm import Session

# from app.models.chat_memory import ChatMessage, ChatSession


# def _generate_title_from_message(message: str) -> str:
#     cleaned = " ".join(message.strip().split())

#     if not cleaned:
#         return "New Chat"

#     if len(cleaned) <= 60:
#         return cleaned

#     return cleaned[:60].rstrip() + "..."


# def create_session(db: Session, title: str | None = None) -> ChatSession:
#     session = ChatSession(
#         title=title.strip() if title and title.strip() else "New Chat"
#     )
#     db.add(session)
#     db.commit()
#     db.refresh(session)
#     return session


# def get_session_by_id(db: Session, session_id: str) -> ChatSession | None:
#     return (
#         db.query(ChatSession)
#         .filter(ChatSession.id == session_id)
#         .first()
#     )


# def list_sessions(db: Session, limit: int = 50) -> list[ChatSession]:
#     return (
#         db.query(ChatSession)
#         .order_by(ChatSession.updated_at.desc(), ChatSession.created_at.desc())
#         .limit(limit)
#         .all()
#     )


# def get_or_create_session(
#     db: Session,
#     session_id: str | None = None,
#     first_user_message: str | None = None,
# ) -> ChatSession:
#     if session_id:
#         session = get_session_by_id(db, session_id)
#         if not session:
#             raise ValueError("Session not found")
#         return session

#     title = _generate_title_from_message(first_user_message or "")
#     return create_session(db, title=title)


# def update_session_title_if_needed(
#     db: Session,
#     session: ChatSession,
#     first_user_message: str,
# ) -> ChatSession:
#     has_messages = (
#         db.query(ChatMessage)
#         .filter(ChatMessage.session_id == session.id)
#         .count()
#     )

#     if session.title == "New Chat" and has_messages == 0:
#         session.title = _generate_title_from_message(first_user_message)
#         session.updated_at = datetime.utcnow()
#         db.commit()
#         db.refresh(session)

#     return session


# def save_message(
#     db: Session,
#     session_id: str,
#     role: str,
#     content: str,
#     sources: list[dict] | None = None,
# ) -> ChatMessage:
#     message = ChatMessage(
#         session_id=session_id,
#         role=role,
#         content=content,
#         sources_json=json.dumps(sources or []),
#     )
#     db.add(message)

#     session = get_session_by_id(db, session_id)
#     if session:
#         session.updated_at = datetime.utcnow()

#     db.commit()
#     db.refresh(message)
#     return message


# def get_recent_messages(db: Session, session_id: str, limit: int = 6) -> list[dict]:
#     messages = (
#         db.query(ChatMessage)
#         .filter(ChatMessage.session_id == session_id)
#         .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
#         .all()
#     )

#     if limit > 0:
#         messages = messages[-limit:]

#     return [
#         {
#             "role": message.role,
#             "content": message.content
#         }
#         for message in messages
#     ]


# def get_session_messages(db: Session, session_id: str) -> list[dict]:
#     messages = (
#         db.query(ChatMessage)
#         .filter(ChatMessage.session_id == session_id)
#         .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
#         .all()
#     )

#     normalized_messages = []

#     for message in messages:
#         try:
#             sources = json.loads(message.sources_json) if message.sources_json else []
#         except json.JSONDecodeError:
#             sources = []

#         normalized_messages.append(
#             {
#                 "id": message.id,
#                 "role": message.role,
#                 "content": message.content,
#                 "created_at": message.created_at,
#                 "sources": sources,
#             }
#         )

#     return normalized_messages

import json
from datetime import datetime

from sqlalchemy.orm import Session

from app.models.chat_memory import ChatMessage, ChatSession


def _generate_title_from_message(message: str) -> str:
    cleaned = " ".join(message.strip().split())

    if not cleaned:
        return "New Chat"

    if len(cleaned) <= 60:
        return cleaned

    return cleaned[:60].rstrip() + "..."


def create_session(db: Session, title: str | None = None) -> ChatSession:
    session = ChatSession(
        title=title.strip() if title and title.strip() else "New Chat"
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def get_session_by_id(db: Session, session_id: str) -> ChatSession | None:
    return (
        db.query(ChatSession)
        .filter(ChatSession.id == session_id)
        .first()
    )


def list_sessions(db: Session, limit: int = 50) -> list[ChatSession]:
    return (
        db.query(ChatSession)
        .order_by(ChatSession.updated_at.desc(), ChatSession.created_at.desc())
        .limit(limit)
        .all()
    )


def delete_session(db: Session, session_id: str) -> bool:
    session = get_session_by_id(db, session_id)

    if not session:
        return False

    db.delete(session)
    db.commit()
    return True


def get_or_create_session(
    db: Session,
    session_id: str | None = None,
    first_user_message: str | None = None,
) -> ChatSession:
    if session_id:
        session = get_session_by_id(db, session_id)
        if not session:
            raise ValueError("Session not found")
        return session

    title = _generate_title_from_message(first_user_message or "")
    return create_session(db, title=title)


def update_session_title_if_needed(
    db: Session,
    session: ChatSession,
    first_user_message: str,
) -> ChatSession:
    has_messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session.id)
        .count()
    )

    if session.title == "New Chat" and has_messages == 0:
        session.title = _generate_title_from_message(first_user_message)
        session.updated_at = datetime.utcnow()
        db.commit()
        db.refresh(session)

    return session


def save_message(
    db: Session,
    session_id: str,
    role: str,
    content: str,
    sources: list[dict] | None = None,
) -> ChatMessage:
    message = ChatMessage(
        session_id=session_id,
        role=role,
        content=content,
        sources_json=json.dumps(sources or []),
    )
    db.add(message)

    session = get_session_by_id(db, session_id)
    if session:
        session.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(message)
    return message


def get_recent_messages(db: Session, session_id: str, limit: int = 6) -> list[dict]:
    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
        .all()
    )

    if limit > 0:
        messages = messages[-limit:]

    return [
        {
            "role": message.role,
            "content": message.content
        }
        for message in messages
    ]


def get_session_messages(db: Session, session_id: str) -> list[dict]:
    messages = (
        db.query(ChatMessage)
        .filter(ChatMessage.session_id == session_id)
        .order_by(ChatMessage.created_at.asc(), ChatMessage.id.asc())
        .all()
    )

    normalized_messages = []

    for message in messages:
        try:
            sources = json.loads(message.sources_json) if message.sources_json else []
        except json.JSONDecodeError:
            sources = []

        normalized_messages.append(
            {
                "id": message.id,
                "role": message.role,
                "content": message.content,
                "created_at": message.created_at,
                "sources": sources,
            }
        )

    return normalized_messages