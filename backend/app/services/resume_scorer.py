from app.schemas.resume_analysis import SkillStatistics


def calculate_resume_score(statistics: SkillStatistics) -> int:
    """
    Calculate a simple resume score based on extracted skills.

    Score components:
    - Up to 60 points for total skills
    - Up to 40 points for category diversity

    Maximum score: 100
    """

    skill_score = min(statistics.total_skills * 5, 60)

    category_score = min(len(statistics.categories) * 10, 40)

    return skill_score + category_score