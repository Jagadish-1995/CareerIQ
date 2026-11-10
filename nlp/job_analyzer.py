from nlp.preprocessing.text_cleaner import clean_resume_text
from nlp.extraction.skill_extractor import extract_skills


class JobDescriptionAnalyzer:

    def analyze(self, job_description: str) -> dict:

        cleaned_text = clean_resume_text(
            job_description
        )

        skills = extract_skills(
            cleaned_text
        )

        return {
            "cleaned_text": cleaned_text,
            "skills": skills
        }