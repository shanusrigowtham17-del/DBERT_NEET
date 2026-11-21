from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from backend.db.database import Base


class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    paper_id = Column(
        Integer,
        ForeignKey("papers.id"),
        nullable=False
    )

    started_at = Column(
        DateTime,
        nullable=False
    )

    duration_seconds = Column(
        Integer,
        nullable=False
    )

    submitted_at = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String,
        default="in_progress",
        nullable=False
    )