from pathlib import Path
from datetime import datetime

BACKUP = Path("data/_backup")
DATA = Path("data")

def write(p: Path, content: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def backup_if_exists(src: Path):
    if src.exists():
        BACKUP.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        dst = BACKUP / f"{src.name}.bak.{ts}"
        dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
        print(f"[backup] {src} -> {dst}")

def main():
    # 1) varsa mevcut dosyaları yedekle
    for name in ["screening_log.csv","excluded_studies.csv","included_studies.csv"]:
        backup_if_exists(DATA / name)

    # 2) dummy dosyaları yaz
    write(DATA / "screening_log.csv", """record_id,source_db,status,decided_by,decided_at
R001,IEEE Xplore,identified,CD,2025-09-26T10:00:00Z
R001,IEEE Xplore,screened,CD,2025-09-26T10:10:00Z
R002,Scopus,identified,CD,2025-09-26T10:05:00Z
R002,Scopus,excluded_title_abs,CD,2025-09-26T10:20:00Z
R003,Web of Science,identified,CD,2025-09-26T10:15:00Z
R003,Web of Science,fulltext_assessed,CD,2025-09-26T10:45:00Z
R003,Web of Science,included_qual,CD,2025-09-26T11:00:00Z
""")

    write(DATA / "excluded_studies.csv", """record_id,reason,reason_code,notes
R002,"title/abstract not relevant to optical ISAC","out_of_scope",""
R004,"non-optical; no OPA or RIS",,to be normalized
""")

    write(DATA / "included_studies.csv", """record_id,citation,year,doi
R003,"Doe et al., 2023, Journal of Optical ISAC",2023,10.9999/dummy.doi
""")

    print("[ok] dummy data seeded under data/")

if __name__ == "__main__":
    main()
