# from fastapi import APIRouter, Query
# from app.schemas.ingest import CleanPageResponse, ChunkedPageResponse
# from app.services.ingest_service import (
#     get_clean_page_for_ingestion,
#     get_chunked_page_for_ingestion,
# )

# router = APIRouter(prefix="/ingest", tags=["ingest"])


# @router.get("/page/{page_id}/clean", response_model=CleanPageResponse)
# def get_clean_page(page_id: str):
#     page = get_clean_page_for_ingestion(page_id)
#     return CleanPageResponse(**page)


# @router.get("/page/{page_id}/chunks", response_model=ChunkedPageResponse)
# def get_chunked_page(
#     page_id: str,
#     chunk_size: int = Query(default=800, ge=100, le=2000),
#     chunk_overlap: int = Query(default=150, ge=0, le=500),
# ):
#     page = get_chunked_page_for_ingestion(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     return ChunkedPageResponse(**page)

# from fastapi import APIRouter, Query
# from app.schemas.ingest import (
#     CleanPageResponse,
#     ChunkedPageResponse,
#     UpsertPageResponse,
# )
# from app.services.ingest_service import (
#     get_clean_page_for_ingestion,
#     get_chunked_page_for_ingestion,
#     upsert_page_to_vector_store,
# )

# router = APIRouter(prefix="/ingest", tags=["ingest"])


# @router.get("/page/{page_id}/clean", response_model=CleanPageResponse)
# def get_clean_page(page_id: str):
#     page = get_clean_page_for_ingestion(page_id)
#     return CleanPageResponse(**page)


# @router.get("/page/{page_id}/chunks", response_model=ChunkedPageResponse)
# def get_chunked_page(
#     page_id: str,
#     chunk_size: int = Query(default=800, ge=100, le=2000),
#     chunk_overlap: int = Query(default=150, ge=0, le=500),
# ):
#     page = get_chunked_page_for_ingestion(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     return ChunkedPageResponse(**page)


# @router.post("/page/{page_id}/upsert", response_model=UpsertPageResponse)
# def upsert_page(
#     page_id: str,
#     chunk_size: int = Query(default=800, ge=100, le=2000),
#     chunk_overlap: int = Query(default=150, ge=0, le=500),
# ):
#     result = upsert_page_to_vector_store(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     return UpsertPageResponse(**result)

# from fastapi import APIRouter, Query
# from app.schemas.ingest import (
#     CleanPageResponse,
#     ChunkedPageResponse,
#     UpsertPageResponse,
# )
# from app.services.ingest_service import (
#     get_clean_page_for_ingestion,
#     get_chunked_page_for_ingestion,
#     upsert_page_to_vector_store,
# )

# router = APIRouter(prefix="/ingest", tags=["ingest"])


# @router.get("/page/{page_id}/clean", response_model=CleanPageResponse)
# def get_clean_page(page_id: str):
#     page = get_clean_page_for_ingestion(page_id)
#     return CleanPageResponse(**page)


# @router.get("/page/{page_id}/chunks", response_model=ChunkedPageResponse)
# def get_chunked_page(
#     page_id: str,
#     chunk_size: int = Query(default=800, ge=100, le=2000),
#     chunk_overlap: int = Query(default=150, ge=0, le=500),
# ):
#     page = get_chunked_page_for_ingestion(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     return ChunkedPageResponse(**page)


# @router.post("/page/{page_id}/upsert", response_model=UpsertPageResponse)
# def upsert_page(
#     page_id: str,
#     chunk_size: int = Query(default=800, ge=100, le=2000),
#     chunk_overlap: int = Query(default=150, ge=0, le=500),
# ):
#     result = upsert_page_to_vector_store(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )
#     return UpsertPageResponse(**result)

from fastapi import APIRouter, Query
from app.schemas.ingest import (
    BulkUpsertResponse,
    ChunkedPageResponse,
    CleanPageResponse,
    UpsertPageResponse,
)
from app.services.ingest_service import (
    get_chunked_page_for_ingestion,
    get_clean_page_for_ingestion,
    upsert_page_to_vector_store,
    upsert_space_to_vector_store,
)

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.get("/page/{page_id}/clean", response_model=CleanPageResponse)
def get_clean_page(page_id: str):
    page = get_clean_page_for_ingestion(page_id)
    return CleanPageResponse(**page)


@router.get("/page/{page_id}/chunks", response_model=ChunkedPageResponse)
def get_chunked_page(
    page_id: str,
    chunk_size: int = Query(default=800, ge=100, le=2000),
    chunk_overlap: int = Query(default=150, ge=0, le=500),
):
    page = get_chunked_page_for_ingestion(
        page_id=page_id,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return ChunkedPageResponse(**page)


@router.post("/page/{page_id}/upsert", response_model=UpsertPageResponse)
def upsert_page(
    page_id: str,
    chunk_size: int = Query(default=800, ge=100, le=2000),
    chunk_overlap: int = Query(default=150, ge=0, le=500),
):
    result = upsert_page_to_vector_store(
        page_id=page_id,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return UpsertPageResponse(**result)


@router.post("/space/upsert", response_model=BulkUpsertResponse)
def upsert_space(
    limit: int = Query(default=25, ge=1, le=100),
    chunk_size: int = Query(default=800, ge=100, le=2000),
    chunk_overlap: int = Query(default=150, ge=0, le=500),
):
    result = upsert_space_to_vector_store(
        limit=limit,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return BulkUpsertResponse(**result)