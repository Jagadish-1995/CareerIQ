from nlp.embeddings.embedding_engine import EmbeddingEngine


engine = EmbeddingEngine()


text = "I build machine learning models using Python."

embedding = engine.generate_embedding(text)


print("=" * 60)
print("EMBEDDING")
print("=" * 60)

print(embedding)

print("\nEmbedding shape:")

print(embedding.shape)