from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.attempt import Attempt
from backend.models.attempt_answer import AttemptAnswer
from backend.schemas.attempt_answer import (
    AttemptAnswerCreate,
    AttemptAnswerResponse
)
from backend.services.auth import get_current_user
from backend.services.session_manager import ensure_attempt_active

router = APIRouter(
    prefix="/api/attempt-answers",
    tags=["Attempt Answers"]
)


@router.post(
    "/",
    response_model=AttemptAnswerResponse
)
def save_answer(
    answer_data: AttemptAnswerCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Check that the attempt belongs to the logged-in user
    attempt = (
        db.query(Attempt)
        .filter(
            Attempt.id == answer_data.attempt_id,
            Attempt.user_id == current_user.id
        )
        .first()
    )

    if not attempt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attempt not found"
        )

    # Validate that the attempt is active and has not expired
    ensure_attempt_active(attempt)

    # Check whether an answer already exists
    existing_answer = (
        db.query(AttemptAnswer)
        .filter(
            AttemptAnswer.attempt_id == answer_data.attempt_id,
            AttemptAnswer.question_id == answer_data.question_id
        )
        .first()
    )

    # If answer already exists, update it
    if existing_answer:
        existing_answer.selected_option = answer_data.selected_option

        db.commit()
        db.refresh(existing_answer)

        return existing_answer

    # Otherwise create a new answer
    new_answer = AttemptAnswer(
        attempt_id=answer_data.attempt_id,
        question_id=answer_data.question_id,
        selected_option=answer_data.selected_option
    )

    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)

    return new_answer


@router.get(
    "/{attempt_id}",
    response_model=list[AttemptAnswerResponse]
)
def get_attempt_answers(
    attempt_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Verify that the attempt belongs to the logged-in user
    attempt = (
        db.query(Attempt)
        .filter(
            Attempt.id == attempt_id,
            Attempt.user_id == current_user.id
        )
        .first()
    )

    if not attempt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attempt not found"
        )

    answers = (
        db.query(AttemptAnswer)
        .filter(AttemptAnswer.attempt_id == attempt_id)
        .all()
    )

    return answers