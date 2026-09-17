from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.paper import Paper
from backend.schemas.paper import PaperCreate, PaperResponse
from backend.schemas.paper_builder import PaperBuildRequest
from backend.services.auth import get_current_user, require_admin
from backend.services.paper_builder import build_paper


router = APIRouter(
    prefix="/api/papers",
    tags=["Papers"]
)


# Get papers for an exam
@router.get(
    "/{exam_id}",
    response_model=list[PaperResponse]
)
def get_papers(
    exam_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    papers = (
        db.query(Paper)
        .filter(Paper.exam_id == exam_id)
        .all()
    )

    return papers


# Create a new paper
@router.post(
    "/",
    response_model=PaperResponse,
    status_code=status.HTTP_201_CREATED
)
def create_paper(
    paper_data: PaperCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    new_paper = Paper(
        exam_id=paper_data.exam_id,
        title=paper_data.title,
        total_questions=paper_data.total_questions,
        duration_minutes=paper_data.duration_minutes
    )

    db.add(new_paper)
    db.commit()
    db.refresh(new_paper)

    return new_paper


# Build a paper using existing database questions
@router.post(
    "/build",
    response_model=PaperResponse,
    status_code=status.HTTP_201_CREATED
)
def build_paper_route(
    build_data: PaperBuildRequest,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    paper = build_paper(
        db=db,
        exam_id=build_data.exam_id,
        question_count=build_data.question_count,
        title=build_data.title
    )

    return paper