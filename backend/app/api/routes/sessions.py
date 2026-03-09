# from fastapi import APIRouter, Depends, HTTPException, Query
# from sqlalchemy.orm import Session

# from app.db.postgres import get_db
# from app.schemas.session import (
#     SessionCreateRequest,
#     SessionDetailResponse,
#     SessionListResponse,
#     SessionMessageResponse,
#     SessionSummary,
# )
# from app.services.session_service import (
#     create_session,
#     get_session_by_id,
#     get_session_messages,
#     list_sessions,
# )

# router = APIRouter(prefix="/sessions", tags=["sessions"])


# @router.post("", response_model=SessionSummary)
# def create_new_session(
#     request: SessionCreateRequest,
#     db: Session = Depends(get_db)
# ):
#     session = create_session(db=db, title=request.title)
#     return SessionSummary(
#         id=session.id,
#         title=session.title,
#         created_at=session.created_at,
#         updated_at=session.updated_at,
#     )


# @router.get("", response_model=SessionListResponse)
# def get_sessions(
#     limit: int = Query(default=50, ge=1, le=200),
#     db: Session = Depends(get_db)
# ):
#     sessions = list_sessions(db=db, limit=limit)

#     return SessionListResponse(
#         count=len(sessions),
#         sessions=[
#             SessionSummary(
#                 id=session.id,
#                 title=session.title,
#                 created_at=session.created_at,
#                 updated_at=session.updated_at,
#             )
#             for session in sessions
#         ]
#     )


# @router.get("/{session_id}", response_model=SessionDetailResponse)
# def get_session_detail(session_id: str, db: Session = Depends(get_db)):
#     session = get_session_by_id(db=db, session_id=session_id)

#     if not session:
#         raise HTTPException(status_code=404, detail="Session not found")

#     messages = get_session_messages(db=db, session_id=session_id)

#     return SessionDetailResponse(
#         id=session.id,
#         title=session.title,
#         created_at=session.created_at,
#         updated_at=session.updated_at,
#         messages=[
#             SessionMessageResponse(
#                 id=message.id,
#                 role=message.role,
#                 content=message.content,
#                 created_at=message.created_at,
#             )
#             for message in messages
#         ]
#     )

# from fastapi import APIRouter, Depends, HTTPException, Query
# from sqlalchemy.orm import Session

# from app.db.postgres import get_db
# from app.schemas.session import (
#     SessionCreateRequest,
#     SessionDetailResponse,
#     SessionListResponse,
#     SessionMessageResponse,
#     SessionSummary,
# )
# from app.services.session_service import (
#     create_session,
#     get_session_by_id,
#     get_session_messages,
#     list_sessions,
# )

# router = APIRouter(prefix="/sessions", tags=["sessions"])


# @router.post("", response_model=SessionSummary)
# def create_new_session(
#     request: SessionCreateRequest,
#     db: Session = Depends(get_db)
# ):
#     session = create_session(db=db, title=request.title)
#     return SessionSummary(
#         id=session.id,
#         title=session.title,
#         created_at=session.created_at,
#         updated_at=session.updated_at,
#     )


# @router.get("", response_model=SessionListResponse)
# def get_sessions(
#     limit: int = Query(default=50, ge=1, le=200),
#     db: Session = Depends(get_db)
# ):
#     sessions = list_sessions(db=db, limit=limit)

#     return SessionListResponse(
#         count=len(sessions),
#         sessions=[
#             SessionSummary(
#                 id=session.id,
#                 title=session.title,
#                 created_at=session.created_at,
#                 updated_at=session.updated_at,
#             )
#             for session in sessions
#         ]
#     )


# @router.get("/{session_id}", response_model=SessionDetailResponse)
# def get_session_detail(session_id: str, db: Session = Depends(get_db)):
#     session = get_session_by_id(db=db, session_id=session_id)

#     if not session:
#         raise HTTPException(status_code=404, detail="Session not found")

#     messages = get_session_messages(db=db, session_id=session_id)

#     return SessionDetailResponse(
#         id=session.id,
#         title=session.title,
#         created_at=session.created_at,
#         updated_at=session.updated_at,
#         messages=[
#             SessionMessageResponse(
#                 id=message["id"],
#                 role=message["role"],
#                 content=message["content"],
#                 created_at=message["created_at"],
#                 sources=message["sources"],
#             )
#             for message in messages
#         ]
#     )

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.postgres import get_db
from app.schemas.session import (
    SessionCreateRequest,
    SessionDetailResponse,
    SessionListResponse,
    SessionMessageResponse,
    SessionSummary,
)
from app.services.session_service import (
    create_session,
    delete_session,
    get_session_by_id,
    get_session_messages,
    list_sessions,
)

router = APIRouter(prefix="/sessions", tags=["sessions"])


@router.post("", response_model=SessionSummary)
def create_new_session(
    request: SessionCreateRequest,
    db: Session = Depends(get_db)
):
    session = create_session(db=db, title=request.title)
    return SessionSummary(
        id=session.id,
        title=session.title,
        created_at=session.created_at,
        updated_at=session.updated_at,
    )


@router.get("", response_model=SessionListResponse)
def get_sessions(
    limit: int = Query(default=50, ge=1, le=200),
    db: Session = Depends(get_db)
):
    sessions = list_sessions(db=db, limit=limit)

    return SessionListResponse(
        count=len(sessions),
        sessions=[
            SessionSummary(
                id=session.id,
                title=session.title,
                created_at=session.created_at,
                updated_at=session.updated_at,
            )
            for session in sessions
        ]
    )


@router.get("/{session_id}", response_model=SessionDetailResponse)
def get_session_detail(session_id: str, db: Session = Depends(get_db)):
    session = get_session_by_id(db=db, session_id=session_id)

    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    messages = get_session_messages(db=db, session_id=session_id)

    return SessionDetailResponse(
        id=session.id,
        title=session.title,
        created_at=session.created_at,
        updated_at=session.updated_at,
        messages=[
            SessionMessageResponse(
                id=message["id"],
                role=message["role"],
                content=message["content"],
                created_at=message["created_at"],
                sources=message["sources"],
            )
            for message in messages
        ]
    )


@router.delete("/{session_id}")
def delete_session_route(session_id: str, db: Session = Depends(get_db)):
    deleted = delete_session(db=db, session_id=session_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Session not found")

    return {
        "message": "Session deleted successfully",
        "session_id": session_id,
    }