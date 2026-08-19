from app.schemas.section_content import SectionContentAnalysis
from app.schemas.section_quality import (
    SectionQuality,
    SectionQualityAnalysis,
)


def analyze_section_quality(
    section_content: SectionContentAnalysis,
) -> SectionQualityAnalysis:
    """
    Evaluate basic content quality for each resume section.
    """

    quality_analysis = {}

    for section, content in section_content.sections.items():

        if section == "Unknown":
            continue

        if not content.has_content:
            quality = "Needs Improvement"
            feedback = "This section does not contain any content."

        elif content.content_lines < 3:
            quality = "Needs Improvement"
            feedback = "This section contains very little content."

        elif content.content_lines < 6:
            quality = "Fair"
            feedback = "This section contains a moderate amount of content."

        else:
            quality = "Good"
            feedback = "This section contains sufficient content."

        quality_analysis[section] = SectionQuality(
            quality=quality,
            feedback=feedback,
        )

    return SectionQualityAnalysis(
        sections=quality_analysis,
    )