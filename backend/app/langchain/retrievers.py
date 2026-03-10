from langchain_core.documents import Document

from app.db.astradb import get_vector_store


DEFAULT_SCORE_THRESHOLD = 0.45
DEFAULT_FETCH_K = 12
DEFAULT_LAMBDA_MULT = 0.5


def get_threshold_retriever(
    k: int = 4,
    score_threshold: float = DEFAULT_SCORE_THRESHOLD,
):
    vector_store = get_vector_store()
    return vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": k,
            "score_threshold": score_threshold,
        },
    )


def get_mmr_retriever(
    k: int = 4,
    fetch_k: int = DEFAULT_FETCH_K,
    lambda_mult: float = DEFAULT_LAMBDA_MULT,
):
    vector_store = get_vector_store()
    return vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": k,
            "fetch_k": fetch_k,
            "lambda_mult": lambda_mult,
        },
    )


def retrieve_documents(
    query: str,
    k: int = 4,
    score_threshold: float = DEFAULT_SCORE_THRESHOLD,
) -> list[Document]:
    normalized_query = (query or "").strip()

    if not normalized_query:
        return []

    retriever = get_threshold_retriever(
        k=k,
        score_threshold=score_threshold,
    )
    documents = retriever.invoke(normalized_query)

    if not documents:
        return []

    return list(documents)