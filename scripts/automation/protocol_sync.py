import yaml
from pathlib import Path
from datetime import date

CFG = Path("config/review.yml")
OUT = Path("protocol/prisma_protocol.md")

def _safe_list(x):
    return x if isinstance(x, list) else []

def main():
    if not CFG.exists():
        raise SystemExit("Missing config/review.yml")

    cfg = yaml.safe_load(CFG.read_text())

    title = cfg.get("title", "")
    short_title = cfg.get("short_title", "")
    timeframe = cfg.get("timeframe", {}) or {}
    regs = cfg.get("registrations", {}) or {}
    databases = cfg.get("databases", []) or []
    search = cfg.get("search", {}) or {}
    inclusion = _safe_list(cfg.get("eligibility", {}).get("inclusion"))
    exclusion = _safe_list(cfg.get("eligibility", {}).get("exclusion"))
    rqs = _safe_list(cfg.get("research_questions"))
    core_fields = _safe_list(cfg.get("extraction_core_fields"))

    lines = []
    lines.append("# Protocol for Systematic Review\n")
    lines.append(f"**Title:** {title}\n")
    lines.append(f"**Short title:** {short_title}\n")
    lines.append(f"**Date generated:** {date.today().isoformat()}\n")

    # Registration
    lines.append("## Protocol & Registration\n")
    osf = regs.get("osf") or "<add OSF link/DOI>"
    prospero = regs.get("prospero") or "<add PROSPERO ID>"
    lines.append(f"- OSF: {osf}")
    lines.append(f"- PROSPERO: {prospero}\n")

    # Timeframe
    lines.append("## Timeframe\n")
    lines.append(f"- From: {timeframe.get('from')}\n- To: {timeframe.get('to')}\n")

    # Databases
    lines.append("## Information Sources (Databases & Interfaces)\n")
    for db in databases:
        name = db.get("name", "")
        iface = db.get("interface", "")
        lines.append(f"- {name} (interface: {iface})")
    lines.append("")

    # Search Strategy
    lines.append("## Search Strategy\n")
    qlist = _safe_list(search.get("queries"))
    if qlist:
        lines.append("### Query Strings")
        for q in qlist:
            label = q.get("label", "")
            qs = q.get("string", "")
            lines.append(f"- **{label}**: `{qs}`")
        lines.append("")
    grey = search.get("grey_literature", False)
    last_ran = search.get("last_ran", "")
    lines.append(f"- Grey literature: {'yes' if grey else 'no'}")
    lines.append(f"- Last search run: {last_ran or '<add ISO datetime>'}\n")

    # Eligibility
    lines.append("## Eligibility Criteria\n### Inclusion\n")
    for inc in inclusion:
        lines.append(f"- {inc}")
    lines.append("\n### Exclusion\n")
    for exc in exclusion:
        lines.append(f"- {exc}")
    lines.append("")

    # Research Questions
    lines.append("## Research Questions\n")
    for rq in rqs:
        lines.append(f"- {rq}")
    lines.append("")

    # Data Extraction Core Fields (helps align templates)
    if core_fields:
        lines.append("## Core Data Items for Extraction\n")
        for f in core_fields:
            lines.append(f"- {f}")
        lines.append("")

    # Footer
    lines.append("> This protocol is **auto-generated** from `config/review.yml` (SSOT). Edit the YAML to update this document.\n")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] Wrote protocol to {OUT}")

if __name__ == "__main__":
    main()