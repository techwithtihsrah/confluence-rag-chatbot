from fastapi import APIRouter, Query
from app.core.config import settings
from app.schemas.confluence import ConfluencePageListResponse, ConfluencePageResponse
from app.services.confluence_service import get_pages_from_space, get_page_by_id

router = APIRouter(prefix="/confluence", tags=["confluence"])


@router.get("/pages", response_model=ConfluencePageListResponse)
def list_confluence_pages(limit: int = Query(default=10, ge=1, le=50)):
    pages = get_pages_from_space(limit=limit)

    return ConfluencePageListResponse(
        space_key=settings.CONFLUENCE_SPACE_KEY,
        count=len(pages),
        pages=pages
    )


@router.get("/page/{page_id}", response_model=ConfluencePageResponse)
def get_confluence_page(page_id: str):
    page = get_page_by_id(page_id)
    return ConfluencePageResponse(**page)