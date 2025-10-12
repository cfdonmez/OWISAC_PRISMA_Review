# Technical Context
**Repo layout (kritik yollar)**
- `scripts/analysis/*` → sayım/sentez üretimi
- `results/prisma_counts.json` → akış verisi
- `results/synthesis_tables/*.md` → tablolar
- `manuscript/` → ana makale bölümleri
- `data/` → screening/extraction/QA CSV’leri

**Automation notes**
- Python 3.10+ önerilir
- `pip install -r requirements.txt`
- Çalışan komut: `python scripts/run_pipeline.py`

**Data contracts**
- `included_studies.csv` min alanlar: record_id, title, venue, year, doi, scenario, hardware, metrics, tags
- QA bayrakları: `optical_ok`, `opa_ok`, `ris_ok`, `casc_ok`, `chan_ok`, `tech_ok`
