# from typing import Any, Dict, List, Optional
# from pydantic import BaseModel


# class CleanPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     clean_text: str


# class ChunkResponse(BaseModel):
#     chunk_id: str
#     chunk_index: int
#     content: str
#     source_url: str
#     page_id: str
#     page_title: str
#     metadata: Dict[str, Any]


# class ChunkedPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     chunk_count: int
#     chunks: List[ChunkResponse]

# from typing import Any, Dict, List, Optional
# from pydantic import BaseModel


# class CleanPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     clean_text: str


# class ChunkResponse(BaseModel):
#     chunk_id: str
#     chunk_index: int
#     content: str
#     source_url: str
#     page_id: str
#     page_title: str
#     metadata: Dict[str, Any]


# class ChunkedPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     chunk_count: int
#     chunks: List[ChunkResponse]


# class UpsertPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     chunk_count: int
#     collection_name: str
#     inserted_ids: List[str]

# from typing import Any, Dict, List, Optional
# from pydantic import BaseModel


# class CleanPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     clean_text: str


# class ChunkResponse(BaseModel):
#     chunk_id: str
#     chunk_index: int
#     content: str
#     source_url: str
#     page_id: str
#     page_title: str
#     metadata: Dict[str, Any]


# class ChunkedPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     chunk_count: int
#     chunks: List[ChunkResponse]


# class UpsertPageResponse(BaseModel):
#     id: str
#     title: str
#     url: str
#     space_key: str
#     version: Optional[int]
#     chunk_count: int
#     collection_name: str
#     inserted_ids: List[str]

from typing import Any, Dict, List, Optional
from pydantic import BaseModel


class CleanPageResponse(BaseModel):
    id: str
    title: str
    url: str
    space_key: str
    version: Optional[int]
    clean_text: str


class ChunkResponse(BaseModel):
    chunk_id: str
    chunk_index: int
    content: str
    source_url: str
    page_id: str
    page_title: str
    metadata: Dict[str, Any]


class ChunkedPageResponse(BaseModel):
    id: str
    title: str
    url: str
    space_key: str
    version: Optional[int]
    chunk_count: int
    chunks: List[ChunkResponse]


class UpsertPageResponse(BaseModel):
    id: str
    title: str
    url: str
    space_key: str
    version: Optional[int]
    chunk_count: int
    collection_name: str
    inserted_ids: List[str]


class BulkUpsertPageResult(BaseModel):
    page_id: str
    page_title: str
    success: bool
    chunk_count: int
    error: Optional[str] = None


class BulkUpsertResponse(BaseModel):
    space_key: str
    total_pages_found: int
    total_pages_processed: int
    total_successful_pages: int
    total_failed_pages: int
    total_chunks_upserted: int
    collection_name: str
    results: List[BulkUpsertPageResult]