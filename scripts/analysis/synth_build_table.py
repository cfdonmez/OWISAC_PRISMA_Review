import csv
from pathlib import Path

SRC = Path("data/extraction/synthesis_input_demo.csv")
OUT_CSV = Path("results/synthesis_tables/summary.csv")
OUT_MD  = Path("results/synthesis_tables/summary.md")

def main():
    if not SRC.exists():
        raise SystemExit("missing data/extraction/synthesis_input_demo.csv")

    rows = list(csv.DictReader(SRC.open(encoding="utf-8")))
    # küçük bir pivot: metric bazında ortalama değer (örnek)
    metrics = {}
    counts = {}
    for r in rows:
        m = r["metric"]
        v = float(r["value"]) if r["value"] != "" else 0.0
        metrics[m] = metrics.get(m, 0.0) + v
        counts[m] = counts.get(m, 0) + 1
    agg = [(m, metrics[m]/counts[m]) for m in metrics]

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline='', encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["metric","mean_value"])
        for m, mean in agg:
            w.writerow([m, f"{mean:.6g}"])

    # Markdown sürümü
    with OUT_MD.open("w", encoding="utf-8") as f:
        f.write("# Synthesis Summary (demo)\n\n")
        f.write("| Metric | Mean value |\n|---|---:|\n")
        for m, mean in agg:
            f.write(f"| {m} | {mean:.6g} |\n")

    print(f"[ok] wrote {OUT_CSV} and {OUT_MD}")

if __name__ == "__main__":
    main()
