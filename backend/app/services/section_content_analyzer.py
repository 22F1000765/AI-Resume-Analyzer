from app.schemas.section_content import (
    SectionContent,
    SectionContentAnalysis,
)


def analyze_section_content(
    sections: dict[str, list[str]],
) -> SectionContentAnalysis:
    """
    Analyze the amount of content present in each resume section.
    """

    section_analysis = {}

    for section, content in sections.items():
        content_lines = len(content)

        section_analysis[section] = SectionContent(
            has_content=content_lines > 0,
            content_lines=content_lines,
        )

    return SectionContentAnalysis(
        sections=section_analysis,
    )