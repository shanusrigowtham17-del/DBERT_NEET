from pathlib import Path
import json

from ingestion.question_normalizer import (
    validate_question,
    find_duplicates,)

INPUT_FILE = Path(
    "data/Question_Bank/normalized/questions_normalized.json"
)
OUTPUT_FILE = Path(
    "data/Question_Bank/processed/questions.json"
)

def load_questions():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        questions = json.load(file)

        return questions

def validate_questions(questions):
    valid_questions = []
    invalid_questions =[]

    for index, question in enumerate(questions, start = 1):
        missing_fields = validate_question(question)

        if missing_fields:
            invalid_questions.append({
                "index": index,
                "missing_fields": missing_fields
            })
        else:
            valid_questions.append(question)

    return valid_questions, invalid_questions

def remove_duplicates(questions):
    clean_questions = []
    duplicates = []

    questions_by_source = {}

    for question in questions:
        source = question.get("source")

        if source not in questions_by_source:
            questions_by_source[source] = []

        questions_by_source[source].append(question)

    for source_questions in questions_by_source.values():
        source_duplicates = find_duplicates(source_questions)

        duplicate_indices = {
            duplicate["duplicate_index"]
            for duplicate in source_duplicates
        }

        for index, question in enumerate(source_questions, start=1):
            if index not in duplicate_indices:
                clean_questions.append(question)

        duplicates.extend(source_duplicates)

    return clean_questions, duplicates

def process_import():
    questions = load_questions()

    valid_questions, invalid_questions = validate_questions(questions)

    clean_questions, duplicates = remove_duplicates(valid_questions)

    return clean_questions, invalid_questions, duplicates

def save_questions(questions):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(
            questions,
            file,
            indent=4,
            ensure_ascii=False
        )
