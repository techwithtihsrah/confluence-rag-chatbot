# from typing import List, Dict
# from requests.auth import HTTPBasicAuth
# import requests

# from app.config import settings


# def _get_auth():
#     if not settings.CONFLUENCE_EMAIL or not settings.CONFLUENCE_API_TOKEN:
#         raise ValueError("Confluence email or API token is missing in .env")

#     return HTTPBasicAuth(settings.CONFLUENCE_EMAIL, settings.CONFLUENCE_API_TOKEN)


# def _get_headers():
#     return {
#         "Accept": "application/json"
#     }


# def _build_full_url(relative_or_absolute_url: str) -> str:
#     if not relative_or_absolute_url:
#         return ""

#     if relative_or_absolute_url.startswith("http://") or relative_or_absolute_url.startswith("https://"):
#         return relative_or_absolute_url

#     return f"{settings.CONFLUENCE_BASE_URL}{relative_or_absolute_url}"


# def get_pages_from_space(limit: int = 10) -> List[Dict]:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     if not settings.CONFLUENCE_SPACE_KEY:
#         raise ValueError("CONFLUENCE_SPACE_KEY is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/search"

#     cql = f'space="{settings.CONFLUENCE_SPACE_KEY}" and type=page'

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "cql": cql,
#             "limit": limit
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence API error: {response.status_code} - {response.text}"
#         )

#     data = response.json()
#     results = data.get("results", [])

#     pages = []

#     for item in results:
#         title = item.get("title", "Untitled")
#         page_id = item.get("id", "")
#         links = item.get("_links", {})
#         webui = links.get("webui", "")
#         page_url = _build_full_url(webui)

#         pages.append(
#             {
#                 "id": page_id,
#                 "title": title,
#                 "url": page_url
#             }
#         )

#     return pages

# working 2
# from typing import List, Dict
# from requests.auth import HTTPBasicAuth
# import requests

# from app.config import settings


# def _get_auth():
#     if not settings.CONFLUENCE_EMAIL or not settings.CONFLUENCE_API_TOKEN:
#         raise ValueError("Confluence email or API token is missing in .env")

#     return HTTPBasicAuth(settings.CONFLUENCE_EMAIL, settings.CONFLUENCE_API_TOKEN)


# def _get_headers():
#     return {
#         "Accept": "application/json"
#     }


# def _build_full_url(links: Dict) -> str:
#     webui = links.get("webui", "")
#     base = links.get("base", "")

#     if base and webui:
#         return f"{base}{webui}"

#     if webui.startswith("http://") or webui.startswith("https://"):
#         return webui

#     if webui.startswith("/wiki"):
#         return f"{settings.CONFLUENCE_BASE_URL}{webui}"

#     if webui.startswith("/"):
#         return f"{settings.CONFLUENCE_BASE_URL}/wiki{webui}"

#     return ""


# def get_pages_from_space(limit: int = 10) -> List[Dict]:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     if not settings.CONFLUENCE_SPACE_KEY:
#         raise ValueError("CONFLUENCE_SPACE_KEY is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/search"
#     cql = f'space="{settings.CONFLUENCE_SPACE_KEY}" and type=page'

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "cql": cql,
#             "limit": limit
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence API error: {response.status_code} - {response.text}"
#         )

#     data = response.json()
#     results = data.get("results", [])

#     pages = []

#     for item in results:
#         title = item.get("title", "Untitled")
#         page_id = item.get("id", "")
#         links = item.get("_links", {})
#         page_url = _build_full_url(links)

#         pages.append(
#             {
#                 "id": page_id,
#                 "title": title,
#                 "url": page_url
#             }
#         )

#     return pages


# def get_page_by_id(page_id: str) -> Dict:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/{page_id}"

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "expand": "body.storage,version,space"
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence page fetch error: {response.status_code} - {response.text}"
#         )

#     data = response.json()

#     title = data.get("title", "Untitled")
#     page_id_value = data.get("id", "")
#     links = data.get("_links", {})
#     page_url = _build_full_url(links)

#     body_storage = data.get("body", {}).get("storage", {}).get("value", "")
#     version_number = data.get("version", {}).get("number", None)
#     space_key = data.get("space", {}).get("key", "")

#     return {
#         "id": page_id_value,
#         "title": title,
#         "url": page_url,
#         "space_key": space_key,
#         "version": version_number,
#         "body_storage": body_storage
#     }

# from typing import List, Dict
# from requests.auth import HTTPBasicAuth
# import requests

# from app.config import settings
# from app.utils.text_cleaner import clean_confluence_storage_html


# def _get_auth():
#     if not settings.CONFLUENCE_EMAIL or not settings.CONFLUENCE_API_TOKEN:
#         raise ValueError("Confluence email or API token is missing in .env")

#     return HTTPBasicAuth(settings.CONFLUENCE_EMAIL, settings.CONFLUENCE_API_TOKEN)


# def _get_headers():
#     return {
#         "Accept": "application/json"
#     }


# def _build_full_url(links: Dict) -> str:
#     webui = links.get("webui", "")
#     base = links.get("base", "")

#     if base and webui:
#         return f"{base}{webui}"

#     if webui.startswith("http://") or webui.startswith("https://"):
#         return webui

#     if webui.startswith("/wiki"):
#         return f"{settings.CONFLUENCE_BASE_URL}{webui}"

#     if webui.startswith("/"):
#         return f"{settings.CONFLUENCE_BASE_URL}/wiki{webui}"

#     return ""


# def get_pages_from_space(limit: int = 10) -> List[Dict]:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     if not settings.CONFLUENCE_SPACE_KEY:
#         raise ValueError("CONFLUENCE_SPACE_KEY is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/search"
#     cql = f'space="{settings.CONFLUENCE_SPACE_KEY}" and type=page'

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "cql": cql,
#             "limit": limit
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence API error: {response.status_code} - {response.text}"
#         )

#     data = response.json()
#     results = data.get("results", [])

#     pages = []

#     for item in results:
#         title = item.get("title", "Untitled")
#         page_id = item.get("id", "")
#         links = item.get("_links", {})
#         page_url = _build_full_url(links)

#         pages.append(
#             {
#                 "id": page_id,
#                 "title": title,
#                 "url": page_url
#             }
#         )

#     return pages


# def get_page_by_id(page_id: str) -> Dict:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/{page_id}"

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "expand": "body.storage,version,space"
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence page fetch error: {response.status_code} - {response.text}"
#         )

#     data = response.json()

#     title = data.get("title", "Untitled")
#     page_id_value = data.get("id", "")
#     links = data.get("_links", {})
#     page_url = _build_full_url(links)

#     body_storage = data.get("body", {}).get("storage", {}).get("value", "")
#     version_number = data.get("version", {}).get("number", None)
#     space_key = data.get("space", {}).get("key", "")

#     return {
#         "id": page_id_value,
#         "title": title,
#         "url": page_url,
#         "space_key": space_key,
#         "version": version_number,
#         "body_storage": body_storage
#     }


# def get_clean_page_by_id(page_id: str) -> Dict:
#     page = get_page_by_id(page_id)
#     cleaned_text = clean_confluence_storage_html(page["body_storage"])

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "clean_text": cleaned_text
#     }

# from typing import List, Dict
# from requests.auth import HTTPBasicAuth
# import requests

# from app.config import settings
# from app.utils.text_cleaner import clean_confluence_storage_html
# from app.utils.chunker import chunk_text


# def _get_auth():
#     if not settings.CONFLUENCE_EMAIL or not settings.CONFLUENCE_API_TOKEN:
#         raise ValueError("Confluence email or API token is missing in .env")

#     return HTTPBasicAuth(settings.CONFLUENCE_EMAIL, settings.CONFLUENCE_API_TOKEN)


# def _get_headers():
#     return {
#         "Accept": "application/json"
#     }


# def _build_full_url(links: Dict) -> str:
#     webui = links.get("webui", "")
#     base = links.get("base", "")

#     if base and webui:
#         return f"{base}{webui}"

#     if webui.startswith("http://") or webui.startswith("https://"):
#         return webui

#     if webui.startswith("/wiki"):
#         return f"{settings.CONFLUENCE_BASE_URL}{webui}"

#     if webui.startswith("/"):
#         return f"{settings.CONFLUENCE_BASE_URL}/wiki{webui}"

#     return ""


# def get_pages_from_space(limit: int = 10) -> List[Dict]:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     if not settings.CONFLUENCE_SPACE_KEY:
#         raise ValueError("CONFLUENCE_SPACE_KEY is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/search"
#     cql = f'space="{settings.CONFLUENCE_SPACE_KEY}" and type=page'

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "cql": cql,
#             "limit": limit
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence API error: {response.status_code} - {response.text}"
#         )

#     data = response.json()
#     results = data.get("results", [])

#     pages = []

#     for item in results:
#         title = item.get("title", "Untitled")
#         page_id = item.get("id", "")
#         links = item.get("_links", {})
#         page_url = _build_full_url(links)

#         pages.append(
#             {
#                 "id": page_id,
#                 "title": title,
#                 "url": page_url
#             }
#         )

#     return pages


# def get_page_by_id(page_id: str) -> Dict:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/{page_id}"

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "expand": "body.storage,version,space"
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence page fetch error: {response.status_code} - {response.text}"
#         )

#     data = response.json()

#     title = data.get("title", "Untitled")
#     page_id_value = data.get("id", "")
#     links = data.get("_links", {})
#     page_url = _build_full_url(links)

#     body_storage = data.get("body", {}).get("storage", {}).get("value", "")
#     version_number = data.get("version", {}).get("number", None)
#     space_key = data.get("space", {}).get("key", "")

#     return {
#         "id": page_id_value,
#         "title": title,
#         "url": page_url,
#         "space_key": space_key,
#         "version": version_number,
#         "body_storage": body_storage
#     }


# def get_clean_page_by_id(page_id: str) -> Dict:
#     page = get_page_by_id(page_id)
#     cleaned_text = clean_confluence_storage_html(page["body_storage"])

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "clean_text": cleaned_text
#     }


# def get_chunked_page_by_id(
#     page_id: str,
#     chunk_size: int = 500,
#     overlap: int = 100
# ) -> Dict:
#     page = get_clean_page_by_id(page_id)
#     chunks = chunk_text(
#         text=page["clean_text"],
#         chunk_size=chunk_size,
#         overlap=overlap
#     )

#     chunk_objects = []

#     for index, chunk in enumerate(chunks):
#         chunk_objects.append(
#             {
#                 "chunk_id": f"{page_id}_chunk_{index}",
#                 "chunk_index": index,
#                 "content": chunk,
#                 "source_url": page["url"],
#                 "page_id": page["id"],
#                 "page_title": page["title"]
#             }
#         )

#     return {
#         "id": page["id"],
#         "title": page["title"],
#         "url": page["url"],
#         "space_key": page["space_key"],
#         "version": page["version"],
#         "chunk_count": len(chunk_objects),
#         "chunks": chunk_objects
#     }

# from typing import Dict, List
# from requests.auth import HTTPBasicAuth
# import requests

# from app.core.config import settings


# def _get_auth():
#     if not settings.CONFLUENCE_EMAIL or not settings.CONFLUENCE_API_TOKEN:
#         raise ValueError("Confluence email or API token is missing in .env")

#     return HTTPBasicAuth(settings.CONFLUENCE_EMAIL, settings.CONFLUENCE_API_TOKEN)


# def _get_headers():
#     return {
#         "Accept": "application/json"
#     }


# def _build_full_url(links: Dict) -> str:
#     webui = links.get("webui", "")
#     base = links.get("base", "")

#     if base and webui:
#         return f"{base}{webui}"

#     if webui.startswith("http://") or webui.startswith("https://"):
#         return webui

#     if webui.startswith("/wiki"):
#         return f"{settings.CONFLUENCE_BASE_URL}{webui}"

#     if webui.startswith("/"):
#         return f"{settings.CONFLUENCE_BASE_URL}/wiki{webui}"

#     return ""


# def get_pages_from_space(limit: int = 10) -> List[Dict]:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     if not settings.CONFLUENCE_SPACE_KEY:
#         raise ValueError("CONFLUENCE_SPACE_KEY is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/search"
#     cql = f'space="{settings.CONFLUENCE_SPACE_KEY}" and type=page'

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "cql": cql,
#             "limit": limit
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence API error: {response.status_code} - {response.text}"
#         )

#     data = response.json()
#     results = data.get("results", [])

#     pages = []

#     for item in results:
#         title = item.get("title", "Untitled")
#         page_id = item.get("id", "")
#         links = item.get("_links", {})
#         page_url = _build_full_url(links)

#         pages.append(
#             {
#                 "id": page_id,
#                 "title": title,
#                 "url": page_url
#             }
#         )

#     return pages


# def get_page_by_id(page_id: str) -> Dict:
#     if not settings.CONFLUENCE_BASE_URL:
#         raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

#     url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/{page_id}"

#     response = requests.get(
#         url,
#         auth=_get_auth(),
#         headers=_get_headers(),
#         params={
#             "expand": "body.storage,version,space"
#         },
#         timeout=30
#     )

#     if response.status_code != 200:
#         raise Exception(
#             f"Confluence page fetch error: {response.status_code} - {response.text}"
#         )

#     data = response.json()

#     title = data.get("title", "Untitled")
#     page_id_value = data.get("id", "")
#     links = data.get("_links", {})
#     page_url = _build_full_url(links)

#     body_storage = data.get("body", {}).get("storage", {}).get("value", "")
#     version_number = data.get("version", {}).get("number", None)
#     space_key = data.get("space", {}).get("key", "")

#     return {
#         "id": page_id_value,
#         "title": title,
#         "url": page_url,
#         "space_key": space_key,
#         "version": version_number,
#         "body_storage": body_storage
#     }

from typing import Dict, List
from requests.auth import HTTPBasicAuth
import requests

from app.core.config import settings


def _get_auth():
    if not settings.CONFLUENCE_EMAIL or not settings.CONFLUENCE_API_TOKEN:
        raise ValueError("Confluence email or API token is missing in .env")

    return HTTPBasicAuth(settings.CONFLUENCE_EMAIL, settings.CONFLUENCE_API_TOKEN)


def _get_headers():
    return {
        "Accept": "application/json"
    }


def _build_full_url(links: Dict) -> str:
    webui = links.get("webui", "")
    base = links.get("base", "")

    if base and webui:
        return f"{base}{webui}"

    if webui.startswith("http://") or webui.startswith("https://"):
        return webui

    if webui.startswith("/wiki"):
        return f"{settings.CONFLUENCE_BASE_URL}{webui}"

    if webui.startswith("/"):
        return f"{settings.CONFLUENCE_BASE_URL}/wiki{webui}"

    return ""


def _build_api_url(relative_or_absolute_url: str) -> str:
    if not relative_or_absolute_url:
        return ""

    if relative_or_absolute_url.startswith("http://") or relative_or_absolute_url.startswith("https://"):
        return relative_or_absolute_url

    if relative_or_absolute_url.startswith("/wiki"):
        return f"{settings.CONFLUENCE_BASE_URL}{relative_or_absolute_url}"

    if relative_or_absolute_url.startswith("/rest"):
        return f"{settings.CONFLUENCE_BASE_URL}/wiki{relative_or_absolute_url}"

    if relative_or_absolute_url.startswith("/"):
        return f"{settings.CONFLUENCE_BASE_URL}{relative_or_absolute_url}"

    return f"{settings.CONFLUENCE_BASE_URL}/{relative_or_absolute_url}"


def get_pages_from_space(limit: int = 10) -> List[Dict]:
    if not settings.CONFLUENCE_BASE_URL:
        raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

    if not settings.CONFLUENCE_SPACE_KEY:
        raise ValueError("CONFLUENCE_SPACE_KEY is missing in .env")

    url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/search"
    cql = f'space="{settings.CONFLUENCE_SPACE_KEY}" and type=page'

    response = requests.get(
        url,
        auth=_get_auth(),
        headers=_get_headers(),
        params={
            "cql": cql,
            "limit": limit
        },
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(
            f"Confluence API error: {response.status_code} - {response.text}"
        )

    data = response.json()
    results = data.get("results", [])

    pages = []

    for item in results:
        title = item.get("title", "Untitled")
        page_id = item.get("id", "")
        links = item.get("_links", {})
        page_url = _build_full_url(links)

        pages.append(
            {
                "id": page_id,
                "title": title,
                "url": page_url
            }
        )

    return pages


def get_all_pages_from_space(limit: int = 25) -> List[Dict]:
    if not settings.CONFLUENCE_BASE_URL:
        raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

    if not settings.CONFLUENCE_SPACE_KEY:
        raise ValueError("CONFLUENCE_SPACE_KEY is missing in .env")

    cql = f'space="{settings.CONFLUENCE_SPACE_KEY}" and type=page'
    next_url = (
        f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/search"
        f"?cql={requests.utils.quote(cql)}&limit={limit}"
    )

    pages = []

    while next_url:
        response = requests.get(
            next_url,
            auth=_get_auth(),
            headers=_get_headers(),
            timeout=30
        )

        if response.status_code != 200:
            raise Exception(
                f"Confluence API error during bulk page fetch: {response.status_code} - {response.text}"
            )

        data = response.json()
        results = data.get("results", [])

        for item in results:
            title = item.get("title", "Untitled")
            page_id = item.get("id", "")
            links = item.get("_links", {})
            page_url = _build_full_url(links)

            pages.append(
                {
                    "id": page_id,
                    "title": title,
                    "url": page_url
                }
            )

        relative_next = data.get("_links", {}).get("next")
        next_url = _build_api_url(relative_next) if relative_next else None

    return pages


def get_page_by_id(page_id: str) -> Dict:
    if not settings.CONFLUENCE_BASE_URL:
        raise ValueError("CONFLUENCE_BASE_URL is missing in .env")

    url = f"{settings.CONFLUENCE_BASE_URL}/wiki/rest/api/content/{page_id}"

    response = requests.get(
        url,
        auth=_get_auth(),
        headers=_get_headers(),
        params={
            "expand": "body.storage,version,space"
        },
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(
            f"Confluence page fetch error: {response.status_code} - {response.text}"
        )

    data = response.json()

    title = data.get("title", "Untitled")
    page_id_value = data.get("id", "")
    links = data.get("_links", {})
    page_url = _build_full_url(links)

    body_storage = data.get("body", {}).get("storage", {}).get("value", "")
    version_number = data.get("version", {}).get("number", None)
    space_key = data.get("space", {}).get("key", "")

    return {
        "id": page_id_value,
        "title": title,
        "url": page_url,
        "space_key": space_key,
        "version": version_number,
        "body_storage": body_storage
    }