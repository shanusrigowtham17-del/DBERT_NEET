from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.attempt import Attempt
from backend.models.paper import Paper
from backend.models.result import Result
from backend.schemas.attempt import AttemptCreate, AttemptResponse
from backend.services.auth import get_current_user
from backend.services.scoring import calculate_attempt_score
from backend.services.session_manager import ensure_attempt_active

router = APIRouter(
    prefix="/api/attempts",
    tags=["Attempts"]
)


@router.post(
    "/",
    response_model=AttemptResponse,
    status_code=status.HTTP_201_CREATED
)
def start_attempt(
    attempt_data: AttemptCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Check that the paper exists
    paper = (
        db.query(Paper)
        .filter(Paper.id == attempt_data.paper_id)
        .first()
    )

    if not paper:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Paper not found"
        )

    # Create a new attempt for the logged-in user
    new_attempt = Attempt(
    user_id=current_user.id,
    paper_id=attempt_data.paper_id,
    started_at=datetime.now(timezone.utc),
    duration_seconds=paper.duration_minutes * 60,
    status="in_progress"
)

    db.add(new_attempt)
    db.commit()
    db.refresh(new_attempt)

    return new_attempt


@router.get(
    "/{attempt_id}",
    response_model=AttemptResponse
)
def get_attempt(
    attempt_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Find the attempt belonging to the logged-in user
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

    return attempt


@router.post(
    "/{attempt_id}/submit",
    response_model=AttemptResponse
)
def submit_attempt(
    attempt_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Find the attempt belonging to the logged-in user
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

    # Validate that the attempt is active and has not expired
    ensure_attempt_active(attempt)

    # Calculate attempt score and statistics
    score_data = calculate_attempt_score(db, attempt)

    # Prevent duplicate Result creation if a result already exists for this attempt
    existing_result = (
        db.query(Result)
        .filter(Result.attempt_id == attempt.id)
        .first()
    )

    if not existing_result:
        result = Result(
            attempt_id=attempt.id,
            total_questions=score_data["total_questions"],
            attempted_questions=score_data["attempted_questions"],
            correct_answers=score_data["correct_answers"],
            wrong_answers=score_data["wrong_answers"],
            unanswered_questions=score_data["unanswered_questions"],
            score=score_data["score"]
        )
        db.add(result)

    # Mark the attempt as submitted
    attempt.status = "submitted"
    attempt.submitted_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(attempt)

    return attempt