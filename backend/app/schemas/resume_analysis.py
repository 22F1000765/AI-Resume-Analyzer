from pydantic import BaseModel


class SkillStatistics(BaseModel):
    total_skills: int
    categories: dict[str, int]


class ResumeAnalysis(BaseModel):
    skills: list[str]
    categorized_skills: dict[str, list[str]]
    statistics: SkillStatistics