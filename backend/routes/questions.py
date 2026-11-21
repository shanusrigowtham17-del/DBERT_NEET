from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.question import Question
from backend.schemas.question import (
    QuestionCreate,
    QuestionResponse,
    QuestionAdminResponse
)
from backend.services.auth import get_current_user, require_admin


router = APIRouter(
    prefix="/api/questions",
    tags=["Questions"]
)


@router.get(
    "/",
    response_model=list[QuestionAdminResponse]
)
def get_all_questions(
    exam_id: int | None = None,
    topic_id: int | None = None,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    query = db.query(Question)
    if exam_id is not None:
        query = query.filter(Question.exam_id == exam_id)
    if topic_id is not None:
        query = query.filter(Question.topic_id == topic_id)
    return query.all()


@router.post(
    "/",
    response_model=QuestionAdminResponse,
    status_code=status.HTTP_201_CREATED
)
def create_question(
    question_data: QuestionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    new_question = Question(
        exam_id=question_data.exam_id,
        topic_id=question_data.topic_id,
        text=question_data.text,
        option_a=question_data.option_a,
        option_b=question_data.option_b,
        option_c=question_data.option_c,
        option_d=question_data.option_d,
        correct_option=question_data.correct_option,
        difficulty=question_data.difficulty,
        source=question_data.source,
        explanation=question_data.explanation
    )
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question


@router.get(
    "/{exam_id}",
    response_model=list[QuestionResponse]
)
def get_questions(
    exam_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    questions = (
        db.query(Question)
        .filter(Question.exam_id == exam_id)
        .all()
    )

    return questions