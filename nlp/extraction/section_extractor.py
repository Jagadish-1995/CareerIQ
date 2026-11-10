import re


SECTION_NAMES = [
    "summary",
    "objective",
    "education",
    "skills",
    "technical skills",
    "experience",
    "work experience",
    "projects",
    "certifications",
    "achievements",
    "internships",
    "publications"
]


def detect_sections(text: str) -> dict:

    sections = {}

    lines = text.splitlines()

    current_section = None
    current_content = []

    for line in lines:

        normalized = line.strip().lower()

        if normalized in SECTION_NAMES:

            if current_section:
                sections[current_section] = "\n".join(
                    current_content
                ).strip()

            current_section = normalized
            current_content = []

        elif current_section:
            current_content.append(line)

    if current_section:
        sections[current_section] = "\n".join(
            current_content
        ).strip()

    return sections