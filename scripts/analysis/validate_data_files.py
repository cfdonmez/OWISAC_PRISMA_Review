import csv, sys, re
from pathlib import Path
from datetime import datetime

DDOC = Path(".meta/data_dictionary.md")
BASE = Path("data")
REPORT = Path("results/qa_data_report.txt")

ALLOWED_STATUS = {
    "identified","deduplicated","screened","excluded_title_abs",
    "fulltext_assessed","fulltext_excluded","included_qual","included_quant"
}
ALLOWED_REASON_CODES = {
    "out_of_scope","not_optical","no_opa_or_ris","no_nlos_or_turbulence",
    "insufficient_methods","no_metrics","duplicate","not_substantial"
}

def read_csv(path):
    with path.open(newline='', encoding="utf-8") as f:
        return list(csv.DictReader(f))

def iso8601_ok(s):
    try:
        # kabul: 2025-09-28T12:34:56Z veya +00:00
        datetime.fromisoformat(s.replace("Z","+00:00"))
        return True
    except Exception:
        return False

def validate_screening_log(p, problems):
    rows = read_csv(p)
    required = {"record_id","source_db","status","decided_by","decided_at"}
    missing_cols = required - set(rows[0].keys()) if rows else required
    if missing_cols:
        problems.append(f"[{p}] missing columns: {sorted(missing_cols)}")
        return
    for i, r in enumerate(rows, 1):
        rid = r.get("record_id","").strip()
        st  = r.get("status","").strip().lower()
        ts  = r.get("decided_at","").strip()
        if not rid:
            problems.append(f"[{p}#{i}] empty record_id")
        if st not in ALLOWED_STATUS:
            problems.append(f"[{p}#{i}] invalid status: {st!r}")
        if ts and not iso8601_ok(ts):
            problems.append(f"[{p}#{i}] invalid decided_at (ISO 8601 expected): {ts!r}")

def normalize_reason_text(t):
    s = t.lower()
    if any(k in s for k in ["duplicate","dup."]):
        return "duplicate"
    if "not optical" in s or "non-optical" in s:
        return "not_optical"
    if "no opa" in s or "no ris" in s:
        return "no_opa_or_ris"
    if "nlos" in s or "turbulence" in s:
        # burada "no nlos/turbulence" ifadesi free-text'te çok değişken; heuristik:
        if "no nlos" in s or "no turbulence" in s:
            return "no_nlos_or_turbulence"
    if "out of scope" in s:
        return "out_of_scope"
    if "insufficient" in s or "method" in s:
        return "insufficient_methods"
    if "no metric" in s or "no key-physics" in s:
        return "no_metrics"
    if "not substantial" in s:
        return "not_substantial"
    return None

def validate_excluded(p, problems, suggestions):
    rows = read_csv(p)
    required_any = {"record_id"}
    missing_cols = required_any - set(rows[0].keys()) if rows else required_any
    if missing_cols:
        problems.append(f"[{p}] missing columns: {sorted(missing_cols)}")
        return
    has_reason_code = "reason_code" in rows[0].keys() if rows else False
    has_reason_text = "reason" in rows[0].keys() if rows else False

    if not has_reason_code and not has_reason_text:
        problems.append(f"[{p}] needs 'reason_code' or 'reason' column")
        return

    for i, r in enumerate(rows, 1):
        rid = r.get("record_id","").strip()
        if not rid:
            problems.append(f"[{p}#{i}] empty record_id")

        if has_reason_code:
            code = (r.get("reason_code") or "").strip().lower()
            if code and code not in ALLOWED_REASON_CODES:
                problems.append(f"[{p}#{i}] invalid reason_code: {code!r}")
        if has_reason_text:
            txt = (r.get("reason") or "").strip()
            if txt:
                sug = normalize_reason_text(txt)
                if sug and (not has_reason_code or not r.get("reason_code")):
                    suggestions.append(f"{rid}\t{txt}\t=> {sug}")
            else:
                problems.append(f"[{p}#{i}] empty reason text")

def validate_included(p, problems):
    rows = read_csv(p)
    required = {"record_id","citation","year"}
    missing_cols = required - set(rows[0].keys()) if rows else required
    if missing_cols:
        problems.append(f"[{p}] missing columns: {sorted(missing_cols)}")
        return
    for i, r in enumerate(rows, 1):
        y = (r.get("year") or "").strip()
        if y and not y.isdigit():
            problems.append(f"[{p}#{i}] non-integer year: {y!r}")

def main():
    problems, suggestions = [], []
    if not DDOC.exists():
        problems.append("Missing .meta/data_dictionary.md")

    scr = BASE / "screening_log.csv"
    if scr.exists():
        validate_screening_log(scr, problems)
    else:
        problems.append("Missing data/screening_log.csv")

    exc = BASE / "excluded_studies.csv"
    if exc.exists():
        validate_excluded(exc, problems, suggestions)
    else:
        problems.append("Missing data/excluded_studies.csv")

    inc = BASE / "included_studies.csv"
    if inc.exists():
        validate_included(inc, problems)
    else:
        problems.append("Missing data/included_studies.csv")

    REPORT.parent.mkdir(exist_ok=True)
    with REPORT.open("w", encoding="utf-8") as f:
        if problems:
            f.write("## Problems\n")
            f.write("\n".join(problems) + "\n\n")
        else:
            f.write("## Problems\nNone\n\n")
        if suggestions:
            f.write("## Suggestions (normalize to reason_code)\n")
            for s in suggestions:
                f.write(s + "\n")
        else:
            f.write("## Suggestions\nNone\n")

    print(f"[ok] wrote report to {REPORT}")
    if problems:
        print("[warn] problems found — see report")

if __name__ == "__main__":
    main()
