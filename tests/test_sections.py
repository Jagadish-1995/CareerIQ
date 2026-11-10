from nlp.extraction.pdf_extractor import extract_text_from_pdf
from nlp.preprocessing.text_cleaner import clean_resume_text
from nlp.extraction.section_extractor import detect_sections


PDF_PATH = "data/raw/resume.pdf"


raw_text = extract_text_from_pdf(PDF_PATH)

cleaned_text = clean_resume_text(raw_text)

sections = detect_sections(cleaned_text)


for section_name, content in sections.items():

    print("\n" + "=" * 60)

    print(section_name.upper())

    print("=" * 60)

    print(content)