from sentence_transformers import SentenceTransformer


class EmbeddingEngine:

    def __init__(
        self,
        model_name="all-MiniLM-L6-v2"
    ):
        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text: str):

        if not text.strip():
            raise ValueError("Text cannot be empty.")

        return self.model.encode(text)

    def generate_embeddings(self, texts: list[str]):

        if not texts:
            raise ValueError("Text list cannot be empty.")

        return self.model.encode(texts)