from pathlib import Path
p = Path("scripts/analysis/make_prisma_flow.py")
s = p.read_text(encoding="utf-8")
s = s.replace("prisma_flow.png", "results/figures/prisma_flow.png")
p.write_text(s, encoding="utf-8")
print("[updated] make_prisma_flow.py -> results/figures/prisma_flow.png")
