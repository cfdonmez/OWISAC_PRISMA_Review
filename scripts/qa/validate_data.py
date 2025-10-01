#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_data.py — PRISMA-2020 / PRISMA-S uyumlu temel şema denetimi
Çıktı: results/qa_data_report.txt
"""

import csv, re, sys
from pathlib import Path
from datetime import datetime

# Karar gerektiren statüler
decision_required_statuses = {
    "excluded_title_abs","fulltext_excluded","included_qual","included_quant"
}
# 'stage' gerektiren (ama karar zorunlu olmayanı da içeren) statüler
stage_required_statuses = decision_required_statuses | {"fulltext_assessed"}

ROOT = Path(__file__).resolve().parents[2] if (Path(__file__).name == "validate_data.py") else Path.cwd()
DATA = ROOT / "data"
RESULTS = ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

REPORT = RESULTS / "qa_data_report.txt"

ISO_TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+\-]\d{2}:\d{2})?$")
DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$", re.I)

OK = []
ERR = []

def is_iso8601(s: str) -> bool:
    if not s or not ISO_TS_RE.match(s.strip()):
        return False
    try:
        # fromisoformat supports "+HH:MM"; replace Z with +00:00
        datetime.fromisoformat(s.replace("Z", "+00:00"))
        return True
    except Exception:
        return False

def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rdr = csv.DictReader(f)
        rows = list(rdr)
    return rdr.fieldnames or [], rows

def require_columns(file, cols, required):
    missing = [c for c in required if c not in cols]
    if missing:
        ERR.append(f"[{file}] Eksik zorunlu kolon(lar): {missing}")

def check_enum(file, rows, col, allowed):
    for i, r in enumerate(rows, 2):
        v = (r.get(col) or "").strip()
        if v and v not in allowed:
            ERR.append(f"[{file}:{i}] '{col}' için geçersiz değer: '{v}' (izin verilen: {sorted(allowed)})")

def check_bool(file, rows, col):
    ALLOWED = {"true","false","1","0","yes","no",""}
    for i, r in enumerate(rows, 2):
        v = (r.get(col) or "").strip().lower()
        if v not in ALLOWED:
            ERR.append(f"[{file}:{i}] '{col}' bool bekleniyor (true/false/1/0/yes/no) → '{v}'")

def check_int(file, rows, col):
    for i, r in enumerate(rows, 2):
        v = (r.get(col) or "").strip()
        if v and not re.fullmatch(r"[+-]?\d+", v):
            ERR.append(f"[{file}:{i}] '{col}' tamsayı bekleniyor → '{v}'")

def check_iso_ts(file, rows, col):
    for i, r in enumerate(rows, 2):
        v = (r.get(col) or "").strip()
        if v and not is_iso8601(v):
            ERR.append(f"[{file}:{i}] '{col}' ISO-8601 bekleniyor (YYYY-MM-DDThh:mm:ssZ/+hh:mm) → '{v}'")

def check_unique(file, rows, col):
    seen = {}
    for i, r in enumerate(rows, 2):
        v = (r.get(col) or "").strip()
        if not v:
            ERR.append(f"[{file}:{i}] '{col}' boş olamaz")
            continue
        if v in seen:
            ERR.append(f"[{file}:{i}] '{col}' tekil olmalı; tekrar: '{v}' (ilk satır: {seen[v]})")
        else:
            seen[v] = i

def check_any_present(file, rows, col_a, col_b, label=""):
    for i, r in enumerate(rows, 2):
        a = (r.get(col_a) or "").strip()
        b = (r.get(col_b) or "").strip()
        if not a and not b:
            tag = f" '{label}'" if label else ""
            ERR.append(f"[{file}:{i}] En az biri dolu olmalı{tag}: {col_a} | {col_b}")

def check_screening_composite_key(file, rows):
    """
    1) Aynı (record_id, stage, status) satırı birden fazla olamaz  → tam duplike satırı yakala
    2) TIAB aşamasında en fazla bir nihai karar (excluded_title_abs) olmalı
    3) FULLTEXT aşamasında nihai kararlardan (fulltext_excluded | included_qual | included_quant) en fazla BİRİ olmalı
       'fulltext_assessed' ile birlikte bulunması meşrudur.
    """
    terminal_tiab = {"excluded_title_abs"}
    terminal_full = {"fulltext_excluded", "included_qual", "included_quant"}

    seen_exact = {}                 # (rid, stage, status) → line
    tiab_decisions = {}             # rid → [(status, line)]
    fulltext_decisions = {}         # rid → [(status, line)]

    for i, r in enumerate(rows, 2):
        rid = (r.get("record_id") or "").strip()
        stage = (r.get("stage") or "").strip()
        status = (r.get("status") or "").strip()

        if not rid:
            ERR.append(f"[{file}:{i}] 'record_id' boş olamaz")
            continue

        # 1) Tam duplike satırı yakala
        key_exact = (rid, stage, status)
        if key_exact in seen_exact:
            first = seen_exact[key_exact]
            ERR.append(f"[{file}:{i}] aynı kayıt tekrarlandı: {key_exact} (ilk satır: {first})")
        else:
            seen_exact[key_exact] = i

        # 2–3) Aşama bazlı nihai karar sayımı
        if stage == "tiab" and status in terminal_tiab:
            tiab_decisions.setdefault(rid, []).append((status, i))

        if stage == "fulltext" and status in terminal_full:
            fulltext_decisions.setdefault(rid, []).append((status, i))

    # TIAB: birden fazla nihai karar olamaz
    for rid, items in tiab_decisions.items():
        if len(items) > 1:
            lines = [str(line) for _, line in items]
            statuses = [st for st, _ in items]
            ERR.append(f"[{file}] TIAB aşamasında (record_id={rid}) birden fazla nihai karar var: {statuses} (satırlar: {', '.join(lines)})")

    # FULLTEXT: birden fazla nihai karar olamaz
    for rid, items in fulltext_decisions.items():
        if len(items) > 1:
            lines = [str(line) for _, line in items]
            statuses = [st for st, _ in items]
            ERR.append(f"[{file}] FULLTEXT aşamasında (record_id={rid}) birden fazla nihai karar var: {statuses} (satırlar: {', '.join(lines)})")

def check_conditional_stage_decision(file, rows, stage_enum, decision_enum,
                                     stage_required_statuses, decision_required_statuses):
    for i, r in enumerate(rows, 2):
        status = (r.get("status") or "").strip()
        stage = (r.get("stage") or "").strip()
        decision = (r.get("decision") or "").strip()

        if status in stage_required_statuses:
            if not stage or stage not in stage_enum:
                ERR.append(f"[{file}:{i}] '{status}' için 'stage' {sorted(stage_enum)} olmalı")

        if status in decision_required_statuses:
            if not decision or decision not in decision_enum:
                ERR.append(f"[{file}:{i}] '{status}' için 'decision' {sorted(decision_enum)} olmalı")

def run():
    # --- Şema tanımları ---
    status_enum = {
        "identified","deduplicated","screened","excluded_title_abs",
        "fulltext_assessed","fulltext_excluded","included_qual","included_quant"
    }
    stage_enum = {"tiab","fulltext"}
    decision_enum = {"include","exclude","unsure"}
    reason_enum = {
        "out_of_scope","not_optical","no_opa_or_ris","no_nlos_or_turbulence",
        "insufficient_methods","no_metrics","duplicate","not_substantial",
        "unobtainable_fulltext","retracted","wrong_pub_type"
    }
    pub_type_enum = {"journal","conference","preprint","thesis","other"}
    automation_flag_enum = {"screened_out","prioritized","none"}

    files = [
        ("screening_log.csv", {
            "required": ["record_id","source_db","status","decided_by","decided_at"],
            "checks": [
                # Not: tekillik kontrolü composite yapılacak; aşağıda özel işliyoruz
                ("iso","decided_at"),
                ("enum","status", status_enum),
                # stage/decision yalnızca "karar statüleri" için zorunlu
                ("conditional_stage_decision", None),
                ("enum_opt","automation_flag", automation_flag_enum),
            ]
        }),
        ("excluded_studies.csv", {
            "required": ["record_id","stage"],
            "checks": [
                ("unique","record_id"),
                ("enum","stage", stage_enum),
                ("any","reason_code","reason","dışlama gerekçesi"),
                ("enum_opt","reason_code", reason_enum),
            ]
        }),
        ("included_studies.csv", {
            "required": ["record_id","citation","title","authors","year","venue","pub_type","peer_reviewed","doi","url"],
            "checks": [
                ("unique","record_id"),
                ("int","year"),
                ("enum","pub_type", pub_type_enum),
                ("bool","peer_reviewed"),
                ("any","doi","url","izlenebilirlik (DOI/URL)"),
            ]
        }),
        ("search_log.csv", {
            "required": ["search_run_id","source_db","platform","query_string","date_ran","results_n"],
            "checks": [
                ("unique","search_run_id"),
                ("iso","date_ran"),
                ("int","results_n"),
            ]
        }),
        ("dedup_log.csv", {
            "required": ["primary_record_id","merged_record_ids","method","decided_by","decided_at"],
            "checks": [
                ("iso","decided_at"),
            ]
        }),
        ("automation_log.csv", {
            "required": ["record_id","tool","version","threshold","action"],
            "checks": [
                ("int","threshold"),  # eğer yüzde/float kullanıyorsan burada değiştir
            ]
        }),
    ]

    lines = []
    total_rows = 0

    for fname, spec in files:
        path = DATA / fname
        if not path.exists():
            ERR.append(f"[{fname}] Dosya yok: {path}")
            continue
        cols, rows = read_csv(path)
        total_rows += len(rows)
        require_columns(fname, cols, spec["required"])

        # satır denetimleri
        for typ, *args in spec["checks"]:
            if typ == "unique":
                check_unique(fname, rows, args[0])
            elif typ == "enum":
                check_enum(fname, rows, args[0], args[1])
            elif typ == "enum_opt":
                c, allowed = args
                # sadece değer varsa kontrol et
                check_enum(fname, rows, c, allowed)
            elif typ == "bool":
                check_bool(fname, rows, args[0])
            elif typ == "int":
                check_int(fname, rows, args[0])
            elif typ == "iso":
                check_iso_ts(fname, rows, args[0])
            elif typ == "any":
                check_any_present(fname, rows, args[0], args[1], args[2])

        # Özel kontroller için hook
        if fname == "screening_log.csv":
            check_screening_composite_key(fname, rows)
            check_conditional_stage_decision(
                fname, rows, stage_enum, decision_enum,
                stage_required_statuses, decision_required_statuses
            )

        lines.append(f"- {fname}: {len(rows)} satır, {len(cols)} kolon")

        # DOI biçimi ipucu (opsiyonel uyarı)
        if fname == "included_studies.csv" and "doi" in cols:
            for i, r in enumerate(rows, 2):
                d = (r.get("doi") or "").strip()
                if d and not DOI_RE.match(d):
                    ERR.append(f"[{fname}:{i}] DOI şüpheli biçim: '{d}' (10.xxxx/...)")

    # Rapor yaz
    with REPORT.open("w", encoding="utf-8") as f:
        f.write("# QA Data Report (schema)\n")
        f.write("\n## Özet\n")
        f.write("\n".join(lines) + "\n")
        f.write(f"\nToplam satır: {total_rows}\n")
        if ERR:
            f.write("\n## Hatalar / Uyarılar\n")
            for e in ERR:
                f.write(f"- {e}\n")
        else:
            f.write("\n✅ Şema denetimi: Hata bulunmadı.\n")

    msg = f"[ok] wrote report to {REPORT}"
    print(msg)

if __name__ == "__main__":
    run()
