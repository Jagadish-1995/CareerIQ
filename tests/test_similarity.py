from nlp.embeddings.embedding_engine import EmbeddingEngine
from nlp.embeddings.similarity import calculate_similarity


engine = EmbeddingEngine()


text_a = (
    "I build machine learning models "
    "using Python."
)

text_b = (
    "I have experience developing "
    "predictive models with Python."
)

text_c = (
    "I enjoy watching cricket matches "
    "on weekends."
)


embedding_a = engine.generate_embedding(text_a)

embedding_b = engine.generate_embedding(text_b)

embedding_c = engine.generate_embedding(text_c)


similarity_ab = calculate_similarity(
    embedding_a,
    embedding_b
)

similarity_ac = calculate_similarity(
    embedding_a,
    embedding_c
)


print("=" * 60)

print("A vs B")

print(similarity_ab)

print("\nA vs C")

print(similarity_ac)