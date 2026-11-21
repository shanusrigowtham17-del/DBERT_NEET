from sqlalchemy import Column, Integer, String, ForeignKey
from backend.db.database import Base


class Paper(Base):
    __tablename__ = "papers"

    id = Column(Integer, primary_key=True, index=True)

    exam_id = Column(
        Integer,
        ForeignKey("exams.id"),
        nullable=False
    )

    title = Column(String, nullable=False)

    total_questions = Column(Integer, nullable=False)

    duration_minutes = Column(Integer, nullable=False)