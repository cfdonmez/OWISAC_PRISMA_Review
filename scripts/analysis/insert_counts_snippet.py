import json
from pathlib import Path

SRC = Path("results/prisma_counts.json")
OUT = Path("results/snippets/prisma_counts.md")

def main():
    if not SRC.exists():
        raise SystemExit("Missing results/prisma_counts.json (run pipeline first)")

    data = json.loads(SRC.read_text(encoding="utf-8"))
    ident  = data.get("identified", 0)
    scr    = data.get("screened", 0)
    fta    = data.get("fulltext_assessed", 0)
    ex_ta  = data.get("excluded_title_abs", 0)
    inq    = data.get("included_qual", 0)
    inqt   = data.get("included_quant", 0)
    reasons = data.get("fulltext_excluded", {})

    lines = []
    lines.append("### PRISMA Counts Summary (auto)")
    lines.append("")
    lines.append(f"We identified **{ident}** records; screened **{scr}**; assessed **{fta}** full texts;")
    lines.append(f"excluded **{ex_ta}** at title/abstract; and included **{inq}** qualitatively and **{inqt}** quantitatively.")
    if reasons:
        lines.append("")
        lines.append("**Full-text exclusion reasons:**")
        for r, n in sorted(reasons.items(), key=lambda x: (-x[1], x[0])):
            lines.append(f"- {r} — {n}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[ok] wrote {OUT}")

if __name__ == "__main__":
    main()
