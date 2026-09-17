from sqlalchemy import Column, Integer, Float, String, ForeignKey
from backend.db.database import Base


class ExamBlueprint(Base):
    __tablename__ = "exam_blueprints"

    id = Column(Integer, primary_key=True, index=True)

    exam_id = Column(
        Integer,
        ForeignKey("exams.id"),
        nullable=False
    )

    section_name = Column(
        String,
        nullable=False
    )

    num_questions = Column(
        Integer,
        nullable=False
    )

    marks_per_question = Column(
        Float,
        nullable=False
    )

    negative_marks = Column(
        Float,
        nullable=False
    )

    duration_minutes = Column(
        Integer,
        nullable=False
    )