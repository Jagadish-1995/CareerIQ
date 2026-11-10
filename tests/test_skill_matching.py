from pathlib import Path

from nlp.resume_profile import (
    ResumeProfileBuilder
)

from nlp.job_analyzer import (
    JobDescriptionAnalyzer
)

from nlp.skill_matcher import (
    calculate_skill_match
)


resume_path = (
    "data/raw/resume.pdf"
)

job_path = Path(
    "data/raw/sample_job_description.txt"
)


resume_builder = (
    ResumeProfileBuilder()
)

resume_profile = (
    resume_builder.build(
        resume_path
    )
)


job_text = job_path.read_text(
    encoding="utf-8"
)

job_analyzer = (
    JobDescriptionAnalyzer()
)

job_profile = (
    job_analyzer.analyze(
        job_text
    )
)


result = calculate_skill_match(
    resume_profile["skills"],
    job_profile["skills"]
)


print("\n" + "=" * 60)

print("CAREERIQ JOB MATCH")

print("=" * 60)

print(
    f"\nSkill Match: "
    f"{result['score']}%"
)


print("\nMatched Skills:")

for skill in result[
    "matched_skills"
]:

    print(f"  ✓ {skill}")


print("\nMissing Skills:")

for skill in result[
    "missing_skills"
]:

    print(f"  ✗ {skill}")