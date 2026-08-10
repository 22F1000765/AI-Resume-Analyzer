def generate_skill_statistics(categorized_skills: dict[str, list[str]]) -> dict:
    """
    Generate summary statistics from categorized skills.
    """

    category_counts = {}

    total = 0

    for category, skills in categorized_skills.items():
        category_counts[category] = len(skills)
        total += len(skills)

    return {
        "total_skills": total,
        "categories": category_counts,
    }