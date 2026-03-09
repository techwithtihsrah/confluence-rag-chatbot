# from langchain_text_splitters import RecursiveCharacterTextSplitter

# from app.services.confluence_service import get_page_by_id
# from app.utils.text_cleaner import clean_confluence_storage_html


# def get_clean_page_for_ingestion(page_id: str) -> dict:
#     page = get_page_by_id(page_id)
#     clean_text = clean_confluence_storage_html(page["body_storage"])

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "clean_text": clean_text
#     }


# def get_chunked_page_for_ingestion(
#     page_id: str,
#     chunk_size: int = 800,
#     chunk_overlap: int = 150
# ) -> dict:
#     if chunk_overlap >= chunk_size:
#         raise ValueError("chunk_overlap must be smaller than chunk_size")

#     page = get_clean_page_for_ingestion(page_id)

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap,
#         separators=["\n\n", "\n", " ", ""]
#     )

#     documents = splitter.create_documents(
#         texts=[page["clean_text"]],
#         metadatas=[
#             {
#                 "page_id": page["id"],
#                 "page_title": page["title"],
#                 "source_url": page["url"],
#                 "space_key": page["space_key"],
#                 "version": page["version"],
#             }
#         ]
#     )

#     chunks = []

#     for index, document in enumerate(documents):
#         chunks.append(
#             {
#                 "chunk_id": f"{page['id']}_chunk_{index}",
#                 "chunk_index": index,
#                 "content": document.page_content,
#                 "source_url": page["url"],
#                 "page_id": page["id"],
#                 "page_title": page["title"],
#                 "metadata": document.metadata,
#             }
#         )

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "chunk_count": len(chunks),
#         "chunks": chunks
#     }

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# from app.core.config import settings
# from app.db.astradb import get_vector_store
# from app.services.confluence_service import get_page_by_id
# from app.utils.text_cleaner import clean_confluence_storage_html


# def get_clean_page_for_ingestion(page_id: str) -> dict:
#     page = get_page_by_id(page_id)
#     clean_text = clean_confluence_storage_html(page["body_storage"])

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "clean_text": clean_text
#     }


# def _build_chunk_documents(
#     page_id: str,
#     chunk_size: int = 800,
#     chunk_overlap: int = 150
# ):
#     if chunk_overlap >= chunk_size:
#         raise ValueError("chunk_overlap must be smaller than chunk_size")

#     page = get_clean_page_for_ingestion(page_id)

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap,
#         separators=["\n\n", "\n", " ", ""]
#     )

#     documents = splitter.create_documents(
#         texts=[page["clean_text"]],
#         metadatas=[
#             {
#                 "page_id": page["id"],
#                 "page_title": page["title"],
#                 "source_url": page["url"],
#                 "space_key": page["space_key"],
#                 "version": page["version"],
#             }
#         ]
#     )

#     for index, document in enumerate(documents):
#         document.metadata["chunk_id"] = f"{page['id']}_chunk_{index}"
#         document.metadata["chunk_index"] = index

#     return page, documents


# def get_chunked_page_for_ingestion(
#     page_id: str,
#     chunk_size: int = 800,
#     chunk_overlap: int = 150
# ) -> dict:
#     page, documents = _build_chunk_documents(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )

#     chunks = []

#     for document in documents:
#         chunks.append(
#             {
#                 "chunk_id": document.metadata["chunk_id"],
#                 "chunk_index": document.metadata["chunk_index"],
#                 "content": document.page_content,
#                 "source_url": document.metadata["source_url"],
#                 "page_id": document.metadata["page_id"],
#                 "page_title": document.metadata["page_title"],
#                 "metadata": document.metadata,
#             }
#         )

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "chunk_count": len(chunks),
#         "chunks": chunks
#     }


# def upsert_page_to_vector_store(
#     page_id: str,
#     chunk_size: int = 800,
#     chunk_overlap: int = 150
# ) -> dict:
#     page, documents = _build_chunk_documents(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )

#     vector_store = get_vector_store()
#     ids = [document.metadata["chunk_id"] for document in documents]

#     vector_store.add_documents(documents=documents, ids=ids)

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "chunk_count": len(documents),
#         "collection_name": settings.ASTRA_DB_COLLECTION,
#         "inserted_ids": ids,
#     }

# from langchain_text_splitters import RecursiveCharacterTextSplitter

# from app.core.config import settings
# from app.db.astradb import get_vector_store
# from app.services.confluence_service import get_page_by_id
# from app.utils.text_cleaner import clean_confluence_storage_html


# def get_clean_page_for_ingestion(page_id: str) -> dict:
#     page = get_page_by_id(page_id)
#     clean_text = clean_confluence_storage_html(page["body_storage"])

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "clean_text": clean_text
#     }


# def _build_chunk_documents(
#     page_id: str,
#     chunk_size: int = 800,
#     chunk_overlap: int = 150
# ):
#     if chunk_overlap >= chunk_size:
#         raise ValueError("chunk_overlap must be smaller than chunk_size")

#     page = get_clean_page_for_ingestion(page_id)

#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap,
#         separators=["\n\n", "\n", " ", ""]
#     )

#     documents = splitter.create_documents(
#         texts=[page["clean_text"]],
#         metadatas=[
#             {
#                 "page_id": page["id"],
#                 "page_title": page["title"],
#                 "source_url": page["url"],
#                 "space_key": page["space_key"],
#                 "version": page["version"],
#             }
#         ]
#     )

#     for index, document in enumerate(documents):
#         document.metadata["chunk_id"] = f"{page['id']}_chunk_{index}"
#         document.metadata["chunk_index"] = index

#     return page, documents


# def get_chunked_page_for_ingestion(
#     page_id: str,
#     chunk_size: int = 800,
#     chunk_overlap: int = 150
# ) -> dict:
#     page, documents = _build_chunk_documents(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )

#     chunks = []

#     for document in documents:
#         chunks.append(
#             {
#                 "chunk_id": document.metadata["chunk_id"],
#                 "chunk_index": document.metadata["chunk_index"],
#                 "content": document.page_content,
#                 "source_url": document.metadata["source_url"],
#                 "page_id": document.metadata["page_id"],
#                 "page_title": document.metadata["page_title"],
#                 "metadata": document.metadata,
#             }
#         )

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "chunk_count": len(chunks),
#         "chunks": chunks
#     }


# def upsert_page_to_vector_store(
#     page_id: str,
#     chunk_size: int = 800,
#     chunk_overlap: int = 150
# ) -> dict:
#     page, documents = _build_chunk_documents(
#         page_id=page_id,
#         chunk_size=chunk_size,
#         chunk_overlap=chunk_overlap
#     )

#     vector_store = get_vector_store()
#     ids = [document.metadata["chunk_id"] for document in documents]

#     vector_store.add_documents(documents=documents, ids=ids)

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "chunk_count": len(documents),
#         "collection_name": settings.ASTRA_DB_COLLECTION,
#         "inserted_ids": ids,
#     }

from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings
from app.db.astradb import get_vector_store
from app.services.confluence_service import get_all_pages_from_space, get_page_by_id
from app.utils.text_cleaner import clean_confluence_storage_html


def get_clean_page_for_ingestion(page_id: str) -> dict:
    page = get_page_by_id(page_id)
    clean_text = clean_confluence_storage_html(page["body_storage"])

    return {
        "id": page["id"],
        "title": page["title"],
        "url": page["url"],
        "space_key": page["space_key"],
        "version": page["version"],
        "clean_text": clean_text
    }


def _build_chunk_documents(
    page_id: str,
    chunk_size: int = 800,
    chunk_overlap: int = 150
):
    if chunk_overlap >= chunk_size:
        raise ValueError("chunk_overlap must be smaller than chunk_size")

    page = get_clean_page_for_ingestion(page_id)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    documents = splitter.create_documents(
        texts=[page["clean_text"]],
        metadatas=[
            {
                "page_id": page["id"],
                "page_title": page["title"],
                "source_url": page["url"],
                "space_key": page["space_key"],
                "version": page["version"],
            }
        ]
    )

    for index, document in enumerate(documents):
        document.metadata["chunk_id"] = f"{page['id']}_chunk_{index}"
        document.metadata["chunk_index"] = index

    return page, documents


def get_chunked_page_for_ingestion(
    page_id: str,
    chunk_size: int = 800,
    chunk_overlap: int = 150
) -> dict:
    page, documents = _build_chunk_documents(
        page_id=page_id,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = []

    for document in documents:
        chunks.append(
            {
                "chunk_id": document.metadata["chunk_id"],
                "chunk_index": document.metadata["chunk_index"],
                "content": document.page_content,
                "source_url": document.metadata["source_url"],
                "page_id": document.metadata["page_id"],
                "page_title": document.metadata["page_title"],
                "metadata": document.metadata,
            }
        )

    return {
        "id": page["id"],
        "title": page["title"],
        "url": page["url"],
        "space_key": page["space_key"],
        "version": page["version"],
        "chunk_count": len(chunks),
        "chunks": chunks
    }


def upsert_page_to_vector_store(
    page_id: str,
    chunk_size: int = 800,
    chunk_overlap: int = 150
) -> dict:
    page, documents = _build_chunk_documents(
        page_id=page_id,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    vector_store = get_vector_store()
    ids = [document.metadata["chunk_id"] for document in documents]

    vector_store.add_documents(documents=documents, ids=ids)

    return {
        "id": page["id"],
        "title": page["title"],
        "url": page["url"],
        "space_key": page["space_key"],
        "version": page["version"],
        "chunk_count": len(documents),
        "collection_name": settings.ASTRA_DB_COLLECTION,
        "inserted_ids": ids,
    }


def upsert_space_to_vector_store(
    limit: int = 25,
    chunk_size: int = 800,
    chunk_overlap: int = 150
) -> dict:
    pages = get_all_pages_from_space(limit=limit)

    results = []
    total_chunks_upserted = 0
    total_successful_pages = 0
    total_failed_pages = 0

    for page in pages:
        page_id = page["id"]
        page_title = page["title"]

        try:
            upsert_result = upsert_page_to_vector_store(
                page_id=page_id,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )

            chunk_count = upsert_result["chunk_count"]
            total_chunks_upserted += chunk_count
            total_successful_pages += 1

            results.append(
                {
                    "page_id": page_id,
                    "page_title": page_title,
                    "success": True,
                    "chunk_count": chunk_count,
                    "error": None,
                }
            )
        except Exception as exc:
            total_failed_pages += 1
            results.append(
                {
                    "page_id": page_id,
                    "page_title": page_title,
                    "success": False,
                    "chunk_count": 0,
                    "error": str(exc),
                }
            )

    return {
        "space_key": settings.CONFLUENCE_SPACE_KEY,
        "total_pages_found": len(pages),
        "total_pages_processed": len(results),
        "total_successful_pages": total_successful_pages,
        "total_failed_pages": total_failed_pages,
        "total_chunks_upserted": total_chunks_upserted,
        "collection_name": settings.ASTRA_DB_COLLECTION,
        "results": results,
    }