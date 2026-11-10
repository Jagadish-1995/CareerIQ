from nlp.resume_profile import ResumeProfileBuilder


PDF_PATH = "data/raw/resume.pdf"


builder = ResumeProfileBuilder()

profile = builder.build(PDF_PATH)


print("=" * 60)

print("RESUME PROFILE")

print("=" * 60)


print("\nSECTIONS")

for section in profile["sections"]:
    print(f"✓ {section}")


print("\nSKILLS")

for category, skills in profile["skills"].items():

    print(f"\n{category.upper()}")

    for skill in skills:
        print(f"  ✓ {skill}")