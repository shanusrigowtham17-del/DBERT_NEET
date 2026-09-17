from pydantic import BaseModel, Field


class PaperBuildRequest(BaseModel):
    exam_id: int
    question_count: int = Field(gt=0, description="Requested number of questions (must be greater than 0)")
    title: str | None = None

