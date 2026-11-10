import re


SKILL_DATABASE = {
    "programming": [
        "python",
        "java",
        "c",
        "c++",
        "javascript"
    ],

    "data": [
        "sql",
        "excel",
        "power bi",
        "tableau",
        "pandas",
        "numpy"
    ],

    "machine_learning": [
        "machine learning",
        "scikit-learn",
        "random forest",
        "xgboost",
        "decision tree",
        "logistic regression",
        "linear regression"
    ],

    "deep_learning": [
        "tensorflow",
        "keras",
        "pytorch",
        "ann",
        "cnn",
        "rnn"
    ],

    "nlp": [
        "nlp",
        "natural language processing",
        "tokenization",
        "embeddings",
        "transformers",
        "rag"
    ],

    "genai": [
        "generative ai",
        "llm",
        "large language model",
        "prompt engineering",
        "ai agents"
    ],

    "backend": [
        "fastapi",
        "flask",
        "rest api",
        "api"
    ],

    "database": [
        "mysql",
        "postgresql",
        "mongodb"
    ],

    "cloud": [
        "aws",
        "azure",
        "gcp",
        "docker"
    ]
}


def extract_skills(text: str) -> dict:

    text = text.lower()

    detected_skills = {}

    for category, skills in SKILL_DATABASE.items():

        found = []

        for skill in skills:

            pattern = r"\b" + re.escape(skill) + r"\b"

            if re.search(pattern, text):
                found.append(skill)

        if found:
            detected_skills[category] = found

    return detected_skills