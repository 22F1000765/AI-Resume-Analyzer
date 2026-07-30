from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    filename: str
    file_path: str

    model_config = {
        "from_attributes": True
    }