from pathlib import Path

from nlp.job_analyzer import (
    JobDescriptionAnalyzer
)


job_path = Path(
    "data/raw/sample_job_description.txt"
)

job_text = job_path.read_text(
    encoding="utf-8"
)


analyzer = JobDescriptionAnalyzer()

result = analyzer.analyze(
    job_text
)


print("=" * 60)

print("JOB DESCRIPTION SKILLS")

print("=" * 60)


for category, skills in result["skills"].items():

    print(f"\n{category.upper()}")

    for skill in skills:

        print(f"  ✓ {skill}")