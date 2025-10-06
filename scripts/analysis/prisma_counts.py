#!/usr/bin/env python3
import csv, json, os, sys
from collections import Counter, defaultdict
from datetime import datetime

SCREENING_CSV = sys.argv[1] if len(sys.argv) > 1 else "data/screening_log.csv"
OUT_JSON = "results/prisma_counts.json"
OUT_CSV  = "results/synthesis_tables/prisma_counts.csv"

def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r)

def to_int(x, default=0):
    try:
        return int(str(x).strip())
    except:
        return default

def has_any(cols, *cands):
    cl = [c.lower() for c in cols]
    for c in cands:
        if c.lower() in cl:
            return True
    return False

def pick(row, *keys, default=""):
    for k in keys:
        if k in row and row[k] not in (None, ""):
            return row[k]
        # case-insensitive fallback
        for kk in row.keys():
            if kk.lower() == k.lower() and row[kk] not in (None, ""):
                return row[kk]
    return default

def main():
    os.makedirs("results/synthesis_tables", exist_ok=True)
    rows = read_rows(SCREENING_CSV)
    cols = list(rows[0].keys()) if rows else []

    # --- MODE DETECTION ---
    # Aggregated mode if 'hits' column exists; else row-level mode if 'screening_judgement/decision' exists
    aggregated_mode = has_any(cols, "hits")
    row_mode = (has_any(cols, "screening_judgement", "screening_judgment", "decision"))

    total_hits = 0
    phase1 = 0
    phase2 = 0
    source_hits = Counter()
    by_date = defaultdict(lambda: {"hits":0, "p1":0, "p2":0})

    if aggregated_mode:
        # === AGGREGATED MODE (original behavior) ===
        for row in rows:
            date = pick(row, "date", "Date")
            src  = pick(row, "source", "SRC") or "NA"
            hits_i = to_int(pick(row, "hits", "Hits"))
            p1_i   = to_int(pick(row, "included_phase1", "phase1", "Included_P1"))
            p2_i   = to_int(pick(row, "included_phase2", "phase2", "Included_P2"))

            total_hits += hits_i
            phase1 += p1_i
            phase2 += p2_i
            source_hits[src] += hits_i

            if date:
                by_date[date]["hits"] += hits_i
                by_date[date]["p1"]   += p1_i
                by_date[date]["p2"]   += p2_i

    elif row_mode:
        # === ROW-LEVEL MODE (your data1.xlsx style) ===
        # Normalize judgement
        def norm_judg(s):
            t = str(s).strip().lower()
            if t in {"include","included","yes","y","1"}:
                return "include"
            if t in {"exclude","excluded","no","n","0"}:
                return "exclude"
            return "other"

        # If source missing, default single source to 'Elicit'
        for row in rows:
            total_hits += 1
            j = norm_judg(pick(row, "screening_judgement", "screening_judgment", "decision"))
            if j == "include":
                phase1 += 1
            # phase2 unknown at TIAB-only stage -> keep 0

            src = pick(row, "source", "SRC") or "Elicit"
            source_hits[src] += 1

            # date optional; if absent we skip by_date aggregation
            date = pick(row, "date")
            if date:
                by_date[date]["hits"] += 1
                by_date[date]["p1"]   += (1 if j == "include" else 0)
                by_date[date]["p2"]   += 0
    else:
        print("[error] Could not detect columns. Expect either aggregated (hits/phase1/phase2) "
              "or row-level (screening_judgement/decision).")
        sys.exit(1)

    prisma = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "totals": {
            "identification_hits": total_hits,
            "screening_included_p1": phase1,
            "eligibility_included_p2": phase2
        },
        "by_source": dict(source_hits),
        "by_date": by_date  # json.dump will handle dict fine
    }

    # Optional JSON schema validation if present
    try:
        from jsonschema import validate, Draft202012Validator  # type: ignore
        import pathlib
        schema_path = pathlib.Path(".meta/prisma_counts.schema.json")
        if schema_path.exists():
            with open(schema_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
            prisma["last_updated"] = datetime.utcnow().isoformat() + "Z"
            Draft202012Validator.check_schema(schema)
            validate(instance=prisma, schema=schema)
            print("[ok] PRISMA counts validated against schema")
        else:
            print("[warn] schema not found: .meta/prisma_counts.schema.json (skipping validation)")
    except Exception as e:
        print(f"[error] schema validation failed: {e}")

    # JSON
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(prisma, f, indent=2, ensure_ascii=False)

    # CSV (by_date)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date","hits","included_phase1","included_phase2"])
        for d in sorted(by_date.keys()):
            dd = by_date[d]
            w.writerow([d, dd["hits"], dd["p1"], dd["p2"]])

    print(f"Wrote {OUT_JSON} and {OUT_CSV}")

if __name__ == "__main__":
    main()
