#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
fix_consistency.py — PRISMA 2020 tutarlılık düzeltici (minimal, güvenli)

Yapar:
- excluded_studies(stage=fulltext)  → screening_log'a (fulltext_excluded) satırı ekler (yoksa).
- screening_log included_{qual,quant} → included_studies.csv'de yoksa UYARI üretir.
- search_log boş + TIAB tarama varsa → "Identified" için UYARI üretir.

Çıktı: results/consistency_fix_report.txt
"""

import csv, sys, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)
REPORT = RESULTS / "consistency_fix_report.txt"

def read_rows(name):
    p = DATA / name
    if not p.exists():
        return [], []
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        rdr = csv.DictReader(f)
        return (rdr.fieldnames or []), list(rdr)

def write_rows(name, fieldnames, rows):
    p = DATA / name
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

def ensure_cols(cols, need):
    for c in need:
        if c not in cols:
            cols.append(c)
    return cols

def iso_utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00","Z")

def main():
    rep = []
    # --- Dosyaları yükle ---
    sl_cols, sl = read_rows("screening_log.csv")
    ex_cols, ex = read_rows("excluded_studies.csv")
    inc_cols, inc = read_rows("included_studies.csv")
    se_cols, se = read_rows("search_log.csv")

    # Korumalı kolon listeleri
    sl_cols = ensure_cols(sl_cols or [], ["record_id","source_db","status","decided_by","decided_at","stage","decision","automation_flag"])
    ex_cols = ensure_cols(ex_cols or [], ["record_id","stage","reason_code","reason"])
    inc_cols = ensure_cols(inc_cols or [], ["record_id","citation","title","authors","year","venue","pub_type","peer_reviewed","doi","url"])

    # --- 1) Full-text excluded satırlarını garantiye al ---
    # screening_log'ta mevcut fulltext_excluded anahtarları
    existing_ft_excl = {
        (r.get("record_id","").strip(), r.get("stage","").strip(), r.get("status","").strip())
        for r in sl
    }
    # record_id -> source_db (varsa)
    source_hint = {}
    for r in sl:
        rid = (r.get("record_id") or "").strip()
        sdb = (r.get("source_db") or "").strip()
        if rid and sdb and rid not in source_hint:
            source_hint[rid] = sdb

    added = 0
    for r in ex:
        if (r.get("stage") or "").strip() != "fulltext":
            continue
        rid = (r.get("record_id") or "").strip()
        if not rid:
            continue
        key = (rid, "fulltext", "fulltext_excluded")
        if key in existing_ft_excl:
            continue
        # Yeni satır ekle
        newrow = {c: "" for c in sl_cols}
        newrow["record_id"]  = rid
        newrow["source_db"]  = source_hint.get(rid, "unknown")
        newrow["status"]     = "fulltext_excluded"
        newrow["stage"]      = "fulltext"
        newrow["decision"]   = "exclude"
        newrow["decided_by"] = "consistency-fixer"
        newrow["decided_at"] = iso_utc_now()
        sl.append(newrow)
        existing_ft_excl.add(key)
        added += 1

    if added:
        write_rows("screening_log.csv", sl_cols, sl)
        rep.append(f"[fix] screening_log.csv → fulltext_excluded eksikleri tamamlandı: +{added}")

    # --- 2) Included (qual/quant) ama included_studies.csv'de yoksa uyar ---
    included_statuses = {"included_qual","included_quant"}
    included_ids = { (r.get("record_id") or "").strip()
                     for r in sl if (r.get("status") or "").strip() in included_statuses }
    inc_ids = { (r.get("record_id") or "").strip() for r in inc }
    missing_inc_cards = sorted([rid for rid in included_ids - inc_ids if rid])

    if missing_inc_cards:
        rep.append("[warn] included_studies.csv eksik kart(lar): " + ", ".join(missing_inc_cards))
        rep.append("       → Bu kayıtlar için bibliyografik alanları doldurarak included_studies.csv’ye satır ekleyin.")

    # --- 3) Identified=0 ama tarama varsa uyar ---
    tiab_screened = any(((r.get("stage") or "").strip() == "tiab") or ((r.get("status") or "").strip() == "excluded_title_abs") for r in sl)
    if tiab_screened and not se:
        rep.append("[warn] search_log.csv boş; PRISMA-S’e göre 'Identified' kutusunu doldurmak için en az bir arama satırı ekleyin.")
        rep.append("       → Alanlar: search_run_id, source_db, platform, query_string, date_ran, results_n")

    # Yaz rapor
    if not rep:
        rep.append("No inconsistencies found or nothing to fix.")
    REPORT.write_text("\n".join(rep), encoding="utf-8")
    print(f"[ok] wrote {REPORT}")

if __name__ == "__main__":
    main()
