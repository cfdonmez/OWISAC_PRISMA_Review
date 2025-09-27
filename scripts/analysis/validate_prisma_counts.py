import json, sys
from pathlib import Path

SCHEMA = Path(".meta/prisma_counts.schema.json")
COUNTS = Path("results/prisma_counts.json")

def main():
    if not SCHEMA.exists():
        print("[error] Missing schema: .meta/prisma_counts.schema.json", file=sys.stderr)
        sys.exit(2)
    if not COUNTS.exists():
        print("[error] Missing counts: results/prisma_counts.json", file=sys.stderr)
        sys.exit(3)

    # Try to use jsonschema if available
    try:
        from jsonschema import validate, Draft202012Validator
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        counts = json.loads(COUNTS.read_text(encoding="utf-8"))

        Draft202012Validator.check_schema(schema)
        validate(instance=counts, schema=schema)
        print("[ok] PRISMA counts conform to schema ✔")
        sys.exit(0)

    except ModuleNotFoundError:
        # Fallback: minimal shape checks without jsonschema
        print("[warn] 'jsonschema' not installed; running minimal checks…")
        required = [
            "identified","deduplicated","screened","excluded_title_abs",
            "fulltext_assessed","fulltext_excluded","included_qual","included_quant"
        ]
        counts = json.loads(COUNTS.read_text(encoding="utf-8"))
        missing = [k for k in required if k not in counts]
        if missing:
            print(f"[error] Missing keys: {missing}", file=sys.stderr)
            sys.exit(4)
        print("[ok] Minimal checks passed (install 'jsonschema' for full validation)")
        sys.exit(0)

    except Exception as e:
        print(f"[error] Schema validation failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
