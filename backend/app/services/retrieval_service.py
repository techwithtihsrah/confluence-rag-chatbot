# from app.db.astradb import get_vector_store


# def retrieve_similar_chunks(query: str, k: int = 4) -> dict:
#     vector_store = get_vector_store()
#     documents = vector_store.similarity_search(query, k=k)

#     results = []

#     for document in documents:
#         results.append(
#             {
#                 "content": document.page_content,
#                 "source_url": document.metadata.get("source_url", ""),
#                 "page_id": document.metadata.get("page_id", ""),
#                 "page_title": document.metadata.get("page_title", ""),
#                 "metadata": document.metadata,
#             }
#         )

#     return {
#         "query": query,
#         "count": len(results),
#         "results": results
#     }

from langchain_core.documents import Document

from app.langchain.retrievers import retrieve_documents


def _serialize_document(document: Document) -> dict:
    metadata = document.metadata or {}

    return {
        "content": document.page_content,
        "source_url": metadata.get("source_url", "") or "",
        "page_id": metadata.get("page_id", "") or "",
        "page_title": metadata.get("page_title", "") or "",
        "metadata": metadata,
    }


def search_retrieved_documents(query: str, k: int = 4) -> list[Document]:
    return retrieve_documents(query=query, k=k)


def retrieve_similar_chunks(query: str, k: int = 4) -> dict:
    documents = search_retrieved_documents(query=query, k=k)
    results = [_serialize_document(document) for document in documents]

    return {
        "query": query,
        "count": len(results),
        "results": results,
    }