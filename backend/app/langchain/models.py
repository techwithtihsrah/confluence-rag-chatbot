from functools import lru_cache

from langchain_groq import ChatGroq

from app.core.config import settings


DEFAULT_GROQ_MODEL = "llama-3.1-8b-instant"
DEFAULT_GROQ_TEMPERATURE = 0.0


@lru_cache(maxsize=1)
def get_chat_model() -> ChatGroq:
    if not settings.GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing in .env file")

    model_name = getattr(settings, "GROQ_MODEL_NAME", DEFAULT_GROQ_MODEL) or DEFAULT_GROQ_MODEL
    temperature_value = getattr(
        settings,
        "GROQ_TEMPERATURE",
        DEFAULT_GROQ_TEMPERATURE,
    )

    try:
        temperature = float(temperature_value)
    except (TypeError, ValueError):
        temperature = DEFAULT_GROQ_TEMPERATURE

    return ChatGroq(
        api_key=settings.GROQ_API_KEY,
        model=model_name,
        temperature=temperature,
        max_retries=2,
    )