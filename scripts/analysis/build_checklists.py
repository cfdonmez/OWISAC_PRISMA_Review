#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_checklists.py — PRISMA-2020 (27) ve PRISMA-S (16) için auto-fill checklist + methods boilerplate
Girdiler: data/*.csv, results/prisma_counts.json
Çıktılar:
  - docs/checklists/PRISMA_2020_checklist.md
  - docs/checklists/PRISMA_S_checklist.md
  - results/snippets/methods_boilerplate.md
"""

import csv, json, statistics
from collections import defaultdict, Counter
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
DOCS = ROOT / "docs" / "checklists"
DOCS.mkdir(parents=True, exist_ok=True)
RESULTS.mkdir(parents=True, exist_ok=True)

def read_csv(name):
    p = DATA / name
    if not p.exists(): return [], []
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        rdr = csv.DictReader(f)
        rows = list(rdr)
        return rdr.fieldnames or [], rows

def read_json(p):
    if not p.exists(): return {}
    return json.loads(p.read_text(encoding="utf-8"))

def uniq(seq):
    out, seen = [], set()
    for x in seq:
        if x and x not in seen:
            out.append(x); seen.add(x)
    return out

def to_date(s):
    try:
        return datetime.fromisoformat(s.replace("Z","+00:00"))
    except Exception:
        return None

# ---- Veri çek
_, search = read_csv("search_log.csv")
_, screening = read_csv("screening_log.csv")
_, included = read_csv("included_studies.csv")
_, automation = read_csv("automation_log.csv")
counts = read_json(RESULTS / "prisma_counts.json")

# ---- PRISMA-S özetleri
srcs = uniq([ (r.get("source_db") or "").strip() for r in search ])
plats = uniq([ (r.get("platform") or "").strip() for r in search ])
queries = uniq([ (r.get("query_string") or "").strip() for r in search ])
dates = sorted([ d for d in (to_date((r.get("date_ran") or "").strip()) for r in search) if d is not None ])
n_res = [ int(r.get("results_n") or 0) for r in search if (r.get("results_n") or "").strip() != "" ]
results_total = sum(n_res)
date_span = (dates[0].date().isoformat(), dates[-1].date().isoformat()) if dates else (None, None)

# ---- Seçim süreci (hakem/otomasyon ipuçları)
# Not: reviewer sayısını doğrudan veri seti sağlamadığı için sabit/varsayılan "not reported" bırakıyoruz.
auto_tools = uniq([ (r.get("tool") or "").strip() for r in automation ])
auto_actions = Counter([ (r.get("action") or "").strip().lower() for r in automation ])

# ---- Included çalışmaların kısa özeti (başlık/yıl/venue)
inc_years = [ int((r.get("year") or 0)) for r in included if (r.get("year") or "").strip().isdigit() ]
inc_venues = Counter([ (r.get("venue") or "").strip() for r in included if (r.get("venue") or "").strip() ])
inc_year_span = (min(inc_years), max(inc_years)) if inc_years else (None, None)
inc_n = len(included)

# ---- Methods boilerplate üret
boiler = []
boiler.append("## Methods (Automated Boilerplate)")
boiler.append("")
boiler.append("### Information Sources and Search Strategy (PRISMA-S)")
if srcs:
    boiler.append(f"- Databases/registers: {', '.join(srcs)}.")
if plats:
    boiler.append(f"- Interfaces/platforms: {', '.join(plats)}.")
if queries:
    boiler.append(f"- Representative queries (subset):\n  - " + "\n  - ".join(queries[:5]))
if date_span != (None, None):
    boiler.append(f"- Search dates: {date_span[0]} to {date_span[1]}.")
boiler.append(f"- Total results reported by sources: {results_total}.")

boiler.append("")
boiler.append("### Selection Process")
boiler.append("- Title/abstract (TIAB) and full-text screening logged in `data/screening_log.csv` with ISO-8601 timestamps.")
if auto_tools:
    boiler.append(f"- Automation used: {', '.join(auto_tools)}.")
if auto_actions:
    boiler.append(f"- Automation actions summary: " + ", ".join(f"{k}={v}" for k,v in auto_actions.items() if k))

boiler.append("")
boiler.append("### Eligibility, Exclusions, and Included Studies")
boiler.append(f"- Records screened (TIAB): {counts.get('screening',{}).get('records_screened_tiab',0)}; excluded at TIAB: {counts.get('screening',{}).get('records_excluded_tiab',0)}.")
boiler.append(f"- Reports assessed for eligibility (full-text): {counts.get('eligibility',{}).get('fulltexts_assessed',0)}; full-text excluded with reasons: see `data/excluded_studies.csv`.")
boiler.append(f"- Studies included in review: {counts.get('included',{}).get('studies_included_total',0)} (qual={counts.get('included',{}).get('qualitative',0)}, quant={counts.get('included',{}).get('quantitative',0)}).")
if inc_year_span != (None, None):
    boiler.append(f"- Included study years span: {inc_year_span[0]}–{inc_year_span[1]}.")
if inc_venues:
    topv = ", ".join([f"{v}× {k}" for k,v in inc_venues.most_common(5)])
    boiler.append(f"- Venues (top): {topv}.")

(RESULTS / "snippets").mkdir(parents=True, exist_ok=True)
(RESULTS / "snippets" / "methods_boilerplate.md").write_text("\n".join(boiler), encoding="utf-8")

# ---- PRISMA-S checklist (16 maddeye göre alanlar)
# Bu tablo, veri tabanlı satırları otomatik doldurur; boşsa TODO bırakır.
ps_lines = []
ps_lines.append("# PRISMA-S Checklist (Auto-filled Draft)")
ps_lines.append("")
ps_lines.append("| Item | Reporting Field | Auto-fill |")
ps_lines.append("|---|---|---|")
ps_map = {
  "S1": ("Information sources (databases/registers)", ", ".join(srcs) or "TODO"),
  "S2": ("Interfaces/platforms", ", ".join(plats) or "TODO"),
  "S3": ("Full search strategies (queries)", "; ".join(queries[:8]) or "TODO"),
  "S4": ("Limits/filters used", "TODO"),
  "S5": ("Search dates", f"{date_span[0]} to {date_span[1]}" if date_span!=(None,None) else "TODO"),
  "S6": ("Search results (per source)", "; ".join([f'{(r.get("source_db") or "").strip()}={(r.get("results_n") or 0)}' for r in search]) or '0'),
  "S7": ("Deduplication method", "See data/dedup_log.csv (method column)"),
  "S8": ("Update searches / reruns", "TODO"),
  "S9": ("Grey literature/other sources", "TODO"),
  "S10": ("Peer review of the search", "TODO"),
  "S11": ("Searcher qualifications", "TODO"),
  "S12": ("Use of automation in searching", ", ".join(auto_tools) or "None reported"),
  "S13": ("Data management (records)", "Repo CSV schema; ISO-8601 timestamps"),
  "S14": ("Citation searching / handsearching", "TODO"),
  "S15": ("Translations / language handling", "TODO"),
  "S16": ("Protocol/registration for searching", "TODO (e.g., OSF/PROSPERO ref)")
}
for k,(label,val) in ps_map.items():
    ps_lines.append(f"| {k} | {label} | {val} |")
(DOCS / "PRISMA_S_checklist.md").write_text("\n".join(ps_lines), encoding="utf-8")

# ---- PRISMA-2020 checklist (27 madde) — auto-fill alanları ve TODO’lar
p20 = []
p20.append("# PRISMA-2020 Checklist (Auto-filled Draft)")
p20.append("")
p20.append("| Item | Section/Topic | Auto-filled Content / TODO |")
p20.append("|---|---|---|")
def add(i, sec, val): p20.append(f"| {i} | {sec} | {val} |")

# Title/Abstract
add("1", "Title", "Systematic review/meta-analysis — TODO (ensure identification as SR).")
add("2", "Abstract", "Use PRISMA 2020 abstract checklist — TODO.")

# Introduction
add("3", "Rationale", "Context/motivation — TODO.")
add("4", "Objectives", "Structured question(s) — TODO.")

# Methods
add("5", "Eligibility criteria", "Inclusion/exclusion rules; link to data dictionary — TODO.")
add("6", "Information sources", (", ".join(srcs) if srcs else "TODO") + ("; interfaces: " + ", ".join(plats) if plats else ""))
add("7", "Search strategy", ("Representative queries: " + "; ".join(queries[:8])) if queries else "TODO")
add("8", "Selection process", f"Screening logged in CSV (TIAB & full-text); automation: {', '.join(auto_tools) if auto_tools else 'none'}; decisions in `screening_log.csv`.")
add("9", "Data collection process", "Extraction forms/tools — TODO.")
add("10", "Data items", "Outcomes/variables — TODO.")
add("11", "Study risk of bias assessment", "Tool/criteria — TODO.")
add("12", "Effect measures", "For each outcome — TODO.")
add("13", "Synthesis methods (a-f)", "Modeling/heterogeneity/sensitivity — TODO.")
add("14", "Reporting bias assessment", "Publication bias/small-study — TODO.")
add("15", "Certainty of evidence", "e.g., GRADE — TODO.")

# Results
add("16", "Study selection", f"Flow counts: TIAB screened={counts.get('screening',{}).get('records_screened_tiab',0)}, TIAB excluded={counts.get('screening',{}).get('records_excluded_tiab',0)}, full-text assessed={counts.get('eligibility',{}).get('fulltexts_assessed',0)}, included={counts.get('included',{}).get('studies_included_total',0)}.")
add("17", "Study characteristics", f"{inc_n} included; year span {inc_year_span[0]}–{inc_year_span[1]} — see `included_studies.csv`.")
add("18", "Risk of bias in studies", "Summary — TODO.")
add("19", "Results of individual studies", "Per-study metrics — TODO.")
add("20", "Results of syntheses", "Overall effects/heterogeneity — TODO.")
add("21", "Reporting biases", "Assessment — TODO.")
add("22", "Certainty of evidence", "GRADE/other — TODO.")

# Discussion
add("23", "Discussion", "Summary/limitations/implications — TODO.")

# Other information
add("24", "Registration and protocol", "OSF/PROSPERO ID — TODO.")
add("25", "Support", "Funding — TODO.")
add("26", "Competing interests", "Declarations — TODO.")
add("27", "Availability of data, code and other materials", "Repo links to data/code — provide URLs — TODO.")

(DOCS / "PRISMA_2020_checklist.md").write_text("\n".join(p20), encoding="utf-8")

print("[ok] wrote:",
      DOCS / "PRISMA_S_checklist.md",
      DOCS / "PRISMA_2020_checklist.md",
      RESULTS / "snippets" / "methods_boilerplate.md", sep="\n")
