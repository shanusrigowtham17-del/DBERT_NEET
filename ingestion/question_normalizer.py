import re

VALID_OPTIONS = {"A", "B", "C", "D"}

def normalize_text(value):
       # Remove unnecessary whitespace from a text field.

    if value is None:
        return None

    value = str(value).strip()

    # Replace multiple spaces/newlines/tabs with one space
    value = re.sub(r"\s+"," ", value)

    return value

def normalize_correct_option(value):
    # Convert an answer value into A/B/C/D format.

    if value is None:
        return None

    value = str(value).strip().upper()

    # Remove common formatting around the answer.
    value = value.replace("OPTION", "").strip()
    value = value.replace("(", "").replace(")", "").strip()
    value = value.replace(".", "").strip()

    if value in VALID_OPTIONS:
        return value

    return None

def normalize_question(question):
    # Normalize parsed question.

    normalized = {
        "text": normalize_text(question.get("text")),
        "option_a": normalize_text(question.get("option_a")),
        "option_b": normalize_text(question.get("option_b")),
        "option_c": normalize_text(question.get("option_c")),
        "option_d": normalize_text(question.get("option_d")),
        "correct_option": normalize_correct_option(question.get("correct_option")),
        "explanation": normalize_text(question.get("explanation")),
        "difficulty": normalize_text(question.get("difficulty")),
        "source": normalize_text(question.get("source")),
    }

    return normalized

def normalize_questions(questions):
    # Normalize a list of parsed questions.

    normalized_questions = []

    for question in questions:
        normalized_question = normalize_question(question)
        normalized_questions.append(normalized_question)

    return normalized_questions

def validate_question(question):
    # Check weather a normalized question has all required fields.

    required_fields = [
        "text",
        "option_a",
        "option_b",
        "option_c",
        "option_d",
    ]

    missing_fields = []
    for field in required_fields:
        if not question.get(field):
            missing_fields.append(field)

    return missing_fields

def find_duplicates(questions):
    """
    Find duplicate questions based on normalized question text.
    """
    seen_questions = {}
    duplicates = []

    for index, question in enumerate(questions, start=1):
        text = question.get("text")

        if not text:
            continue

        question_key = text.casefold()

        if question_key in seen_questions:
            duplicates.append({
                "duplicate_index": index,
                "original_index": seen_questions[question_key],
            })
        else:
            seen_questions[question_key] = index

    return duplicates
