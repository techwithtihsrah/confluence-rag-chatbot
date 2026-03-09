# from typing import Any, Dict, List
# from pydantic import BaseModel, Field


# class RetrievalRequest(BaseModel):
#     query: str
#     k: int = Field(default=4, ge=1, le=10)


# class RetrievalResult(BaseModel):
#     content: str
#     source_url: str
#     page_id: str
#     page_title: str
#     metadata: Dict[str, Any]


# class RetrievalResponse(BaseModel):
#     query: str
#     count: int
#     results: List[RetrievalResult]

from typing import Any, Dict, List
from pydantic import BaseModel, Field


class RetrievalRequest(BaseModel):
    query: str
    k: int = Field(default=4, ge=1, le=10)


class RetrievalResult(BaseModel):
    content: str
    source_url: str
    page_id: str
    page_title: str
    metadata: Dict[str, Any]


class RetrievalResponse(BaseModel):
    query: str
    count: int
    results: List[RetrievalResult]