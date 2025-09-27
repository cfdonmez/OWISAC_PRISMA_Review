import csv, json, datetime
from pathlib import Path
from collections import Counter

LOG = Path("data/screening_log.csv")
EXCLUDED = Path("data/excluded_studies.csv")
OUT = Path("results/prisma_counts.json")

def main():
    if not LOG.exists():
        raise SystemExit("Missing data/screening_log.csv")

    # Varsayım: screening_log.csv 'status' kolonu içeriyor
    # status ∈ {included, excluded_title_abs, fulltext_assessed, fulltext_excluded}
    status_counts = Counter()
    with LOG.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            st = (row.get("status") or "").strip().lower()
            if st:
                status_counts[st] += 1

    # Excluded reasons detayları (varsa)
    reasons = Counter()
    if EXCLUDED.exists():
        with EXCLUDED.open() as f:
            reader = csv.DictReader(f)
            for row in reader:
                r = (row.get("reason") or "").strip().lower()
                if r:
                    reasons[r] += 1

    counts = {
        "identified": status_counts.get("identified", 0),
        "deduplicated": status_counts.get("deduplicated", 0),
        "screened": status_counts.get("screened", 0),
        "excluded_title_abs": status_counts.get("excluded_title_abs", 0),
        "fulltext_assessed": status_counts.get("fulltext_assessed", 0),
        "fulltext_excluded": dict(reasons) if reasons else {},
        "included_qual": status_counts.get("included_qual", 0),
        "included_quant": status_counts.get("included_quant", 0),
        "last_updated": datetime.datetime.utcnow().isoformat() + "Z",
    }

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(counts, indent=2), encoding="utf-8")
    print(f"[ok] Wrote {OUT}")

if __name__ == "__main__":
    main()
