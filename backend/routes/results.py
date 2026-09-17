from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.attempt import Attempt
from backend.models.result import Result
from backend.schemas.result import ResultResponse
from backend.services.auth import get_current_user

router = APIRouter(
    prefix="/api/results",
    tags=["Results"]
)


@router.get(
    "/{attempt_id}",
    response_model=ResultResponse
)
def get_result(
    attempt_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    # Verify that the attempt exists and belongs to the authenticated user
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
            detail="Result not found"
        )

    # Find the result associated with the attempt
    result = (
        db.query(Result)
        .filter(Result.attempt_id == attempt_id)
        .first()
    )

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Result not found"
        )

    return result

