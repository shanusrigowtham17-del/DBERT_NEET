from pydantic import BaseModel


class QuestionCreate(BaseModel):
    exam_id: int
    topic_id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    correct_option: str
    difficulty: str
    source: str
    explanation: str | None = None


class QuestionResponse(BaseModel):
    id: int
    exam_id: int
    topic_id: int
    text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str
    difficulty: str
    source: str
    explanation: str | None = None

    class Config:
        from_attributes = True


class QuestionAdminResponse(QuestionResponse):
    correct_option: str