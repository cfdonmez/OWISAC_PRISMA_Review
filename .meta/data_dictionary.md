# Data Dictionary (v0.1)

Bu sözlük `data/` altındaki CSV/XLSX dosyaları için asgari gereksinimleri tanımlar.

## 1) screening_log.csv (CSV)
Zorunlu kolonlar:
- `record_id` (string) — tekil kimlik
- `source_db` (enum) — örn: IEEE Xplore | Scopus | Web of Science | arXiv
- `status` (enum) — { identified, deduplicated, screened, excluded_title_abs, fulltext_assessed, fulltext_excluded, included_qual, included_quant }
- `decided_by` (string) — kişi/ekip etiketi
- `decided_at` (datetime, ISO 8601) — örn: 2025-09-28T12:34:56Z

## 2) excluded_studies.csv (CSV)
Zorunlu kolonlar:
- `record_id` (string)
- Aşağıdakinden **biri** zorunlu:
  - `reason_code` (enum, önerilen): { out_of_scope, not_optical, no_opa_or_ris, no_nlos_or_turbulence, insufficient_methods, no_metrics, duplicate, not_substantial }
  - `reason` (free-text): serbest yazım (geçici). İleride `reason_code`'a normalize edilecek.
- Opsiyonel: `notes` (string)

## 3) included_studies.csv (CSV)
Zorunlu kolonlar:
- `record_id` (string)
- `citation` (string)
- `year` (int)
- Opsiyonel: `doi` (string), `dataset_url` (string)

> Not: Bu sözlük ilk sürümdür; gerekiyorsa alanlar genişletilecektir.
