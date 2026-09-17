from pydantic import BaseModel


class ExamCreate(BaseModel):
    name: str
    category: str
    description: str | None = None


class ExamResponse(BaseModel):
    id: int
    name: str
    category: str
    description: str | None = None

    class Config:
        from_attributes = True