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

from app.db.astradb import get_vector_store


def retrieve_similar_chunks(query: str, k: int = 4) -> dict:
    vector_store = get_vector_store()
    documents = vector_store.similarity_search(query, k=k)

    results = []

    for document in documents:
        results.append(
            {
                "content": document.page_content,
                "source_url": document.metadata.get("source_url", ""),
                "page_id": document.metadata.get("page_id", ""),
                "page_title": document.metadata.get("page_title", ""),
                "metadata": document.metadata,
            }
        )

    return {
        "query": query,
        "count": len(results),
        "results": results
    }