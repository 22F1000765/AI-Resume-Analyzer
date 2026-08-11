from app.services.skill_extractor import extract_skills
from app.services.skill_categorizer import categorize_skills
from app.services.skill_statistics import generate_skill_statistics


def analyze_resume(text: str) -> dict:
    """
    Analyze resume text and return extracted skill information.
    """

    skills = extract_skills(text)

    categorized = categorize_skills(skills)

    statistics = generate_skill_statistics(categorized)

    return {
        "skills": skills,
        "categorized_skills": categorized,
        "statistics": statistics,
    }