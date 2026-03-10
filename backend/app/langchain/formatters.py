from langchain_core.documents import Document


def format_documents_for_prompt(documents: list[Document]) -> str:
    if not documents:
        return ""

    parts: list[str] = []

    for index, document in enumerate(documents, start=1):
        metadata = document.metadata or {}

        page_title = metadata.get("page_title", "") or "Untitled"
        source_url = metadata.get("source_url", "") or ""
        page_id = metadata.get("page_id", "") or ""
        chunk_index = metadata.get("chunk_index", "")

        part = (
            f"[Document {index}]\n"
            f"Page Title: {page_title}\n"
            f"Page ID: {page_id}\n"
            f"Source URL: {source_url}\n"
            f"Chunk Index: {chunk_index}\n"
            f"Content:\n{document.page_content}"
        )
        parts.append(part)

    return "\n\n".join(parts)


def extract_sources_from_documents(documents: list[Document]) -> list[dict]:
    seen: set[tuple[str, str]] = set()
    sources: list[dict] = []

    for document in documents:
        metadata = document.metadata or {}

        page_id = metadata.get("page_id", "") or ""
        page_title = metadata.get("page_title", "") or ""
        source_url = metadata.get("source_url", "") or ""

        source_key = (page_id, source_url)

        if source_key in seen:
            continue

        seen.add(source_key)
        sources.append(
            {
                "page_id": page_id,
                "page_title": page_title,
                "source_url": source_url,
            }
        )

    return sources