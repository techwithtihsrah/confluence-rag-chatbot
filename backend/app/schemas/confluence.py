from typing import List, Optional
from pydantic import BaseModel


class ConfluencePageSummary(BaseModel):
    id: str
    title: str
    url: str


class ConfluencePageListResponse(BaseModel):
    space_key: str
    count: int
    pages: List[ConfluencePageSummary]


class ConfluencePageResponse(BaseModel):
    id: str
    title: str
    url: str
    space_key: str
    version: Optional[int]
    body_storage: str