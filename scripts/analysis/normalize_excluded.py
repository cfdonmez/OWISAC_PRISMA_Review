import csv
from pathlib import Path

SRC = Path("data/excluded_studies.csv")
DST = Path("data/excluded_studies_normalized.csv")

MAP = {
    "duplicate": "duplicate",
    "non-optical": "not_optical",
    "not optical": "not_optical",
    "no opa": "no_opa_or_ris",
    "no ris": "no_opa_or_ris",
    "no nlos": "no_nlos_or_turbulence",
    "no turbulence": "no_nlos_or_turbulence",
    "out of scope": "out_of_scope",
    "insufficient": "insufficient_methods",
    "method": "insufficient_methods",
    "no metric": "no_metrics",
    "no key-physics": "no_metrics",
    "not substantial": "not_substantial",
}

def infer_code(txt: str) -> str | None:
    s = (txt or "").lower()
    for key, code in MAP.items():
        if key in s:
            return code
    return None

def main():
    if not SRC.exists():
        raise SystemExit("Missing data/excluded_studies.csv")

    with SRC.open(newline='', encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    # kolonları garanti et
    fieldnames = list({*rows[0].keys(), "reason_code"}) if rows else ["record_id","reason","reason_code","notes"]

    for r in rows:
        if not (r.get("reason_code") or "").strip():
            code = infer_code(r.get("reason",""))
            if code:
                r["reason_code"] = code

    DST.parent.mkdir(exist_ok=True)
    with DST.open("w", newline='', encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    print(f"[ok] wrote {DST} (filled missing reason_code where possible)")

if __name__ == "__main__":
    main()
