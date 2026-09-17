from pydantic import BaseModel


class PaperQuestionCreate(BaseModel):
    paper_id: int
    question_id: int
    question_number: int


class PaperQuestionResponse(BaseModel):
    id: int
    paper_id: int
    question_id: int
    question_number: int

    class Config:
        from_attributes = True