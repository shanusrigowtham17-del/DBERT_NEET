from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.paper_questions import PaperQuestion
from backend.schemas.paper_question import (
    PaperQuestionCreate,
    PaperQuestionResponse
)
from backend.services.auth import get_current_user


router = APIRouter(
    prefix="/api/paper-questions",
    tags=["Paper Questions"]
)


# Add a question to a paper
@router.post(
    "/",
    response_model=PaperQuestionResponse,
    status_code=201
)
def add_question_to_paper(
    paper_question_data: PaperQuestionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    new_paper_question = PaperQuestion(
        paper_id=paper_question_data.paper_id,
        question_id=paper_question_data.question_id,
        question_number=paper_question_data.question_number
    )

    db.add(new_paper_question)
    db.commit()
    db.refresh(new_paper_question)

    return new_paper_question


# Get questions belonging to a paper
@router.get(
    "/{paper_id}",
    response_model=list[PaperQuestionResponse]
)
def get_paper_questions(
    paper_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    paper_questions = (
        db.query(PaperQuestion)
        .filter(PaperQuestion.paper_id == paper_id)
        .order_by(PaperQuestion.question_number)
        .all()
    )

    return paper_questions