from pydantic import BaseModel


class TopicCreate(BaseModel):
    exam_id: int
    name: str


class TopicResponse(BaseModel):
    id: int
    exam_id: int
    name: str

    class Config:
        from_attributes = True