from app.schemas.resume_analysis import SkillStatistics
def generate_skill_statistics(categorized_skills: dict[str, list[str]]) -> SkillStatistics:
    """
    Generate summary statistics from categorized skills.
    """

    category_counts = {}

    total = 0

    for category, skills in categorized_skills.items():
        category_counts[category] = len(skills)
        total += len(skills)
        
    return SkillStatistics(
    total_skills=total,
    categories=category_counts,
)