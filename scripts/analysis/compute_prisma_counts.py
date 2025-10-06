#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compute_prisma_counts.py — PRISMA 2020 akış sayımları
Kaynaklar:
- search_log.csv → Records identified (DB/registers)
- dedup_log.csv → Duplicates removed
- automation_log.csv & screening_log.automation_flag → Removed by automation
- screening_log.csv → Records screened (TIAB), TIAB excluded, Full-text assessed
- excluded_studies.csv → Full-text excluded with reasons (+ breakdown)
- included_studies.csv → Studies included (toplam); screening_log → qual/quant kırılımı
Çıktı:
- results/prisma_counts.json
- results/snippets/prisma_counts.md
"""
import csv, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
SNIPPETS = RESULTS / "snippets"
RESULTS.mkdir(parents=True, exist_ok=True)
SNIPPETS.mkdir(parents=True, exist_ok=True)

def read_rows(name):
    p = DATA / name
    if not p.exists():
        return [], []
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        rdr = csv.DictReader(f)
        return rdr.fieldnames or [], list(rdr)

def as_int(x):
    try:
        return int(str(x).strip())
    except Exception:
        return 0

# ---- Veri çek ----
_, scr = read_rows("screening_log.csv")
_, exc = read_rows("excluded_studies.csv")
_, inc = read_rows("included_studies.csv")
_, srch = read_rows("search_log.csv")
_, dedup = read_rows("dedup_log.csv")
_, auto = read_rows("automation_log.csv")
_, fr = read_rows("fulltext_request_log.csv")  # opsiyonel

# ---- Identification ----
identified_total = sum(as_int(r.get("results_n")) for r in srch)

# ---- Removed before screening ----
duplicates_removed = len(dedup)

auto_drop_actions = {"screened_out", "exclude", "drop", "remove"}
automated_removed_ids = {
    (r.get("record_id") or "").strip()
    for r in auto
    if (r.get("action") or "").strip().lower() in auto_drop_actions
}
automated_removed_ids |= {
    (r.get("record_id") or "").strip()
    for r in scr
    if (r.get("automation_flag") or "").strip() == "screened_out"
}
automated_removed = len([rid for rid in automated_removed_ids if rid])

# ---- Screening (TIAB) ----
tiab_ids = {
    (r.get("record_id") or "").strip()
    for r in scr
    if (r.get("stage") or "").strip() == "tiab"
       or (r.get("status") or "").strip() == "excluded_title_abs"
}
records_screened_tiab = len([rid for rid in tiab_ids if rid])
records_excluded_tiab = sum(1 for r in scr if (r.get("status") or "").strip() == "excluded_title_abs")

# ---- Eligibility (Full-text) ----
fulltext_statuses = {"fulltext_assessed", "fulltext_excluded", "included_qual", "included_quant"}
fulltext_ids = {
    (r.get("record_id") or "").strip()
    for r in scr
    if (r.get("stage") or "").strip() == "fulltext" or (r.get("status") or "").strip() in fulltext_statuses
}
fulltexts_assessed = len([rid for rid in fulltext_ids if rid])

reports_sought = None
reports_not_retrieved = None
if fr:
    reports_sought = len(fr)
    not_retrieved_flags = {"no", "false", "0"}
    reports_not_retrieved = sum(
        1 for r in fr if (r.get("obtained") or "").strip().lower() in not_retrieved_flags
    )

# ---- Full-text excluded with reasons ----
fulltext_excluded_total = sum(1 for r in exc if (r.get("stage") or "").strip() == "fulltext")
reason_counts = {}
for r in exc:
    if (r.get("stage") or "").strip() != "fulltext":
        continue
    code = (r.get("reason_code") or "reason_unclassified").strip()
    reason_counts[code] = reason_counts.get(code, 0) + 1

# ---- Included ----
studies_included_total = len(inc)
included_qual = sum(1 for r in scr if (r.get("status") or "").strip() == "included_qual")
included_quant = sum(1 for r in scr if (r.get("status") or "").strip() == "included_quant")

out = {
    "identified": identified_total,
    "deduplicated": duplicates_removed,
    "screened": records_screened_tiab,
    "excluded_title_abs": records_excluded_tiab,
    "fulltext_assessed": fulltexts_assessed,
    "fulltext_excluded": reason_counts,
    "included_qual": included_qual,
    "included_quant": included_quant,
}

# Yaz: JSON
with (RESULTS / "prisma_counts.json").open("w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# Yaz: Markdown snippet
lines = []
lines.append("## PRISMA 2020 Flow — Counts")
lines.append(f"- Identified (DB/registers): **{identified_total}**")
lines.append(f"- Removed before screening — Duplicates: **{duplicates_removed}**, Automated: **{automated_removed}**")
lines.append(f"- Records screened (TIAB): **{records_screened_tiab}**")
lines.append(f"- Records excluded (TIAB): **{records_excluded_tiab}**")
lines.append(f"- Reports assessed for eligibility (full-text): **{fulltexts_assessed}**")
if reports_sought is not None:
    lines.append(f"- Reports sought for retrieval: **{reports_sought}**, Not retrieved: **{reports_not_retrieved or 0}**")
lines.append(f"- Full-text excluded with reasons: **{fulltext_excluded_total}**")
if reason_counts:
    lines.append("  - Reasons:")
    for k, v in sorted(reason_counts.items()):
        lines.append(f"    - {k}: **{v}**")
lines.append(f"- Studies included in review: **{studies_included_total}** (qual: {included_qual}, quant: {included_quant})")

with (SNIPPETS / "prisma_counts.md").open("w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("[ok] wrote results/prisma_counts.json and results/snippets/prisma_counts.md")
