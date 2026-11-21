from sqlalchemy import Column, Integer, Float, ForeignKey
from backend.db.database import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id"),
        nullable=False
    )

    total_questions = Column(Integer, nullable=False)

    attempted_questions = Column(Integer, nullable=False)

    correct_answers = Column(Integer, nullable=False)

    wrong_answers = Column(Integer, nullable=False)

    unanswered_questions = Column(Integer, nullable=False)

    score = Column(Float, nullable=False)