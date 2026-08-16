from app.schemas.resume_analysis import SkillStatistics


def generate_resume_feedback(
    statistics: SkillStatistics,
    score: int,
    missing_sections: list[str]
) -> list[str]:
    """
    Generate improvement feedback based on resume score and skill coverage.
    """

    feedback = []

    if statistics.total_skills < 5:
        feedback.append(
            "Add more relevant technical skills to improve skill coverage."
        )

    if len(statistics.categories) < 2:
        feedback.append(
            "Add skills from more categories to improve skill diversity."
        )
    if "Experience" in missing_sections:
        feedback.append(
            "Consider adding an Experience section to highlight your professional experience."
    )

    if "Certifications" in missing_sections:
        feedback.append(
            "Consider adding a Certifications section if you have relevant certifications."
    )

    if score < 50:
        feedback.append(
            "Strengthen your resume with more relevant skills and broader technical coverage."
        )
    elif score < 75:
        feedback.append(
            "Your resume has a reasonable skill foundation, but there is room for improvement."
        )
    else:
        feedback.append(
            "Your resume shows good skill coverage and diversity."
        )

    return feedback