from nlp.extraction.pdf_extractor import extract_text_from_pdf
from nlp.preprocessing.text_cleaner import clean_resume_text
from nlp.extraction.section_extractor import detect_sections
from nlp.extraction.skill_extractor import extract_skills


class ResumeProfileBuilder:

    def build(self, pdf_path: str) -> dict:

        raw_text = extract_text_from_pdf(pdf_path)

        cleaned_text = clean_resume_text(raw_text)

        sections = detect_sections(cleaned_text)

        skills = extract_skills(cleaned_text)

        profile = {
            "raw_text": cleaned_text,
            "sections": sections,
            "skills": skills
        }

        return profile