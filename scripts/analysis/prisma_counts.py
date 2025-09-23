#!/usr/bin/env python3
import csv, json, os, sys
from collections import Counter, defaultdict
from datetime import datetime

SCREENING_CSV = sys.argv[1] if len(sys.argv) > 1 else "data/screening_log.csv"
OUT_JSON = "results/prisma_counts.json"
OUT_CSV = "results/synthesis_tables/prisma_counts.csv"

def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r)

def to_int(x, default=0):
    try:
        return int(str(x).strip())
    except:
        return default

def main():
    os.makedirs("results/synthesis_tables", exist_ok=True)
    rows = read_rows(SCREENING_CSV)

    # Beklenen sütunlar (esnek isimlendirme desteği)
    # date, source, query_id, hits, included_phase1, included_phase2
    total_hits = 0
    phase1 = 0
    phase2 = 0

    source_hits = Counter()
    by_date = defaultdict(lambda: {"hits":0, "p1":0, "p2":0})

    for row in rows:
        date = row.get("date") or row.get("Date") or ""
        src  = row.get("source") or row.get("SRC") or "NA"
        hits_i = to_int(row.get("hits") or row.get("Hits"))
        p1_i   = to_int(row.get("included_phase1") or row.get("phase1") or row.get("Included_P1"))
        p2_i   = to_int(row.get("included_phase2") or row.get("phase2") or row.get("Included_P2"))

        total_hits += hits_i
        phase1 += p1_i
        phase2 += p2_i
        source_hits[src] += hits_i

        if date:
            by_date[date]["hits"] += hits_i
            by_date[date]["p1"]   += p1_i
            by_date[date]["p2"]   += p2_i

    prisma = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "totals": {
            "identification_hits": total_hits,
            "screening_included_p1": phase1,
            "eligibility_included_p2": phase2
        },
        "by_source": dict(source_hits),
        "by_date": by_date
    }

    # JSON
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(prisma, f, indent=2, ensure_ascii=False)

    # CSV
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["date","hits","included_phase1","included_phase2"])
        for d in sorted(by_date.keys()):
            dd = by_date[d]
            w.writerow([d, dd["hits"], dd["p1"], dd["p2"]])

    print(f"Wrote {OUT_JSON} and {OUT_CSV}")

if __name__ == "__main__":
    main()
