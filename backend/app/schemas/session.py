# from datetime import datetime
# from typing import List, Optional

# from pydantic import BaseModel, Field


# class SessionCreateRequest(BaseModel):
#     title: Optional[str] = Field(default=None, max_length=200)


# class SessionSummary(BaseModel):
#     id: str
#     title: str
#     created_at: datetime
#     updated_at: datetime


# class SessionListResponse(BaseModel):
#     count: int
#     sessions: List[SessionSummary]


# class SessionMessageResponse(BaseModel):
#     id: int
#     role: str
#     content: str
#     created_at: datetime


# class SessionDetailResponse(BaseModel):
#     id: str
#     title: str
#     created_at: datetime
#     updated_at: datetime
#     messages: List[SessionMessageResponse]

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class SessionCreateRequest(BaseModel):
    title: Optional[str] = Field(default=None, max_length=200)


class SessionSource(BaseModel):
    page_id: str
    page_title: str
    source_url: str


class SessionSummary(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime


class SessionListResponse(BaseModel):
    count: int
    sessions: List[SessionSummary]


class SessionMessageResponse(BaseModel):
    id: int
    role: str
    content: str
    created_at: datetime
    sources: List[SessionSource] = []


class SessionDetailResponse(BaseModel):
    id: str
    title: str
    created_at: datetime
    updated_at: datetime
    messages: List[SessionMessageResponse]