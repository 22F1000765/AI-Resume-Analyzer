from app.schemas.resume_analysis import SectionStatistics


EXPECTED_SECTIONS = [
    "Summary",
    "Education",
    "Experience",
    "Projects",
    "Skills",
    "Certifications",
    "Achievements",
]


def analyze_sections(
    sections: dict[str, list[str]],
) -> SectionStatistics:
    """
    Analyze resume sections and identify present and missing sections.
    """

    present = []
    missing = []

    for section in EXPECTED_SECTIONS:
        if section in sections:
            present.append(section)
        else:
            missing.append(section)

    return SectionStatistics(
        present=present,
        missing=missing,
    )