from pydantic import BaseModel


class SectionQuality(BaseModel):
    quality: str
    feedback: str


class SectionQualityAnalysis(BaseModel):
    sections: dict[str, SectionQuality]