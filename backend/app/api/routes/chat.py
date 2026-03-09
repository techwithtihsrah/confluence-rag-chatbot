# from fastapi import APIRouter
# from app.schemas.chat import ChatRequest, ChatResponse
# from app.services.chat_service import process_chat_message

# router = APIRouter(tags=["chat"])


# @router.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     result = process_chat_message(request.message)
#     return ChatResponse(**result)

# from fastapi import APIRouter
# from app.schemas.chat import ChatRequest, ChatResponse
# from app.services.chat_service import process_chat_message

# router = APIRouter(tags=["chat"])


# @router.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     result = process_chat_message(
#         user_message=request.message,
#         k=request.k
#     )
#     return ChatResponse(**result)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.postgres import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import process_chat_message

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    try:
        result = process_chat_message(
            db=db,
            user_message=request.message,
            k=request.k,
            session_id=request.session_id,
        )
        return ChatResponse(**result)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))