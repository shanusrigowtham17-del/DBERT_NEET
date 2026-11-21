from sqlalchemy import Column, Integer, String, Text, ForeignKey
from backend.db.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    exam_id = Column(
        Integer,
        ForeignKey("exams.id"),
        nullable=False
    )

    topic_id = Column(
        Integer,
        ForeignKey("topics.id"),
        nullable=False
    )

    text = Column(
        Text,
        nullable=False
    )

    option_a = Column(
        Text,
        nullable=False
    )

    option_b = Column(
        Text,
        nullable=False
    )

    option_c = Column(
        Text,
        nullable=False
    )

    option_d = Column(
        Text,
        nullable=False
    )

    correct_option = Column(
        String(1),
        nullable=False
    )

    difficulty = Column(
        String,
        nullable=False
    )

    source = Column(
        String,
        nullable=False
    )

    explanation = Column(
        Text,
        nullable=True
    )