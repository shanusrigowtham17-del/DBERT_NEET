from pydantic import BaseModel


class PaperCreate(BaseModel):
    exam_id: int
    title: str
    total_questions: int
    duration_minutes: int


class PaperResponse(BaseModel):
    id: int
    exam_id: int
    title: str
    total_questions: int
    duration_minutes: int

    class Config:
        from_attributes = True