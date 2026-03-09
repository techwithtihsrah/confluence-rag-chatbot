# from functools import lru_cache

# from langchain_astradb import AstraDBVectorStore
# from langchain_huggingface import HuggingFaceEmbeddings

# from app.core.config import settings


# @lru_cache
# def get_embeddings():
#     return HuggingFaceEmbeddings(
#         model_name=settings.EMBEDDING_MODEL_NAME
#     )


# @lru_cache
# def get_vector_store():
#     if not settings.ASTRA_DB_API_ENDPOINT:
#         raise ValueError("ASTRA_DB_API_ENDPOINT is missing in .env")

#     if not settings.ASTRA_DB_APPLICATION_TOKEN:
#         raise ValueError("ASTRA_DB_APPLICATION_TOKEN is missing in .env")

#     namespace = settings.ASTRA_DB_NAMESPACE or None

#     return AstraDBVectorStore(
#         collection_name=settings.ASTRA_DB_COLLECTION,
#         embedding=get_embeddings(),
#         api_endpoint=settings.ASTRA_DB_API_ENDPOINT,
#         token=settings.ASTRA_DB_APPLICATION_TOKEN,
#         namespace=namespace,
#     )