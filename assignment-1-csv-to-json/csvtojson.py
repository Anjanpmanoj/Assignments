import csv
import json


def csv_to_json(csv_path, json_path):
    with open(csv_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # Convert numeric fields from strings to ints
    for row in rows:
        row["roll_no"] = int(row["roll_no"])
        row["marks"] = int(row["marks"])

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)

    print(f"Converted {len(rows)} rows -> {json_path}")


if __name__ == "__main__":
    csv_to_json("students.csv", "students.json")
