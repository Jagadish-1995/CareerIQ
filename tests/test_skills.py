from nlp.extraction.pdf_extractor import extract_text_from_pdf
from nlp.preprocessing.text_cleaner import clean_resume_text
from nlp.extraction.skill_extractor import extract_skills


PDF_PATH = "data/raw/resume.pdf"


raw_text = extract_text_from_pdf(PDF_PATH)

cleaned_text = clean_resume_text(raw_text)

skills = extract_skills(cleaned_text)


print("\n" + "=" * 60)
print("DETECTED SKILLS")
print("=" * 60)


for category, skill_list in skills.items():

    print(f"\n{category.upper()}")

    for skill in skill_list:
        print(f"  ✓ {skill}")