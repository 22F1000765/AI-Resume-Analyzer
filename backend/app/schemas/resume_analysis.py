from pydantic import BaseModel


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
