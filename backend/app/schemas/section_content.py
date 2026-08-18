from pydantic import BaseModel


class SectionContent(BaseModel):
    has_content: bool
    content_lines: int


class SectionContentAnalysis(BaseModel):
    sections: dict[str, SectionContent]