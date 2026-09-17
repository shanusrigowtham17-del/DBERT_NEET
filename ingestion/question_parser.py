import csv
from pathlib import Path

REQUIRED_COLUMNS = {
    "questions",
    "option_a",
    "option_b",
    "option_c",
    "option_d",
    "answer",
    "difficulty"
}

def get_source_name(csv_path):
    """
    Creates a readable source name from the CSV filename.

    Example:
    neet_2025_dataset_final_biology.csv
    -> NEET 2025
    """

    filename = csv_path.stem.lower()

    if "2025" in filename:
        return "NEET 2025"
    if "2024" in filename:
        return "NEET 2024"
    if "2023" in filename:
        return "NEET 2023"
    if "2022" in filename:
        return "NEET 2022"
    if "2021" in filename:
        return "NEET 2021"
    if "2020" in filename:
        return "NEET 2020"
    if "2019" in filename:
        return "NEET 2019"
    if "2018" in filename:
        return "NEET 2018"
    if "2017" in filename:
        return "NEET 2017"
    if "2016" in filename:
        return "NEET 2016"
    if "2015" in filename:
        return "AIPMT 2015"
    if "2014" in filename:
        return "AIPMT 2014"
    if "2013" in filename:
        return "AIIMS 2013"

    return csv_path.stem

def clean_value(value):
    """ Converts empty CSV values to None and remove extra spaces. """

    if value is None:
        return None

    value = str(value).strip()

    if not value:
        return None

    return value

def parse_csv(csv_path):
    """
       Read one CSV file and convert every row
       into the standard question structure.
    """

    questions = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        columns = set(reader.fieldnames or [])

        missing_columns = REQUIRED_COLUMNS - columns

        if missing_columns:
            raise ValueError(
                f"Missing columns in {csv_path.name}: {missing_columns}"
            )
        source = get_source_name(Path(csv_path))

        for row_number, row in enumerate(reader, start = 2):

            question = {
                "text": clean_value(row.get("questions")),
                "option_a": clean_value(row.get("option_a")),
                "option_b": clean_value(row.get("option_b")),
                "option_c": clean_value(row.get("option_c")),
                "option_d": clean_value(row.get("option_d")),
                "correct_option": clean_value(row.get("answer")),
                "explanation": None,
                "difficulty": clean_value(row.get("difficulty")),
                "source": source,
                "subject": clean_value(row.get("subject")),
                "chapter": clean_value(row.get("chapter")),
                "year": clean_value(row.get("year")),
            }

            question["_source_file"] = Path(csv_path).name
            question["_source_row"] = row_number

            questions.append(question)

        return questions



