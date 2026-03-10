from functools import lru_cache

from app.langchain.models import get_chat_model
from app.langchain.parsers import get_text_output_parser
from app.langchain.prompts import get_answer_prompt, get_query_rewrite_prompt


@lru_cache(maxsize=1)
def build_query_rewrite_chain():
    prompt = get_query_rewrite_prompt()
    model = get_chat_model()
    parser = get_text_output_parser()
    return prompt | model | parser


@lru_cache(maxsize=1)
def build_answer_chain():
    prompt = get_answer_prompt()
    model = get_chat_model()
    parser = get_text_output_parser()
    return prompt | model | parser