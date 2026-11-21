from sqlalchemy.orm import Session

from backend.models.attempt import Attempt
from backend.models.paper import Paper
from backend.models.paper_questions import PaperQuestion
from backend.models.question import Question
from backend.models.attempt_answer import AttemptAnswer
from backend.models.exam_blueprint import ExamBlueprint
from backend.models.topic import Topic


def _get_question_blueprint(question, paper_question, blueprints, topic_by_id):
    """
    Match a question to its appropriate ExamBlueprint.
    Handles multiple blueprints (sections) by topic matching,
    question number range, or falling back to the first blueprint.
    """
    if not blueprints:
        return None

    if len(blueprints) == 1:
        return blueprints[0]

    # Try matching question topic name to blueprint section_name
    if question and question.topic_id in topic_by_id:
        topic_name = topic_by_id[question.topic_id].name.strip().lower()
        for bp in blueprints:
            bp_section = bp.section_name.strip().lower()
            if bp_section == topic_name or bp_section in topic_name or topic_name in bp_section:
                return bp

    # Try matching question_number within cumulative num_questions of blueprints
    if paper_question and paper_question.question_number is not None:
        cumulative = 0
        for bp in blueprints:
            cumulative += bp.num_questions
            if paper_question.question_number <= cumulative:
                return bp

    # Fallback to the first blueprint
    return blueprints[0]


def calculate_attempt_score(db: Session, attempt: Attempt) -> dict:
    """
    Calculate the score and question statistics for a given attempt.

    Relationships:
    Attempt -> Paper -> PaperQuestion -> Question
    Attempt -> AttemptAnswer

    Returns:
    {
        "total_questions": int,
        "attempted_questions": int,
        "correct_answers": int,
        "wrong_answers": int,
        "unanswered_questions": int,
        "score": float
    }
    """
    paper = (
        db.query(Paper)
        .filter(Paper.id == attempt.paper_id)
        .first()
    )

    if not paper:
        return {
            "total_questions": 0,
            "attempted_questions": 0,
            "correct_answers": 0,
            "wrong_answers": 0,
            "unanswered_questions": 0,
            "score": 0.0
        }

    # Fetch paper questions ordered by question_number
    paper_questions = (
        db.query(PaperQuestion)
        .filter(PaperQuestion.paper_id == paper.id)
        .order_by(PaperQuestion.question_number)
        .all()
    )

    question_ids = [pq.question_id for pq in paper_questions]
    questions = (
        db.query(Question)
        .filter(Question.id.in_(question_ids))
        .all()
    )
    question_by_id = {q.id: q for q in questions}

    # Fetch student answers for this attempt
    answers = (
        db.query(AttemptAnswer)
        .filter(AttemptAnswer.attempt_id == attempt.id)
        .all()
    )
    answer_by_question_id = {ans.question_id: ans.selected_option for ans in answers}

    # Fetch blueprints and topics for the exam
    blueprints = (
        db.query(ExamBlueprint)
        .filter(ExamBlueprint.exam_id == paper.exam_id)
        .all()
    )
    topics = (
        db.query(Topic)
        .filter(Topic.exam_id == paper.exam_id)
        .all()
    )
    topic_by_id = {t.id: t for t in topics}

    total_questions = len(paper_questions)
    attempted_questions = 0
    correct_answers = 0
    wrong_answers = 0
    unanswered_questions = 0
    score = 0.0

    for pq in paper_questions:
        q = question_by_id.get(pq.question_id)
        if not q:
            unanswered_questions += 1
            continue

        bp = _get_question_blueprint(q, pq, blueprints, topic_by_id)
        marks_per_question = float(bp.marks_per_question) if bp else 1.0
        negative_marks = float(bp.negative_marks) if bp else 0.0

        selected = answer_by_question_id.get(q.id)

        # 1. Unanswered if NULL or empty
        if selected is None or str(selected).strip() == "":
            unanswered_questions += 1
        # 2. Correct if matches Question.correct_option
        elif str(selected).strip().upper() == str(q.correct_option).strip().upper():
            attempted_questions += 1
            correct_answers += 1
            score += marks_per_question
        # 3. Wrong otherwise
        else:
            attempted_questions += 1
            wrong_answers += 1
            score -= negative_marks

    return {
        "total_questions": total_questions,
        "attempted_questions": attempted_questions,
        "correct_answers": correct_answers,
        "wrong_answers": wrong_answers,
        "unanswered_questions": unanswered_questions,
        "score": round(score, 2)
    }

