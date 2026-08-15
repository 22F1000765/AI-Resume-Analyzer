from app.services.skill_extractor import extract_skills
from app.services.skill_categorizer import categorize_skills
from app.services.skill_statistics import generate_skill_statistics

from app.schemas.resume_analysis import ResumeAnalysis

from app.services.resume_scorer import calculate_resume_score

from app.services.resume_feedback import generate_resume_feedback


def analyze_resume(text: str) -> ResumeAnalysis:
    """
    Analyze resume text and return extracted skill information.
    """

    skills = extract_skills(text)

    categorized = categorize_skills(skills)

    statistics = generate_skill_statistics(categorized)

    score = calculate_resume_score(statistics)

    feedback = generate_resume_feedback(
    statistics,
    score,
    )

    return ResumeAnalysis (
        skills=skills,
        categorized_skills=categorized,
        statistics=statistics,
        score=score,
        feedback=feedback
        )
        