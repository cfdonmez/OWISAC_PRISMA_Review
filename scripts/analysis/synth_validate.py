import csv, json, sys
from pathlib import Path
from jsonschema import validate, Draft202012Validator

SCHEMA = Path(".meta/synthesis_schema.json")
SRC = Path("data/extraction/synthesis_input_demo.csv")

def main():
    if not SCHEMA.exists():
        print("[error] missing schema", file=sys.stderr); sys.exit(2)
    if not SRC.exists():
        print("[error] missing input CSV", file=sys.stderr); sys.exit(3)

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))

    rows = []
    with SRC.open(newline='', encoding="utf-8") as f:
        for row in csv.DictReader(f):
            # tip dönüşümleri
            row["year"] = int(row["year"])
            row["value"] = float(row["value"]) if row["value"] != "" else 0.0
            rows.append(row)

    Draft202012Validator.check_schema(schema)
    validate(instance=rows, schema=schema)
    print("[ok] synthesis input conforms to schema ✔ (rows:", len(rows), ")")

if __name__ == "__main__":
    main()
