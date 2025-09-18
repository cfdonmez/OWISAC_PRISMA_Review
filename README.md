# A Systematic Review of Cascaded OPA–RIS Architectures for NLoS Optical Wireless ISAC
**Project Status:** Ongoing | **Last Updated:** 2025-09-18

[![PRISMA 2020 Compliant](https://img.shields.io/badge/PRISMA-2020-blue.svg)](https://www.prisma-statement.org/)
[![Protocol Registered](https://img.shields.io/badge/OSF-Registered-informational.svg)](#registration)
[![Open Data](https://img.shields.io/badge/Open%20Data-CC--BY--4.0-success.svg)](#contribution--open-science-statement)
[![Code License](https://img.shields.io/badge/Code-MIT-lightgrey.svg)](#contribution--open-science-statement)

---

## Overview & Rationale
This repository documents a systematic review, conducted in accordance with **PRISMA 2020**, of cascaded **Optical Phased Array (OPA)**–**Reconfigurable Intelligent Surface (RIS)** architectures for **non-line-of-sight (NLoS)** optical wireless **integrated sensing and communications (ISAC)**. We synthesize methods and results across five technical pillars:
1. **Wigner-Uzayı Ortak Işın Biçimleme (WD-JD)**  
   Uzay \((x,y)\) ve uzaysal frekans \((f_x,f_y)\) bölgelerinde eşzamanlı odak/kontrast optimizasyonu; Wigner dağılımı tabanlı amaç fonksiyonları ve separable/FFT hızlandırma.

2. **Kanal Edinimi & RIS-Kodlu Faz Geri-Kazanımı (RC-PR-T)**  
   **Sadece şiddet (intensity-only)** ölçümlerle, NLoS + türbülans altında RIS faz maskeleri kullanarak faz/topoloji çıkarımı; başlangıç (spectral/Wirtinger) ve yakınsama stratejileri.

3. **Grating Lobe Baskılama & Aperiodik (Blue-Noise) RIS Tasarımı (BN-RIS)**  
   Poisson-disk/blue-noise yerleşimleri, hibrit ızgara + jitter; yan lob tepe değeri (PSL) ve yan güç dağılımının metrikleştirilmesi; aliasing’e karşı dayanım.

4. **Kolmogorov Türbülansına Karşı Robust Ön-Şekillendirme (RPB-Kol)**  
   \(\mathbb{E}[I]\)–\(\mathrm{Var}[I]\)–ROI-dışı güç çoklu hedefleri; \(C_n^2, r_0,\) Rytov değişkenleriyle senaryo süpürmeleri ve hassasiyet analizleri.

5. **Donanım-Farkındalıklı Uygulama & Kalibrasyon (HW-Q/CTRL)**  
   Faz-bit sınırlamaları, eleman gecikmesi/tepki süresi, optik verim/kayıplar, OPA↔RIS hizalama ve **scan-rate/latency** etkileri; kuantizasyon-farkındalıklı optimizasyon, ölçüm kalibrasyonu ve kontrol döngüsü bütünleştirme.

- **Last search completed:** 2025-09-17  
- **Planned update cadence:** Quarterly (or on major field releases)

### Registration
This review is preregistered at the **Open Science Framework (OSF)**.  
OSF link/DOI: _to be inserted_  
All protocol deviations will be logged in `/protocol/AMENDMENTS.md`.


---

## 2. Research Protocol (PRISMA-P)
Our protocol was designed and deposited prior to review initiation as recommended by PRISMA-P.  
**Protocol access:** See [`/protocol/prisma_protocol.md`](./protocol/prisma_protocol.md) and [checklist](https://www.prisma-statement.org/PRISMAStatement/Checklist).
- **Pre-registration:** (If available: PROSPERO/OSF registration info)
- **PRISMA 2020 Checklist:** [`/protocol/prisma_checklist.pdf`](./protocol/prisma_checklist.pdf) (to be updated with each project milestone)

### 2.1. Research Questions
**Primary Research Question (PRQ):**
> What are the principal technical challenges, proposed algorithms, and performance trade-offs in implementing a cascaded OPA–RIS architecture for optical wireless ISAC in non-ideal channels?
**Secondary Research Questions:** (SRQ1–4 mapped to above pillars; see full protocol)

### 2.2. Eligibility Criteria (PICO Framework)

**Population / Problem**  
Optical wireless / free-space optics (OWC/FSO) and ISAC systems operating in **non-line-of-sight (NLoS)** or **turbulence-affected** optical channels.

**Intervention / Index**  
Use of **Optical Phased Arrays (OPA)** and/or **optical RIS/metasurfaces** for beam steering, relaying, or wavefront shaping. Priority on **cascaded OPA→RIS** (or OPA↔RIS) architectures.

**Comparator**  
Conventional optics (e.g., lenses/SLMs), single-hop FSO, or method ablations/baselines. A comparator is **not mandatory** for inclusion but recorded when present.

**Outcomes (must report ≥1 primary metric)**  
- **Communications:** SNR/SINR (dB), BER/EVM, throughput/capacity.  
- **Sensing:** detection probability \(P_D\), false alarm \(P_{FA}\), ROC/AUC, CRB/Fisher information.  
- **Beam/Optics:** HPBW, PSL/ISLR (dB), ROI **contrast**, scan range/rate, optical efficiency.  
- **Channel/Physics:** \(C_n^2\), Fried parameter \(r_0\), Rytov variance, propagation distance \(z\), NLoS geometry.

**Study Designs & Media**  
Peer-reviewed journals and full conference papers; high-quality preprints included if methods are sufficiently documented. Simulation, benchtop, and field trials are all eligible.

**Timeframe & Language**  
2019—present; English. (Foundational pre-2019 OPA/metasurface items may enter via **backward/forward snowballing** if they inform cascaded OPA–RIS/ISAC.)

**Exclusion Rules**  
- Pure **RF-only** RIS (non-optical) without optical results.  
- Pure holography/SLM studies **without** OPA/RIS **and** without ISAC-relevant link/beam/sensing metrics.  
- Vision/biomedical optics unrelated to comms/sensing link metrics.  
- Patents/whitepapers without peer-reviewed methodological equivalents.

**Edge Notes (for transparency)**  
When optical wavelength, aperture, or turbulence parameters are missing, the record is retained but flagged for **risk-of-bias** and excluded from any quantitative synthesis subset.


### 2.3. Information Sources & Search Strategy

**Databases & Coverage**  
IEEE Xplore, Scopus, Web of Science, Optica Publishing Group (Optics Express/OL), arXiv (physics.optics, eess.SP). Google Scholar is used only for grey literature triage and snowballing.

- **Last search completed:** 2025-09-17 (Europe/Istanbul, UTC+03)  
- **Planned update cadence:** Quarterly (or on major field releases)  
- **Search record & amendments:** `/protocol/search_strategy.md`, with date-stamped query snapshots

**Core Concepts & Synonyms**  
- *OPA:* “optical phased array”, OPA  
- *RIS:* “reconfigurable intelligent surface”, metasurface, “intelligent reflecting surface” (optical)  
- *ISAC:* “integrated sensing and communication”, “joint sensing and communication”, dual-function, JSC  
- *NLoS & Channel:* non-line-of-sight, “around-the-corner”, diffuse reflection, turbulence, **\(C_n^2\)**, **Fried \(r_0\)**, Rytov, scintillation, beam wander  
- *Cascaded/Relay:* cascaded, relay, double-pass, two-hop, multi-bounce

**Example Boolean Queries (copy & adapt per portal syntax)**

- **IEEE Xplore (All Metadata)**  
("optical phased array" OR OPA)
AND (RIS OR metasurface OR "intelligent surface" OR "intelligent reflecting surface")
AND (ISAC OR "integrated sensing" OR "joint sensing and communication" OR JSC)
AND ("non-line-of-sight" OR NLoS OR turbulence OR "Cn^2" OR "Fried parameter" OR Rytov)
AND (optical OR photonic)
AND (2019:2025)

- **Scopus / Web of Science (TITLE-ABS-KEY)**  
TITLE-ABS-KEY(
("optical phased array" OR OPA)
AND (RIS OR metasurface OR "intelligent reflecting surface")
AND (ISAC OR "integrated sensing" OR "joint sensing and communication" OR JSC)
AND ("non-line-of-sight" OR NLoS OR turbulence OR "Cn^2" OR "Fried parameter" OR Rytov)
AND (optical OR photonic)
) AND PUBYEAR > 2018 AND LANGUAGE(English)
  
- **Optica Publishing Group (site search)**  
"optical phased array" (RIS OR metasurface) (ISAC OR "integrated sensing")
(NLoS OR "non-line-of-sight" OR turbulence OR Cn^2 OR Rytov) site:opg.optica.org

- **arXiv (physics.optics OR eess.SP)**  
("optical phased array" AND (RIS OR metasurface) AND
(ISAC OR "integrated sensing" OR "joint sensing") AND
(NLoS OR turbulence OR Cn^2 OR Rytov))

- **Google Scholar (scoping & snowballing)**  
"optical phased array" RIS ISAC NLoS turbulence Cn^2 Rytov cascaded relay


**Filters & Handling**  
- Year ≥ 2019; English; document types: Article/Conference Paper/Preprint (with adequate methods).  
- De-duplication at DOI/arXiv-ID level.  
- **Snowballing:** backward/forward citation screening on all included records; each action logged in `/data/screening_log.csv` with flags `SRC=IEEE/SCOPUS/WOS/OPTICA/ARXIV/GSCHOLAR`, `TRACE=BWD/FWD`.

**Reproducibility Hooks**  
- Save exact query strings and export counts per database/date to `/protocol/search_strategy.md`.  
- Track daily/weekly deltas in `/data/screening_log.csv` (cols: `date`, `source`, `query_id`, `hits`, `included_phase1`, `included_phase2`).

---

## 3. Methodology & PRISMA Flow
Our methodology strictly tracks the PRISMA 2020 four-stage process (Identification → Screening → Eligibility → Inclusion).  
- **Flow Diagram:** [`/results/prisma_flow_diagram.png`](./results/prisma_flow_diagram.png)
- **Inclusion/Exclusion:** All decisions and rationales logged in `/data/screening_log.csv`.  
- **Transparency:** Full records of included (`included_studies.csv`) and excluded (`excluded_studies.csv`) studies are published.

### 3.1. Data Extraction and Synthesis
- **Extraction Template:** `/protocol/data_extraction_form.xlsx` (columns mirror the fields in [Data Items & Extraction](#data-items))  
- **Database:** `/data/included_studies.csv` (uses the canonical CSV header from Step 3; controlled vocabularies in `/protocol/codebook.md`)  
- **Normalization:** Per-study outcomes may be rescaled (e.g., dB per meter; per-aperture). Exact transforms are recorded in the `normalization_notes` field.  
- **Synthesis Approach:** Thematic synthesis mapped to the project’s **five technical pillars** (WD-JD, RC-PR-T, BN-RIS, RPB-Kol, HW-Q/CTRL). Mini meta-analyses are run only on homogeneous subsets; heterogeneous results are aggregated narratively with vote-counting of effect direction.  
- **Reproducibility:** All analysis scripts live under `/scripts/analysis/` and regenerate tables/figures from `included_studies.csv`. Versioned queries live in `/protocol/search_strategy.md`.

---

## 4. Contribution & Open Science Statement
- This review is the **first to explicitly synthesize the OPA–RIS architecture literature within the unified ISAC context using PRISMA 2020 standards**.
- All search strategies, data extraction, and synthesis code are published for transparency and reuse.
- **Open Access:** All materials in this repo are freely available for academic use.  
- **Data/Code Reuse Policy:** Cite this repo if you use the extraction templates, search protocols, or results in your own work.

---

## 5. Repository Structure (Key Files and Folders)
<code> 
├── README.md # You are here
├── LICENSE
├── data/
│ ├── included_studies.csv
│ ├── excluded_studies.csv
│ └── screening_log.csv
├── protocol/
│ ├── prisma_protocol.md
│ ├── prisma_checklist.pdf
│ ├── search_strategy.md
│ └── data_extraction_form.xlsx
├── results/
│ ├── prisma_flow_diagram.png
│ └── synthesis_tables/
├── scripts/
│ └── analysis/
├── manuscript/
│ └── review_article.md
├── docs/
└── supplementary_material.md </code>



---

## 6. Citing This Work
Please cite this repository (and the forthcoming article/preprint) if you build upon its code, data, protocol, or synthesis tables.  
Citation format and DOI link will be updated here after pre-print or journal acceptance.

---

## 7. Contact / Feedback
For scholarly correspondence, open a Github Issue or email: [Your Name & email here]  
Community contributions and suggestions are welcome.

---

**Keywords:** PRISMA 2020, Cascaded OPA–RIS, Optical Phased Array, Reconfigurable Intelligent Surface, NLoS, Optical Wireless, ISAC, Systematic Review, Turbulence, Coded Phase Retrieval

---

> _This work rigorously implements systematic review best practices in the emerging field of programmable optical wireless systems. Please consult the protocol and checklist for full compliance details._
