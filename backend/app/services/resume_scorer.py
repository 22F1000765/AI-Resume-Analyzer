from app.schemas.resume_analysis import SkillStatistics,SectionStatistics
from app.services.section_analyzer import EXPECTED_SECTIONS


def calculate_resume_score(statistics: SkillStatistics,
                           section_statistics: SectionStatistics,) -> int:
    """
    Calculate a simple resume score based on  skills, skill diversity, and section coverage.

    Score components:
    - Up to 50 points for total skills
    - Up to 30 points for category diversity
    - Up to 20 points for section coverage

    Maximum score: 100
    """

    skill_score = min(statistics.total_skills * 5, 50)

    category_score = min(len(statistics.categories) * 10, 30)

    section_score = round(
        len(section_statistics.present)
        / len(EXPECTED_SECTIONS)
        * 20
    )

    return skill_score + category_score +  section_score