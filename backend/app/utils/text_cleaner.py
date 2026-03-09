# import re
# from bs4 import BeautifulSoup, NavigableString


# CODE_LABELS = {
#     "bash",
#     "sh",
#     "shell",
#     "python",
#     "json",
#     "yaml",
#     "yml",
#     "env",
#     "sql",
#     "code",
#     "javascript",
#     "typescript",
# }


# def clean_confluence_storage_html(storage_html: str) -> str:
#     if not storage_html:
#         return ""

#     soup = BeautifulSoup(storage_html, "html.parser")

#     for tag in soup(["script", "style"]):
#         tag.decompose()

#     for param in soup.find_all(lambda tag: tag.name == "ac:parameter"):
#         param.decompose()

#     for macro in soup.find_all(lambda tag: tag.name == "ac:structured-macro"):
#         macro_name = macro.attrs.get("ac:name", "")

#         if macro_name == "code":
#             plain_text_body = macro.find(lambda tag: tag.name == "ac:plain-text-body")
#             code_text = ""

#             if plain_text_body:
#                 code_text = plain_text_body.get_text()

#             replacement = soup.new_tag("pre")
#             replacement.string = f"\n{code_text.strip()}\n"
#             macro.replace_with(replacement)
#         else:
#             macro.unwrap()

#     for p in soup.find_all("p"):
#         text = p.get_text(strip=True).lower()

#         next_sibling = p.find_next_sibling()
#         if (
#             text in CODE_LABELS
#             and next_sibling
#             and getattr(next_sibling, "name", None) == "pre"
#         ):
#             p.decompose()

#     text = soup.get_text(separator="\n")

#     text = text.replace("\xa0", " ")
#     text = re.sub(r"\r", "\n", text)
#     text = re.sub(r"\n{3,}", "\n\n", text)
#     text = re.sub(r"[ \t]+", " ", text)

#     lines = [line.strip() for line in text.split("\n")]
#     lines = [line for line in lines if line]

#     return "\n".join(lines)

import re
from bs4 import BeautifulSoup


CODE_LABELS = {
    "bash",
    "sh",
    "shell",
    "python",
    "json",
    "yaml",
    "yml",
    "env",
    "sql",
    "code",
    "javascript",
    "typescript",
}


def clean_confluence_storage_html(storage_html: str) -> str:
    if not storage_html:
        return ""

    soup = BeautifulSoup(storage_html, "html.parser")

    for tag in soup(["script", "style"]):
        tag.decompose()

    for param in soup.find_all(lambda tag: tag.name == "ac:parameter"):
        param.decompose()

    for macro in soup.find_all(lambda tag: tag.name == "ac:structured-macro"):
        macro_name = macro.attrs.get("ac:name", "")

        if macro_name == "code":
            plain_text_body = macro.find(lambda tag: tag.name == "ac:plain-text-body")
            code_text = ""

            if plain_text_body:
                code_text = plain_text_body.get_text()

            replacement = soup.new_tag("pre")
            replacement.string = f"\n{code_text.strip()}\n"
            macro.replace_with(replacement)
        else:
            macro.unwrap()

    for p in soup.find_all("p"):
        text = p.get_text(strip=True).lower()

        next_sibling = p.find_next_sibling()
        if (
            text in CODE_LABELS
            and next_sibling
            and getattr(next_sibling, "name", None) == "pre"
        ):
            p.decompose()

    text = soup.get_text(separator="\n")

    text = text.replace("\xa0", " ")
    text = re.sub(r"\r", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)

    lines = [line.strip() for line in text.split("\n")]
    lines = [line for line in lines if line]

    return "\n".join(lines)