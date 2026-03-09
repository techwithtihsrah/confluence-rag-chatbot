# from fastapi import APIRouter
# from app.core.config import settings

# router = APIRouter(tags=["health"])


# @router.get("/")
# def read_root():
#     return {"message": "backend is running"}


# @router.get("/health")
# def health_check():
#     return {
#         "status": "ok",
#         "app_name": settings.APP_NAME,
#         "groq_configured": bool(settings.GROQ_API_KEY),
#         "confluence_configured": bool(
#             settings.CONFLUENCE_BASE_URL
#             and settings.CONFLUENCE_EMAIL
#             and settings.CONFLUENCE_API_TOKEN
#             and settings.CONFLUENCE_SPACE_KEY
#         ),
#         "astra_configured": bool(
#             settings.ASTRA_DB_API_ENDPOINT
#             and settings.ASTRA_DB_APPLICATION_TOKEN
#             and settings.ASTRA_DB_COLLECTION
#         ),
#         "postgres_configured": bool(settings.POSTGRES_URL),
#         "embedding_model_name": settings.EMBEDDING_MODEL_NAME,
#     }

from fastapi import APIRouter
from app.core.config import settings

router = APIRouter(tags=["health"])


@router.get("/")
def read_root():
    return {"message": "backend is running"}


@router.get("/health")
def health_check():
    return {
        "status": "ok",
        "app_name": settings.APP_NAME,
        "groq_configured": bool(settings.GROQ_API_KEY),
        "confluence_configured": bool(
            settings.CONFLUENCE_BASE_URL
            and settings.CONFLUENCE_EMAIL
            and settings.CONFLUENCE_API_TOKEN
            and settings.CONFLUENCE_SPACE_KEY
        ),
        "astra_configured": bool(
            settings.ASTRA_DB_API_ENDPOINT
            and settings.ASTRA_DB_APPLICATION_TOKEN
            and settings.ASTRA_DB_COLLECTION
        ),
        "huggingface_configured": bool(
            settings.HF_TOKEN and settings.HF_EMBEDDING_MODEL
        ),
        "postgres_configured": bool(settings.POSTGRES_URL),
        "embedding_model_name": settings.HF_EMBEDDING_MODEL,
    }