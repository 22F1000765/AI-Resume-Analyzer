from pydantic import BaseModel
from app.schemas.section_content import SectionContentAnalysis
from app.schemas.section_quality import SectionQualityAnalysis


class SkillStatistics(BaseModel):
    total_skills: int
    categories: dict[str, int]

class SectionStatistics(BaseModel):
    present: list[str]
    missing: list[str]

class ResumeAnalysis(BaseModel):
    skills: list[str]
    categorized_skills: dict[str, list[str]]
    statistics: SkillStatistics
    score: int
    feedback: list[str]
    sections: SectionStatistics
    section_content: SectionContentAnalysis
    section_quality: SectionQualityAnalysis
