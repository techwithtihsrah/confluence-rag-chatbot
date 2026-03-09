# # from typing import List
# # from pydantic import BaseModel


# # class ChatRequest(BaseModel):
# #     message: str


# # class ChatResponse(BaseModel):
# #     user_message: str
# #     bot_reply: str
# #     sources: List[str]

# from typing import List
# from pydantic import BaseModel, Field


# class ChatRequest(BaseModel):
#     message: str
#     k: int = Field(default=4, ge=1, le=10)


# class ChatSource(BaseModel):
#     page_id: str
#     page_title: str
#     source_url: str


# class ChatResponse(BaseModel):
#     user_message: str
#     bot_reply: str
#     sources: List[ChatSource]
#     retrieved_chunk_count: int

from typing import List, Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    message: str
    k: int = Field(default=4, ge=1, le=10)
    session_id: Optional[str] = None


class ChatSource(BaseModel):
    page_id: str
    page_title: str
    source_url: str


class ChatResponse(BaseModel):
    session_id: str
    user_message: str
    bot_reply: str
    sources: List[ChatSource]
    retrieved_chunk_count: int