import csv, sys
from pathlib import Path

SRC = Path("data/excluded_studies.csv")
OUT = Path("data/excluded_studies_normalized.csv")
BACKUP = Path("data/excluded_studies.backup.csv")

ALLOWED = {
    "out_of_scope","not_optical","no_opa_or_ris","no_nlos_or_turbulence",
    "insufficient_methods","no_metrics","duplicate","not_substantial"
}

def normalize_reason_text(txt: str):
    s = (txt or "").strip().lower()
    if not s: return None
    if "duplicate" in s or "dup." in s:
        return "duplicate"
    if "out of scope" in s:
        return "out_of_scope"
    if "non-optical" in s or "not optical" in s:
        return "not_optical"
    if "no opa" in s or "no ris" in s or "no optical ris" in s:
        return "no_opa_or_ris"
    if "no nlos" in s or "no turbulence" in s:
        return "no_nlos_or_turbulence"
    if "insufficient" in s or "method" in s:
        return "insufficient_methods"
    if "no metric" in s or "no key-physics" in s or "no key physics" in s:
        return "no_metrics"
    if "not substantial" in s:
        return "not_substantial"
    return None

def main():
    if not SRC.exists():
        sys.exit("Missing data/excluded_studies.csv")

    rows = []
    with SRC.open(newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        has_reason_code = "reason_code" in fieldnames
        if not has_reason_code:
            fieldnames = fieldnames + ["reason_code"]
        for r in reader:
            code = (r.get("reason_code") or "").strip().lower()
            if not code:
                code = normalize_reason_text(r.get("reason",""))
            # guardrail: only allow whitelisted codes
            if code and code not in ALLOWED:
                code = None
            r["reason_code"] = code or ""
            rows.append(r)

    OUT.parent.mkdir(exist_ok=True)
    with OUT.open("w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[ok] wrote normalized file: {OUT}")

    # küçük özet
    total = len(rows)
    filled = sum(1 for r in rows if r.get("reason_code"))
    print(f"[summary] rows: {total}, reason_code filled: {filled}, missing: {total - filled}")

    # İstersen in-place güncelleme için güvenli bir kopya bırak
    if not BACKUP.exists():
        SRC.replace(BACKUP)  # orijinali yedekle
        OUT.replace(SRC)     # normalize edilmişi ana dosyaya koy
        print(f"[ok] replaced original with normalized and saved backup: {BACKUP}")
    else:
        print("[info] backup exists; not replacing originals automatically. Review OUT file.")
        # Eğer BACKUP zaten varsa, bilinçli in-place yapmayı tercih et.
