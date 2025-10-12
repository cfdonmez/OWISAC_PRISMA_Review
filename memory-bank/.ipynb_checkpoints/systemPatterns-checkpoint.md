# System Patterns (task şablonları)

## Pattern: PRISMA Sayım Güncelle
**Trigger:** New/removed studies
**Steps:**
1) Run: `python scripts/run_pipeline.py`
2) Read: `results/prisma_counts.json`
3) Update snippet → `results/snippets/prisma_counts.md`
4) Commit: `chore(prisma): update counts`

## Pattern: Sentez Tablosu Üret
**Trigger:** Yeni etiketler/filtreler
**Steps:**
1) `python scripts/analysis/synth_build_subgroups.py`
2) `python scripts/analysis/synth_build_architectures.py`
3) Tabloları `results/synthesis_tables/` altına yerleştir
4) Manuscript’e include

## Pattern: Dahil/Haric Gerekçeleri
**Steps:**
1) `data/screening_log.csv` → QA
2) Eksik alan → yazarlarla iletişim (gerekirse)
3) `excluded_studies.csv` gerekçeleri kısa, tutarlı

## Pattern: DOI Doldurma
**Steps:**
1) `scripts/utility/fill_doi_plus_semantics.py` ile başlık+yazar → DOI
2) Çatallanma: Crossref→arXiv→OpenAlex→S2
3) Kayıt: `data/extraction/*.csv` ilgili sütun
