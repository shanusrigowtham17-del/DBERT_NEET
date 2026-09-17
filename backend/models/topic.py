from sqlalchemy import Column, Integer, String, ForeignKey
from backend.db.database import Base


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)

    exam_id = Column(
        Integer,
        ForeignKey("exams.id"),
        nullable=False
    )

    name = Column(
        String,
        nullable=False
    )