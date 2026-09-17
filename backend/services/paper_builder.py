from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.models.exam import Exam
from backend.models.exam_blueprint import ExamBlueprint
from backend.models.paper import Paper
from backend.models.paper_questions import PaperQuestion
from backend.models.question import Question


def build_paper(
    db: Session,
    exam_id: int,
    question_count: int,
    title: str | None = None
) -> Paper:
    """
    Assemble and persist a paper using existing questions from the database.

    Validates exam existence and sufficiency of questions. Connects selected questions
    via PaperQuestion records with 1-based sequential numbering. Uses blueprint duration
    when available.
    """
    if question_count <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Requested question count must be greater than 0"
        )

    # Verify that the exam exists
    exam = (
        db.query(Exam)
        .filter(Exam.id == exam_id)
        .first()
    )

    if not exam:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exam not found"
        )

    # Retrieve all available questions for this exam
    questions = (
        db.query(Question)
        .filter(Question.exam_id == exam_id)
        .order_by(Question.id)
        .all()
    )

    if len(questions) < question_count:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Insufficient questions for exam {exam_id}. Requested: {question_count}, Available: {len(questions)}"
        )

    selected_questions = questions[:question_count]

    # Determine duration from exam blueprints if available
    blueprints = (
        db.query(ExamBlueprint)
        .filter(ExamBlueprint.exam_id == exam_id)
        .all()
    )

    duration_minutes = 60
    if blueprints:
        durations = [bp.duration_minutes for bp in blueprints if bp.duration_minutes]
        if durations:
            if len(set(durations)) == 1:
                duration_minutes = durations[0]
            else:
                duration_minutes = sum(durations)

    paper_title = title if title and title.strip() else f"{exam.name} Practice Paper"

    # Create Paper record
    new_paper = Paper(
        exam_id=exam_id,
        title=paper_title,
        total_questions=question_count,
        duration_minutes=duration_minutes
    )
    db.add(new_paper)
    db.flush()

    # Create PaperQuestion records with sequential numbering
    for idx, q in enumerate(selected_questions, start=1):
        paper_question = PaperQuestion(
            paper_id=new_paper.id,
            question_id=q.id,
            question_number=idx
        )
        db.add(paper_question)

    # Commit once and refresh the paper
    db.commit()
    db.refresh(new_paper)

    return new_paper

