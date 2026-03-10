from langchain_core.output_parsers import StrOutputParser


def get_text_output_parser() -> StrOutputParser:
    return StrOutputParser()