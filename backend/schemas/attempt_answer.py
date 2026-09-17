from pydantic import BaseModel


class AttemptAnswerCreate(BaseModel):
    attempt_id: int
    question_id: int
    selected_option: str | None = None


class AttemptAnswerResponse(BaseModel):
    id: int
    attempt_id: int
    question_id: int
    selected_option: str | None = None

    class Config:
        from_attributes = True