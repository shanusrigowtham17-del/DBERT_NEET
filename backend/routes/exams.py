from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.exam import Exam
from backend.schemas.exam import ExamCreate, ExamResponse
from backend.services.auth import get_current_user, require_admin


router = APIRouter(
    prefix="/api/exams",
    tags=["Exams"]
)


@router.get(
    "/",
    response_model=list[ExamResponse]
)
def get_exams(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    exams = db.query(Exam).all()

    return exams


@router.post(
    "/",
    response_model=ExamResponse,
    status_code=status.HTTP_201_CREATED
)
def create_exam(
    exam_data: ExamCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    new_exam = Exam(
        name=exam_data.name,
        category=exam_data.category,
        description=exam_data.description
    )

    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)

    return new_exam