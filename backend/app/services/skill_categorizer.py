from app.data.skill_categories import SKILL_CATEGORIES


def categorize_skills(skills: list[str]) -> dict[str, list[str]]:
    categorized = {}

    for skill in skills:
        category = SKILL_CATEGORIES.get(skill, "Other")

        categorized.setdefault(category, []).append(skill)

    return categorized