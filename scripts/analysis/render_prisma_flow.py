#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
render_prisma_flow.py — PRISMA 2020 akış diyagramını Mermaid ile üretir
Girdi : results/prisma_counts.json  (Adım 3'te üretildi)
Çıktı : docs/prisma_flow.md         (GitHub'da doğrudan görüntülenir)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COUNTS = ROOT / "results" / "prisma_counts.json"
DOCS = ROOT / "docs"
DOCS.mkdir(parents=True, exist_ok=True)
OUT = DOCS / "prisma_flow.md"

def n(x): 
    return 0 if x is None else int(x)

data = json.loads(COUNTS.read_text(encoding="utf-8"))

id_db = n(data["identified"]["db_registers_total"])
dup  = n(data["removed_before_screening"]["duplicates"])
auto = n(data["removed_before_screening"]["automated"])
oth  = n(data["removed_before_screening"]["other"])
scrn = n(data["screening"]["records_screened_tiab"])
tiab_ex = n(data["screening"]["records_excluded_tiab"])
elig = n(data["eligibility"]["fulltexts_assessed"])
sought = data["eligibility"].get("reports_sought_for_retrieval")
notret = data["eligibility"].get("reports_not_retrieved")
inc_total = n(data["included"]["studies_included_total"])
inc_qual  = n(data["included"]["qualitative"])
inc_quant = n(data["included"]["quantitative"])

# Full-text excluded reasons (opsiyonel)
reasons_md = ""
fx_total = 0
if Path("data/excluded_studies.csv").exists():
    # Adım 3 script'i toplamı JSON'a koyuyor; burada breakdown'u Markdown'a ekleyelim
    # JSON içindeki dağılımı saklamadıysan, bu satırı data/excluded_studies.csv'den de üretebilirsin.
    import csv
    from collections import Counter
    c = Counter()
    with (ROOT / "data" / "excluded_studies.csv").open(encoding="utf-8-sig", newline="") as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            if (r.get("stage") or "").strip() == "fulltext":
                c[(r.get("reason_code") or "reason_unclassified").strip()] += 1
    if c:
        fx_total = sum(c.values())
        reasons_md = "\n".join([f"    - {k}: **{v}**" for k, v in sorted(c.items())])

# Mermaid şablonu
mermaid = f"""```mermaid
flowchart TD
  A[Records identified<br/>(databases & registers)<br/>n={id_db}]:::box
  R[Records removed before screening<br/>duplicates: {dup}<br/>automated: {auto}<br/>other: {oth}]:::box
  S[Records screened (title/abstract)<br/>n={scrn}]:::box
  X[Records excluded (title/abstract)<br/>n={tiab_ex}]:::box
  E[Reports assessed for eligibility (full-text)<br/>n={elig}]:::box
  F[Reports excluded (full-text, with reasons){f"<br/>n={fx_total}" if fx_total else ""}]:::box
  I[Studies included in review<br/>total: {inc_total}<br/>qual: {inc_qual} | quant: {inc_quant}]:::box

  A --> R --> S -->|screened| E --> I
  S --> X
  E --> F
{"  RS[Reports sought for retrieval<br/>n="+str(sought)+"]:::box\n  E---RS" if sought is not None else ""}{"\n  RN[Reports not retrieved<br/>n="+str(notret)+"]:::box\n  RS --> RN" if notret is not None else ""}

  classDef box fill:#f9f9f9,stroke:#999,stroke-width:1px,color:#000;
```"""

md = [
  "# PRISMA 2020 Flow — Diagram",
  "",
  mermaid,
  "",
  "## Full-text exclusion reasons",
  (reasons_md if reasons_md else "_No full-text exclusions recorded or reasons not available._")
]
OUT.write_text("\n".join(md), encoding="utf-8")
print(f"[ok] wrote {OUT}")
