from pathlib import Path
p = Path("scripts/analysis/rob_summary.py")
if p.exists():
    s = p.read_text(encoding="utf-8")
    s = s.replace("rob_summary.png", "results/figures/rob_summary.png")
    p.write_text(s, encoding="utf-8")
    print("[updated] rob_summary.py -> results/figures/rob_summary.png")
else:
    print("[skip] scripts/analysis/rob_summary.py not found")
