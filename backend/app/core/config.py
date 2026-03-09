# import os
# from dotenv import load_dotenv

# load_dotenv()


# class Settings:
#     APP_NAME = os.getenv("APP_NAME", "Confluence RAG Chatbot")
#     GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

#     CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
#     CONFLUENCE_EMAIL = os.getenv("CONFLUENCE_EMAIL", "")
#     CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN", "")
#     CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")

#     ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT", "").rstrip("/")
#     ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN", "")
#     ASTRA_DB_COLLECTION = os.getenv("ASTRA_DB_COLLECTION", "confluence_docs_hf_api")
#     ASTRA_DB_NAMESPACE = os.getenv("ASTRA_DB_NAMESPACE", "")

#     HF_TOKEN = os.getenv("HF_TOKEN", "")
#     HF_EMBEDDING_MODEL = os.getenv(
#         "HF_EMBEDDING_MODEL",
#         "sentence-transformers/all-MiniLM-L6-v2"
#     )

#     POSTGRES_URL = os.getenv("POSTGRES_URL", "")
#     CHAT_HISTORY_LIMIT = int(os.getenv("CHAT_HISTORY_LIMIT", "6"))

#     FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")


# settings = Settings()

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME", "Confluence RAG Chatbot")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

    CONFLUENCE_BASE_URL = os.getenv("CONFLUENCE_BASE_URL", "").rstrip("/")
    CONFLUENCE_EMAIL = os.getenv("CONFLUENCE_EMAIL", "")
    CONFLUENCE_API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN", "")
    CONFLUENCE_SPACE_KEY = os.getenv("CONFLUENCE_SPACE_KEY", "")

    ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT", "").rstrip("/")
    ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN", "")
    ASTRA_DB_COLLECTION = os.getenv("ASTRA_DB_COLLECTION", "confluence_docs_hf_api")
    ASTRA_DB_NAMESPACE = os.getenv("ASTRA_DB_NAMESPACE", "")

    HF_TOKEN = os.getenv("HF_TOKEN", "")
    HF_EMBEDDING_MODEL = os.getenv(
        "HF_EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    POSTGRES_URL = os.getenv("POSTGRES_URL", "")
    CHAT_HISTORY_LIMIT = int(os.getenv("CHAT_HISTORY_LIMIT", "6"))

    FRONTEND_URL = os.getenv(
        "FRONTEND_URL",
        "http://localhost:3000"
    ).rstrip("/")


settings = Settings()