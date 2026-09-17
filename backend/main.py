from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.db.database import engine, Base
from backend.models.user import User
from backend.models.exam import Exam
from backend.models.exam_blueprint import ExamBlueprint
from backend.models.topic import Topic
from backend.models.question import Question
from backend.models.paper import Paper
from backend.models.paper_questions import PaperQuestion
from backend.models.attempt import Attempt
from backend.models.attempt_answer import AttemptAnswer
from backend.models.result import Result
from backend.routes.paper_questions import router as paper_questions_router

from backend.routes.exams import router as exams_router
from backend.routes.exam_blueprint import router as exam_blueprints_router
from backend.routes.topics import router as topics_router
from backend.routes.questions import router as questions_router
from backend.routes.papers import router as papers_router
from backend.routes.auth import router as auth_router
from backend.routes.attempts import router as attempts_router
from backend.routes.attempt_answers import router as attempt_answers_router
from backend.routes.results import router as results_router
# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Gayatri Exam Portal",
    description="Competitive Exam Mock Test Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exams_router)
app.include_router(exam_blueprints_router)
app.include_router(topics_router)
app.include_router(questions_router)
app.include_router(papers_router)
app.include_router(auth_router)
app.include_router(paper_questions_router)
app.include_router(attempts_router)
app.include_router(attempt_answers_router)
app.include_router(results_router)

@app.get("/")
def home():
    return {
        "message": "Gayatri Exam Portal is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }