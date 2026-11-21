from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.topic import Topic
from backend.schemas.topic import TopicResponse
from backend.services.auth import get_current_user


router = APIRouter(
    prefix="/api/topics",
    tags=["Topics"]
)


@router.get(
    "/{exam_id}",
    response_model=list[TopicResponse]
)
def get_topics(
    exam_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    topics = (
        db.query(Topic)
        .filter(Topic.exam_id == exam_id)
        .all()
    )

    return topics