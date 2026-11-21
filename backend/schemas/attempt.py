from pydantic import BaseModel, field_serializer
from datetime import datetime, timezone


class AttemptCreate(BaseModel):
    paper_id: int


class AttemptResponse(BaseModel):
    id: int
    user_id: int
    paper_id: int
    started_at: datetime
    duration_seconds: int
    submitted_at: datetime | None = None
    status: str

    @field_serializer("started_at", "submitted_at", when_used="json")
    def serialize_datetime(self, dt: datetime | None) -> str | None:
        if dt is None:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.isoformat()

    class Config:
        from_attributes = True