# Question Bank Ingestion Pipeline

## Running the Pipeline

The complete ingestion pipeline can be executed using the main entry point.
From Terminal
First, make sure you are in the project root:
cd /Users/arijitshaw/Documents/Dbert_Python/DBERT_NEET
Then run:
python3 -m ingestion.main

## Overview

The `ingestion` module processes NEET/AIPMT/AIIMS question-bank CSV files and converts them into a standardized JSON format for use by the DBERT NEET application.

The ingestion pipeline performs the following operations:

1. Reads question-bank CSV files.
2. Parses the CSV data into a standard question structure.
3. Normalizes text, options, and answer values.
4. Validates required question fields.
5. Detects duplicate questions within the same source.
6. Generates an intermediate normalized JSON file.
7. Removes invalid and duplicate questions during the import stage.
8. Generates the final clean question-bank JSON file.

The ingestion module does **not** insert data directly into the database.

---

## Pipeline Flow

```text
CSV Question Banks
        |
        v
question_parser.py
        |
        v
Parsed Questions
        |
        v
question_normalizer.py
        |
        v
Normalized Questions
        |
        v
Validation + Duplicate Detection
        |
        v
questions_normalized.json
        |
        v
import_questions.py
        |
        +---- Invalid Questions Removed
        |
        +---- Duplicate Questions Removed
        |
        v
questions.json
        |
        v
FastAPI Backend
        |
        v
Question Bank / Database
```

---

## Directory Structure

```text
ingestion/
├── __init__.py
├── main.py
├── question_parser.py
├── question_normalizer.py
├── process_questions.py
├── import_questions.py
└── README.md
```

### File Responsibilities

#### `main.py`

Main entry point for the ingestion pipeline.

It executes the complete workflow:

```text
CSV Processing
      ↓
Normalization
      ↓
Validation
      ↓
Duplicate Detection
      ↓
Final Import
```

Run the complete pipeline using:

```bash
python3 -m ingestion.main
```

---

#### `question_parser.py`

Responsible for reading individual CSV files and converting each row into the internal question structure.

The parser:

* Reads CSV files using Python's `csv` module.
* Checks for required CSV columns.
* Extracts question text.
* Extracts options A-D.
* Extracts the available answer.
* Extracts difficulty.
* Creates a readable source name.
* Converts empty values into `None`.

The parser does not generate missing answers or explanations.

---

#### `question_normalizer.py`

Responsible for normalizing and validating parsed questions.

It:

* Removes unnecessary whitespace.
* Normalizes answer values to `A`, `B`, `C`, or `D`.
* Preserves question meaning.
* Validates required fields.
* Detects duplicate questions using normalized question text.

The normalizer does not generate answers, explanations, or missing options.

---

#### `process_questions.py`

Processes all CSV files available in the configured question-bank directory.

It:

1. Finds all CSV files.
2. Parses each CSV.
3. Normalizes the questions.
4. Checks for missing required fields.
5. Detects duplicates within each source.
6. Combines all normalized questions.
7. Writes the intermediate normalized JSON file.

Output:

```text
data/Question_Bank/normalized/questions_normalized.json
```

---

#### `import_questions.py`

Responsible for the final import/cleanup stage.

It:

1. Reads the normalized JSON.
2. Validates each question.
3. Removes invalid questions from the final output.
4. Detects and removes duplicate questions within the same source.
5. Writes the final clean JSON file.

Output:

```text
data/Question_Bank/processed/questions.json
```

No database insertion is performed by this module.

---

## Input Format

The current CSV question-bank files use the following columns:

```text
questions
subject
chapter
difficulty
answer
option_a
option_b
option_c
option_d
year
```

Example:

```csv
questions,subject,chapter,difficulty,answer,option_a,option_b,option_c,option_d,year
"Example question?","Biology","Cell","Easy","A","Option one","Option two","Option three","Option four","2025"
```

The ingestion output does not include `subject`, `chapter`, or `year` in the normalized question schema.

---

## Standard Question Structure

Every normalized question follows this structure:

```json
{
    "text": "Question text",
    "option_a": "First option",
    "option_b": "Second option",
    "option_c": "Third option",
    "option_d": "Fourth option",
    "correct_option": "A",
    "explanation": null,
    "difficulty": "Easy",
    "source": "NEET 2025"
}
```

### Fields

| Field            | Description                                          |
| ---------------- | ---------------------------------------------------- |
| `text`           | Question text                                        |
| `option_a`       | Option A                                             |
| `option_b`       | Option B                                             |
| `option_c`       | Option C                                             |
| `option_d`       | Option D                                             |
| `correct_option` | Correct option normalized to A/B/C/D when available  |
| `explanation`    | Explanation if available; not generated by ingestion |
| `difficulty`     | Difficulty value when available                      |
| `source`         | Source examination/year                              |

---

## Validation

A question is considered incomplete when one or more of these fields are missing:

```text
text
option_a
option_b
option_c
option_d
```

Invalid questions are reported during processing and excluded from the final processed JSON.

The ingestion pipeline does not attempt to guess or generate missing information.

---

## Duplicate Detection

Duplicate questions are detected using the normalized question text.

The comparison is case-insensitive.

For example:

```text
What is photosynthesis?
```

and:

```text
WHAT IS PHOTOSYNTHESIS?
```

are treated as duplicates.

Duplicate detection is performed within the same source.

The first occurrence is retained, while later duplicate occurrences are excluded from the final processed JSON.

---

## Current Dataset Verification

The current dataset contains:

```text
CSV files processed:          13
Total questions parsed:       2440
Invalid questions:            10
Duplicate questions removed:  17
Final clean questions:        2413
```

The final output is:

```text
data/Question_Bank/processed/questions.json
```

The relationship is:

```text
2440 total
 - 10 invalid
 - 17 duplicate
----------------
 = 2413 final questions
```

---

## Running the Pipeline

Run the complete ingestion pipeline from the project root:

```bash
python3 -m ingestion.main
```

The project root should be:

```text
DBERT_NEET/
```

Do not run the module while the current working directory is inside `ingestion/`, because the pipeline uses project-relative paths.

---

## Output Files

### Intermediate Output

```text
data/Question_Bank/normalized/questions_normalized.json
```

Contains all normalized questions before final import cleanup.

### Final Output

```text
data/Question_Bank/processed/questions.json
```

Contains the validated and duplicate-cleaned question bank intended for consumption by the backend.

---

## Dependencies

The ingestion pipeline currently uses Python standard-library modules:

```text
csv
json
pathlib
re
```

No external AI/LLM API is required for the ingestion pipeline.

---

## Backend Integration

The ingestion pipeline does not modify the FastAPI backend or database.

The intended workflow is:

```text
Question CSV Files
        ↓
Ingestion Pipeline
        ↓
questions.json
        ↓
FastAPI Backend
        ↓
Question Database / API
        ↓
Frontend
```

The backend team can consume the final:

```text
data/Question_Bank/processed/questions.json
```

according to the backend's own database/import workflow.

---

## Important Notes

* Source CSV files are not modified by the ingestion pipeline.
* Missing answers are not generated.
* Missing explanations are not generated.
* OCR errors or questionable source data are not automatically corrected.
* Invalid questions are excluded from the final clean JSON.
* Duplicate questions are removed only from the final output; the original source data remains unchanged.
* Running the pipeline again regenerates the normalized and processed JSON files from the current CSV data.

If the source CSV files are corrected or updated, run the ingestion pipeline again to regenerate the JSON outputs.
