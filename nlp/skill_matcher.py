def flatten_skills(skill_dict: dict) -> set:

    skills = set()

    for skill_list in skill_dict.values():

        for skill in skill_list:

            skills.add(skill.lower())

    return skills


def calculate_skill_match(
    resume_skills: dict,
    job_skills: dict
) -> dict:

    resume_set = flatten_skills(
        resume_skills
    )

    job_set = flatten_skills(
        job_skills
    )

    matched = resume_set.intersection(
        job_set
    )

    missing = job_set - resume_set

    if job_set:

        score = (
            len(matched) /
            len(job_set)
        ) * 100

    else:

        score = 0

    return {
        "score": round(score, 2),
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }