from pydantic import BaseModel


class ResultResponse(BaseModel):
    id: int
    attempt_id: int
    total_questions: int
    attempted_questions: int
    correct_answers: int
    wrong_answers: int
    unanswered_questions: int
    score: float

    class Config:
        from_attributes = True