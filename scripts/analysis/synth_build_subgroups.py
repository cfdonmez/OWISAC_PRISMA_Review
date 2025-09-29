import csv
from pathlib import Path
from collections import defaultdict

SRC = Path("data/extraction/synthesis_input_demo.csv")
OUT_CSV = Path("results/synthesis_tables/subgroups.csv")
OUT_MD  = Path("results/synthesis_tables/subgroups.md")

def main():
    if not SRC.exists():
        raise SystemExit("missing data/extraction/synthesis_input_demo.csv")

    rows = list(csv.DictReader(SRC.open(encoding="utf-8")))
    agg_sum = defaultdict(float)
    agg_cnt = defaultdict(int)

    for r in rows:
        key = (r["beamforming_strategy"], r["metric"])
        try:
            v = float(r["value"]) if r["value"] != "" else 0.0
        except Exception:
            v = 0.0
        agg_sum[key] += v
        agg_cnt[key] += 1

    pairs = sorted(agg_sum.keys(), key=lambda k: (k[0], k[1]))
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

    # CSV
    with OUT_CSV.open("w", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["beamforming_strategy","metric","mean_value"])
        for (bf, m) in pairs:
            mean = agg_sum[(bf,m)] / agg_cnt[(bf,m)]
            w.writerow([bf, m, f"{mean:.6g}"])

    # Markdown
    with OUT_MD.open("w", encoding="utf-8") as f:
        f.write("# Synthesis Subgroups (demo)\n\n")
        f.write("| Beamforming | Metric | Mean value |\n|---|---|---:|\n")
        for (bf, m) in pairs:
            mean = agg_sum[(bf,m)] / agg_cnt[(bf,m)]
            f.write(f"| {bf} | {m} | {mean:.6g} |\n")

    print(f"[ok] wrote {OUT_CSV} and {OUT_MD}")

if __name__ == "__main__":
    main()
