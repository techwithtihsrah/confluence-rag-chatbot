# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker

# from app.core.config import settings

# if not settings.POSTGRES_URL:
#     raise ValueError("POSTGRES_URL is missing in .env")

# engine = create_engine(
#     settings.POSTGRES_URL,
#     pool_pre_ping=True,
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine,
# )

# Base = declarative_base()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import settings

if not settings.POSTGRES_URL:
    raise ValueError("POSTGRES_URL is missing in .env")

engine = create_engine(
    settings.POSTGRES_URL,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def run_startup_migrations():
    with engine.begin() as connection:
        connection.execute(
            text(
                """
                ALTER TABLE chat_messages
                ADD COLUMN IF NOT EXISTS sources_json TEXT
                """
            )
        )