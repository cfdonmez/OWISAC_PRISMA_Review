#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"

def read_rows(p):
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        rdr = csv.DictReader(f)
        return rdr.fieldnames or [], list(rdr)

def write_rows(p, fieldnames, rows):
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

def ensure_cols(cols, need):
    for c in need:
        if c not in cols:
            cols.append(c)
    return cols

def fix_screening():
    p = DATA / "screening_log.csv"
    if not p.exists(): return
    cols, rows = read_rows(p)
    cols = ensure_cols(cols, ["stage","decision","automation_flag"])
    for r in rows:
        st = (r.get("status") or "").strip()
        stage = (r.get("stage") or "").strip()
        decision = (r.get("decision") or "").strip()

        if st == "excluded_title_abs":
            if not stage: r["stage"] = "tiab"
            if not decision: r["decision"] = "exclude"

        elif st == "fulltext_assessed":
            if not stage: r["stage"] = "fulltext"
            # decision isteğe bağlı: boş kalabilir

        elif st in {"included_qual","included_quant"}:
            if not stage: r["stage"] = "fulltext"
            if not decision: r["decision"] = "include"

    write_rows(p, cols, rows)

def fix_excluded():
    p = DATA / "excluded_studies.csv"
    if not p.exists(): return
    cols, rows = read_rows(p)
    cols = ensure_cols(cols, ["stage"])
    for r in rows:
        if not (r.get("stage") or "").strip():
            r["stage"] = "fulltext"
    write_rows(p, cols, rows)

def main():
    fix_screening()
    fix_excluded()
    print("[ok] patched screening_log.csv & excluded_studies.csv")

if __name__ == "__main__":
    main()
