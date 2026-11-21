from datetime import datetime, timezone, timedelta

from fastapi import HTTPException, status
from backend.models.attempt import Attempt


def get_expiry_time(attempt: Attempt) -> datetime:
    """
    Calculate and return the expiry datetime for an attempt.
    Treats a naive datetime as UTC and adds duration_seconds.
    """
    started_at = attempt.started_at
    if started_at.tzinfo is None or started_at.tzinfo.utcoffset(started_at) is None:
        started_at = started_at.replace(tzinfo=timezone.utc)
    else:
        started_at = started_at.astimezone(timezone.utc)

    return started_at + timedelta(seconds=attempt.duration_seconds)


def is_attempt_expired(attempt: Attempt) -> bool:
    """
    Compare the calculated expiry time with the current UTC time.
    Returns True if the attempt has expired, otherwise False.
    """
    return datetime.now(timezone.utc) >= get_expiry_time(attempt)


def get_remaining_seconds(attempt: Attempt) -> int:
    """
    Calculate how many seconds remain for an attempt.
    Returns an integer and never returns a negative value (minimum 0).
    """
    remaining = (get_expiry_time(attempt) - datetime.now(timezone.utc)).total_seconds()
    return max(0, int(remaining))


def ensure_attempt_active(attempt: Attempt) -> None:
    """
    Validate that an attempt is active and not expired.
    Raises HTTP 400 if the attempt is not in progress or has expired.
    Otherwise does nothing.
    """
    if attempt.status != "in_progress":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Attempt is not active"
        )

    if is_attempt_expired(attempt):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Attempt time has expired"
        )

