import csv
from pathlib import Path
from collections import defaultdict

SRC = Path("data/extraction/synthesis_input_demo.csv")
OUT_MD = Path("results/synthesis_tables/rob_summary.md")

def main():
    if not SRC.exists():
        raise SystemExit("missing data/extraction/synthesis_input_demo.csv")

    rows = list(csv.DictReader(SRC.open(encoding="utf-8")))

    # Dummy RoB assessment based on available data
    rob_data = []
    for r in rows:
        # Simple heuristic-based RoB assessment
        year = int(r["year"])
        arch = r["architecture_components"]

        # Risk of bias domains (simplified for demo)
        rob_assessment = {
            "study_id": r["record_id"],
            "randomization": "Low" if "RIS" in arch else "High",
            "deviations": "Low" if year >= 2022 else "Some concerns",
            "missing_data": "Low",  # Assuming complete data for demo
            "measurement": "Low" if r["metric"] in ["SINR_dB", "BER"] else "Some concerns",
            "selection": "Low" if year >= 2021 else "High",
            "overall": "Low"
        }

        # Calculate overall risk
        risk_scores = []
        for domain in ["randomization", "deviations", "missing_data", "measurement", "selection"]:
            if rob_assessment[domain] == "High":
                risk_scores.append(3)
            elif rob_assessment[domain] == "Some concerns":
                risk_scores.append(2)
            else:
                risk_scores.append(1)

        avg_risk = sum(risk_scores) / len(risk_scores)
        if avg_risk >= 2.5:
            rob_assessment["overall"] = "High"
        elif avg_risk >= 1.8:
            rob_assessment["overall"] = "Some concerns"

        rob_data.append(rob_assessment)

    # Generate markdown summary
    with OUT_MD.open("w", encoding="utf-8") as f:
        f.write("# Risk of Bias Summary (demo)\n\n")
        f.write("| Study ID | Randomization | Deviations | Missing Data | Measurement | Selection | Overall |\n")
        f.write("|----------|---------------|------------|--------------|-------------|-----------|---------|\n")

        for rob in sorted(rob_data, key=lambda x: x["study_id"]):
            f.write(f"| {rob['study_id']} | {rob['randomization']} | {rob['deviations']} | ")
            f.write(f"{rob['missing_data']} | {rob['measurement']} | {rob['selection']} | ")
            f.write(f"**{rob['overall']}** |\n")

        # Summary statistics
        overall_counts = defaultdict(int)
        for rob in rob_data:
            overall_counts[rob["overall"]] += 1

        f.write(f"\n## Summary\n\n")
        f.write(f"- **Low risk**: {overall_counts['Low']} studies{chr(10)}")
        f.write(f"- **Some concerns**: {overall_counts['Some concerns']} studies{chr(10)}")
        f.write(f"- **High risk**: {overall_counts['High']} studies{chr(10)}")

    print(f"[ok] wrote {OUT_MD}")

if __name__ == "__main__":
    main()
