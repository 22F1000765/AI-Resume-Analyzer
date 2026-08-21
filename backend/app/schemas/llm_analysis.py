from pydantic import BaseModel


class LLMResumeInsights(BaseModel):
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]
    overall_assessment: str