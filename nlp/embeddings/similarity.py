from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
    embedding_a,
    embedding_b
) -> float:

    score = cosine_similarity(
        [embedding_a],
        [embedding_b]
    )[0][0]

    return float(score)