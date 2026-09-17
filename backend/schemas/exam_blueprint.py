from pydantic import BaseModel


class ExamBlueprintCreate(BaseModel):
    exam_id: int
    section_name: str
    num_questions: int
    marks_per_question: float
    negative_marks: float
    duration_minutes: int


class ExamBlueprintResponse(BaseModel):
    id: int
    exam_id: int
    section_name: str
    num_questions: int
    marks_per_question: float
    negative_marks: float
    duration_minutes: int

    class Config:
        from_attributes = True
        