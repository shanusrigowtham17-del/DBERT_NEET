import json
from pathlib import Path

from ingestion.question_parser import parse_csv
from ingestion.question_normalizer import (
    normalize_questions,
    validate_question,
    find_duplicates,
)

CSV_FOLDER = Path("dbert/neet_pyqs_csv")

def get_csv_files():
    return sorted(CSV_FOLDER.glob("*.csv"))

def process_questions():
    csv_files = get_csv_files()

    print(f"CSV files found: {len(csv_files)}")

    all_questions = []

    total_invalid = 0
    total_duplicates = 0

    for csv_file in csv_files:
        print(f"\nProcessing: {csv_file.name}")

        questions = parse_csv(csv_file)

        print(f"Questions parsed: {len(questions)}")

        normalized_questions = normalize_questions(questions)

        print(f"Questions normalized: {len(normalized_questions)}")
        all_questions.extend(normalized_questions)

        invalid_questions = []

        for index, question in enumerate(normalized_questions, start=1):
            missing_fields = validate_question(question)

            if missing_fields:
                invalid_questions.append({
                    "index": index,
                    "missing_fields": missing_fields
                })

        for invalid in invalid_questions:
            print(
                f"Invalid question #{invalid['index']} "
                f"missing: {invalid['missing_fields']}"
            )

        print(f"Invalid questions: {len(invalid_questions)}")
        total_invalid += len(invalid_questions)

        duplicates = find_duplicates(normalized_questions)

        print(f"Duplicate questions: {len(duplicates)}")
        total_duplicates += len(duplicates)

        for duplicate in duplicates:
            print(
                f"Duplicate question #{duplicate['duplicate_index']} "
                f"matches question #{duplicate['original_index']}"
            )

    print("\n========== SUMMARY ==========")
    print(f"Total CSV files: {len(csv_files)}")
    print(f"Total questions: {len(all_questions)}")
    print(f"Total invalid questions: {total_invalid}")
    print(f"Total duplicate questions: {total_duplicates}")
        
    output_file = Path(
        "data/Question_Bank/normalized/questions_normalized.json"
    )
    output_file.parent.mkdir(parents=True, exist_ok = True)

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(all_questions, file, indent = 4, ensure_ascii=False)

    print(f"\nNormalized JSON written to: {output_file}")

    return all_questions