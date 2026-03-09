# from fastapi import FastAPI, Query
# from app.config import settings
# from app.schemas import ChatRequest, ChatResponse
# from app.services.groq_service import get_chat_reply
# from app.services.confluence_service import get_pages_from_space

# app = FastAPI(title=settings.APP_NAME)


# @app.get("/")
# def read_root():
#     return {"message": "backend is running"}


# @app.get("/health")
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
#         )
#     }


# @app.get("/confluence/pages")
# def list_confluence_pages(limit: int = Query(default=10, ge=1, le=50)):
#     pages = get_pages_from_space(limit=limit)

#     return {
#         "space_key": settings.CONFLUENCE_SPACE_KEY,
#         "count": len(pages),
#         "pages": pages
#     }


# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     bot_reply = get_chat_reply(request.message)

#     return ChatResponse(
#         user_message=request.message,
#         bot_reply=bot_reply,
#         sources=[]
#     )

# from fastapi import FastAPI, Query
# from app.config import settings
# from app.schemas import ChatRequest, ChatResponse
# from app.services.groq_service import get_chat_reply
# from app.services.confluence_service import get_pages_from_space, get_page_by_id

# app = FastAPI(title=settings.APP_NAME)


# @app.get("/")
# def read_root():
#     return {"message": "backend is running"}


# @app.get("/health")
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
#         )
#     }


# @app.get("/confluence/pages")
# def list_confluence_pages(limit: int = Query(default=10, ge=1, le=50)):
#     pages = get_pages_from_space(limit=limit)

#     return {
#         "space_key": settings.CONFLUENCE_SPACE_KEY,
#         "count": len(pages),
#         "pages": pages
#     }


# @app.get("/confluence/page/{page_id}")
# def get_confluence_page(page_id: str):
#     page = get_page_by_id(page_id)
#     return page


# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     bot_reply = get_chat_reply(request.message)

#     return ChatResponse(
#         user_message=request.message,
#         bot_reply=bot_reply,
#         sources=[]
#     )

# from fastapi import FastAPI, Query
# from app.config import settings
# from app.schemas import ChatRequest, ChatResponse
# from app.services.groq_service import get_chat_reply
# from app.services.confluence_service import (
#     get_pages_from_space,
#     get_page_by_id,
#     get_clean_page_by_id,
# )

# app = FastAPI(title=settings.APP_NAME)


# @app.get("/")
# def read_root():
#     return {"message": "backend is running"}


# @app.get("/health")
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
#         )
#     }


# @app.get("/confluence/pages")
# def list_confluence_pages(limit: int = Query(default=10, ge=1, le=50)):
#     pages = get_pages_from_space(limit=limit)

#     return {
#         "space_key": settings.CONFLUENCE_SPACE_KEY,
#         "count": len(pages),
#         "pages": pages
#     }


# @app.get("/confluence/page/{page_id}")
# def get_confluence_page(page_id: str):
#     return get_page_by_id(page_id)


# @app.get("/confluence/page/{page_id}/clean")
# def get_clean_confluence_page(page_id: str):
#     return get_clean_page_by_id(page_id)


# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     bot_reply = get_chat_reply(request.message)

#     return ChatResponse(
#         user_message=request.message,
#         bot_reply=bot_reply,
#         sources=[]
#     )

# from fastapi import FastAPI, Query
# from app.config import settings
# from app.schemas import ChatRequest, ChatResponse
# from app.services.groq_service import get_chat_reply
# from app.services.confluence_service import (
#     get_pages_from_space,
#     get_page_by_id,
#     get_clean_page_by_id,
#     get_chunked_page_by_id,
# )

# app = FastAPI(title=settings.APP_NAME)


# @app.get("/")
# def read_root():
#     return {"message": "backend is running"}


# @app.get("/health")
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
#         )
#     }


# @app.get("/confluence/pages")
# def list_confluence_pages(limit: int = Query(default=10, ge=1, le=50)):
#     pages = get_pages_from_space(limit=limit)

#     return {
#         "space_key": settings.CONFLUENCE_SPACE_KEY,
#         "count": len(pages),
#         "pages": pages
#     }


# @app.get("/confluence/page/{page_id}")
# def get_confluence_page(page_id: str):
#     return get_page_by_id(page_id)


# @app.get("/confluence/page/{page_id}/clean")
# def get_clean_confluence_page(page_id: str):
#     return get_clean_page_by_id(page_id)


# @app.get("/confluence/page/{page_id}/chunks")
# def get_chunked_confluence_page(
#     page_id: str,
#     chunk_size: int = Query(default=500, ge=100, le=2000),
#     overlap: int = Query(default=100, ge=0, le=500),
# ):
#     return get_chunked_page_by_id(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         overlap=overlap
#     )


# @app.post("/chat", response_model=ChatResponse)
# def chat(request: ChatRequest):
#     bot_reply = get_chat_reply(request.message)

#     return ChatResponse(
#         user_message=request.message,
#         bot_reply=bot_reply,
#         sources=[]
#     )

# from fastapi import FastAPI

# from app.core.config import settings
# from app.api.routes.health import router as health_router
# from app.api.routes.chat import router as chat_router
# from app.api.routes.confluence import router as confluence_router
# from app.api.routes.ingest import router as ingest_router

# app = FastAPI(title=settings.APP_NAME)

# app.include_router(health_router)
# app.include_router(chat_router)
# app.include_router(confluence_router)
# app.include_router(ingest_router)

# from fastapi import FastAPI

# from app.core.config import settings
# from app.api.routes.health import router as health_router
# from app.api.routes.chat import router as chat_router
# from app.api.routes.confluence import router as confluence_router
# from app.api.routes.ingest import router as ingest_router
# from app.api.routes.retrieval import router as retrieval_router

# app = FastAPI(title=settings.APP_NAME)

# app.include_router(health_router)
# app.include_router(chat_router)
# app.include_router(confluence_router)
# app.include_router(ingest_router)
# app.include_router(retrieval_router)

# from fastapi import FastAPI

# from app.core.config import settings
# from app.api.routes.health import router as health_router
# from app.api.routes.chat import router as chat_router
# from app.api.routes.confluence import router as confluence_router
# from app.api.routes.ingest import router as ingest_router
# from app.api.routes.retrieval import router as retrieval_router

# app = FastAPI(title=settings.APP_NAME)

# app.include_router(health_router)
# app.include_router(chat_router)
# app.include_router(confluence_router)
# app.include_router(ingest_router)
# app.include_router(retrieval_router)

# from contextlib import asynccontextmanager

# from fastapi import FastAPI

# from app.api.routes.chat import router as chat_router
# from app.api.routes.confluence import router as confluence_router
# from app.api.routes.health import router as health_router
# from app.api.routes.ingest import router as ingest_router
# from app.api.routes.retrieval import router as retrieval_router
# from app.api.routes.sessions import router as sessions_router
# from app.core.config import settings
# from app.db.postgres import Base, engine
# from app.models.chat_memory import ChatMessage, ChatSession


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     Base.metadata.create_all(bind=engine)
#     yield


# app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

# app.include_router(health_router)
# app.include_router(chat_router)
# app.include_router(confluence_router)
# app.include_router(ingest_router)
# app.include_router(retrieval_router)
# app.include_router(sessions_router)

# from contextlib import asynccontextmanager

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.api.routes.chat import router as chat_router
# from app.api.routes.confluence import router as confluence_router
# from app.api.routes.health import router as health_router
# from app.api.routes.ingest import router as ingest_router
# from app.api.routes.retrieval import router as retrieval_router
# from app.api.routes.sessions import router as sessions_router
# from app.core.config import settings
# from app.db.postgres import Base, engine
# from app.models.chat_memory import ChatMessage, ChatSession


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     Base.metadata.create_all(bind=engine)
#     yield


# app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[
#         settings.FRONTEND_URL,
#         "http://127.0.0.1:3000",
#     ],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(health_router)
# app.include_router(chat_router)
# app.include_router(confluence_router)
# app.include_router(ingest_router)
# app.include_router(retrieval_router)
# app.include_router(sessions_router)


from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.chat import router as chat_router
from app.api.routes.confluence import router as confluence_router
from app.api.routes.health import router as health_router
from app.api.routes.ingest import router as ingest_router
from app.api.routes.retrieval import router as retrieval_router
from app.api.routes.sessions import router as sessions_router
from app.core.config import settings
from app.db.postgres import Base, engine, run_startup_migrations
from app.models.chat_memory import ChatMessage, ChatSession


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    run_startup_migrations()
    yield


app = FastAPI(title=settings.APP_NAME, lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(chat_router)
app.include_router(confluence_router)
app.include_router(ingest_router)
app.include_router(retrieval_router)
app.include_router(sessions_router)