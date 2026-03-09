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
# from app.db.postgres import Base, engine, run_startup_migrations
# from app.models.chat_memory import ChatMessage, ChatSession


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     Base.metadata.create_all(bind=engine)
#     run_startup_migrations()
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
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_origin_regex=r"^https://.*\.vercel\.app$",
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