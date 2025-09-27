import yaml
from pathlib import Path
from datetime import date

CFG = Path("config/review.yml")
OUT = Path("protocol/prisma_protocol.md")

def main():
    if not CFG.exists():
        raise SystemExit("Missing config/review.yml")

    cfg = yaml.safe_load(CFG.read_text())

    title = cfg.get("title", "")
    short_title = cfg.get("short_title", "")
    timeframe = cfg.get("timeframe", {})
    databases = [db["name"] for db in cfg.get("databases", [])]
    inclusion = cfg.get("eligibility", {}).get("inclusion", [])
    exclusion = cfg.get("eligibility", {}).get("exclusion", [])
    rqs = cfg.get("research_questions", [])

    lines = []
    lines.append(f"# Protocol for Systematic Review\n")
    lines.append(f"**Title:** {title}\n")
    lines.append(f"**Short title:** {short_title}\n")
    lines.append(f"**Date generated:** {date.today().isoformat()}\n")

    lines.append("## Timeframe\n")
    lines.append(f"- From: {timeframe.get('from')}\n- To: {timeframe.get('to')}\n")

    lines.append("## Databases\n")
    for db in databases:
        lines.append(f"- {db}")

    lines.append("\n## Eligibility Criteria\n### Inclusion\n")
    for inc in inclusion:
        lines.append(f"- {inc}")
    lines.append("\n### Exclusion\n")
    for exc in exclusion:
        lines.append(f"- {exc}")

    lines.append("\n## Research Questions\n")
    for rq in rqs:
        lines.append(f"- {rq}")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] Wrote protocol to {OUT}")

if __name__ == "__main__":
    main()
