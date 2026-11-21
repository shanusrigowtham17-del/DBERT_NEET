from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.db.database import get_db
from backend.models.exam_blueprint import ExamBlueprint
from backend.schemas.exam_blueprint import (
    ExamBlueprintCreate,
    ExamBlueprintResponse
)
from backend.services.auth import get_current_user, require_admin


router = APIRouter(
    prefix="/api/exam-blueprints",
    tags=["Exam Blueprints"]
)


# Get all exam blueprints
@router.get(
    "/",
    response_model=list[ExamBlueprintResponse]
)
def get_exam_blueprints(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    blueprints = db.query(ExamBlueprint).all()

    return blueprints


# Create a new exam blueprint
@router.post(
    "/",
    response_model=ExamBlueprintResponse,
    status_code=status.HTTP_201_CREATED
)
def create_exam_blueprint(
    blueprint_data: ExamBlueprintCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    new_blueprint = ExamBlueprint(
        exam_id=blueprint_data.exam_id,
        section_name=blueprint_data.section_name,
        num_questions=blueprint_data.num_questions,
        marks_per_question=blueprint_data.marks_per_question,
        negative_marks=blueprint_data.negative_marks,
        duration_minutes=blueprint_data.duration_minutes
    )

    db.add(new_blueprint)
    db.commit()
    db.refresh(new_blueprint)

    return new_blueprint