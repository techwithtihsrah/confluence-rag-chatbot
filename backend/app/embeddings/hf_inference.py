from typing import List

from huggingface_hub import InferenceClient
from langchain_core.embeddings import Embeddings

from app.core.config import settings


class HuggingFaceInferenceEmbeddings(Embeddings):
    def __init__(self, api_key: str, model_name: str):
        if not api_key:
            raise ValueError("HF_TOKEN is missing in .env")

        if not model_name:
            raise ValueError("HF_EMBEDDING_MODEL is missing in .env")

        self.client = InferenceClient(
            provider="hf-inference",
            api_key=api_key,
        )
        self.model_name = model_name

    def _embed_single_text(self, text: str) -> List[float]:
        result = self.client.feature_extraction(
            text,
            model=self.model_name,
        )

        if hasattr(result, "tolist"):
            result = result.tolist()

        if isinstance(result, list) and result and isinstance(result[0], (int, float)):
            return [float(x) for x in result]

        if (
            isinstance(result, list)
            and result
            and isinstance(result[0], list)
            and result[0]
            and isinstance(result[0][0], (int, float))
        ):
            return [float(x) for x in result[0]]

        raise ValueError("Unexpected embedding response format from Hugging Face Inference API")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self._embed_single_text(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        return self._embed_single_text(text)


def get_hf_inference_embeddings() -> HuggingFaceInferenceEmbeddings:
    return HuggingFaceInferenceEmbeddings(
        api_key=settings.HF_TOKEN,
        model_name=settings.HF_EMBEDDING_MODEL,
    )