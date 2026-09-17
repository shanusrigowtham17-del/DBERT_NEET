from ingestion.process_questions import process_questions
from ingestion.import_questions import process_import, save_questions


def main():
    print("Starting question ingestion pipeline...")

    process_questions()

    clean_questions, invalid_questions, duplicates = process_import()

    save_questions(clean_questions)

    print("\n========== FINAL SUMMARY ==========")
    print(f"Invalid questions: {len(invalid_questions)}")
    print(f"Duplicate questions removed: {len(duplicates)}")
    print(f"Final questions written: {len(clean_questions)}")
    print("Question ingestion completed successfully.")


if __name__ == "__main__":
    main()