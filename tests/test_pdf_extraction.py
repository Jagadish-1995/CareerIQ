from nlp.extraction.pdf_extractor import extract_text_from_pdf
from nlp.preprocessing.text_cleaner import clean_resume_text


PDF_PATH = "data/raw/resume.pdf"


raw_text = extract_text_from_pdf(PDF_PATH)

cleaned_text = clean_resume_text(raw_text)


print("=" * 60)
print("RAW TEXT")
print("=" * 60)

print(raw_text)

print("\n")

print("=" * 60)
print("CLEANED TEXT")
print("=" * 60)

print(cleaned_text)