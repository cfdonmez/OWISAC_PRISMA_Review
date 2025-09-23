# A Systematic Review of Cascaded OPA–RIS Architectures for NLoS Optical Wireless ISAC
**Project Status:** Ongoing | **Last Updated:** 2025-09-23


**Completed:** PRISMA-P preregistration (OSF DOI), search strategy (initial), extraction (Sheet1), QA log (current), review_structure mapping


**Planned/In-Progress:** ROB rubric & SoF tables, automated synthesis tables, PRISMA flow image regeneration, expanded OPA/RIS/ISAC Results sections, benchmark box (turbulence), joint-metrics box (ISAC)

[![PRISMA 2020 Compliant](https://img.shields.io/badge/PRISMA-2020-blue.svg)](https://www.prisma-statement.org/)
[![Protocol Registered](https://img.shields.io/badge/OSF-Registered-informational.svg)](https://doi.org/10.17605/OSF.IO/57VRJ)
[![Open Data](https://img.shields.io/badge/Open%20Data-CC--BY--4.0-success.svg)](#contribution--open-science-statement)
[![Code License](https://img.shields.io/badge/Code-MIT-lightgrey.svg)](#contribution--open-science-statement)
> **Project Transparency Panel**
> - **Last Updated:** 2025-09-23 (Europe/Istanbul, UTC+03)
> - **Completed:** PRISMA-P preregistration (OSF DOI), search strategy (initial), extraction (Sheet1), QA log (current), review_structure mapping
> - **Planned/In-Progress:** ROB rubric & SoF tables, automated synthesis tables, PRISMA flow image regeneration, expanded OPA/RIS/ISAC Results sections, benchmark box (turbulence), joint-metrics box (ISAC)

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
- **Note on Technical Pillars.** The five axes (WD-JD, RC-PR-T, BN-RIS, RPB-Kol, HW-Q/CTRL) are **thematic synthesis axes**, not hard inclusion filters. They emerged during coding of included records to organize methods and trade-offs; the PRISMA eligibility criteria remain independent of these themes.

### Registration
This review is preregistered at the **Open Science Framework (OSF)**.  
OSF link/DOI: https://doi.org/10.17605/OSF.IO/57VRJ  
All protocol deviations will be logged in `/protocol/AMENDMENTS.md`.


---

## 2. Research Protocol (PRISMA-P)
Our protocol was designed and deposited prior to review initiation as recommended by PRISMA-P.  
**Protocol access:** See [`/protocol/prisma_protocol.md`](./protocol/prisma_protocol.md) and [checklist](https://www.prisma-statement.org/PRISMAStatement/Checklist).
- **Pre-registration:** (https://doi.org/10.17605/OSF.IO/57VRJ)
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
**Snowballing Exception.** Foundational pre-2019 optical OPA/metasurface works can enter via **backward/forward snowballing** when directly informative for cascaded OPA→RIS/ISAC; such inclusions are flagged in `TRACE` and discussed in Methods.

**Exclusion Rules**  
- Pure **RF-only** RIS (non-optical) without optical results.  
- Pure holography/SLM studies **without** OPA/RIS **and** without ISAC-relevant link/beam/sensing metrics.  
- Vision/biomedical optics unrelated to comms/sensing link metrics.  
- Patents/whitepapers without peer-reviewed methodological equivalents.

**Retention Exceptions (Transparency).** Studies lacking explicit ISAC metrics (e.g., OPA sidelobe suppression without joint sensing/communication) may be **retained** if they inform cascaded OPA→RIS feasibility or beam/optics outcomes. Such records are flagged for **risk-of-bias** and excluded from any quantitative ISAC-metric synthesis subsets; they remain eligible for narrative synthesis.

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
- **Canonical Database:** `/data/included_studies.csv` (uses the CSV header from Step 3; controlled vocabularies live in `/protocol/codebook.md`)  
- **Normalization:** Per-study outcomes may be rescaled (e.g., dB per meter; per-aperture). Exact transforms are recorded in the `normalization_notes` field.  
- **Synthesis Approach:** Thematic synthesis mapped to the project’s **five technical pillars** (WD-JD, RC-PR-T, BN-RIS, RPB-Kol, HW-Q/CTRL). Mini meta-analyses are run only on homogeneous subsets; heterogeneous results are aggregated narratively with vote-counting of effect direction.  
- **Reproducibility:** All analysis scripts live under `/scripts/analysis/` and regenerate tables/figures from `included_studies.csv`. Versioned queries live in `/protocol/search_strategy.md`.  
- **Validation:** Run `python scripts/analysis/validate_included_studies.py data/included_studies.csv` before commits.
- **Mapping to Manuscript Sections.** Each included record is mapped to a manuscript section via `/docs/review_structure.md` (e.g., OPA → Section 3.1; RIS → Section 3.2; NLoS-Turb → Section 4.1). The mapping file is versioned and updated with each extraction/QA cycle.


<a id="data-items"></a>
## Data Items & Extraction

All included records are extracted into `/data/included_studies.csv` using the template in `/protocol/data_extraction_form.xlsx`. Fields are aligned to the five technical pillars (WD-JD, RC-PR-T, BN-RIS, RPB-Kol, HW-Q/CTRL) to keep screening → synthesis consistent.

**Required fields (must be filled for inclusion):**

| Field | Type | Description | Example |
|---|---|---|---|
| record_id | string | Unique key (stable across updates) | ieeexp-2023-01234 |
| doi_or_id | string | DOI or arXiv ID | 10.1364/OE.xxxxx |
| venue | enum | {journal, conf, preprint} | journal |
| year | int | Publication year | 2024 |
| title | string | Paper title | Cascaded OPA–RIS for NLoS ISAC |
| authors | string | First author et al. | Lee et al. |
| SRC | enum | {IEEE, SCOPUS, WOS, OPTICA, ARXIV, GSCHOLAR} | IEEE |
| TRACE | enum | {DIRECT, BWD, FWD} | DIRECT |
| architecture | enum | {OPA→RIS, OPA↔RIS, single-hop, other} | OPA→RIS |
| channel_regime | enum | {LoS, NLoS, NLoS+turbulence} | NLoS+turbulence |
| wavelength_nm | float | Operating wavelength (nm) | 1550 |
| primary_outcome | enum | {SNR,SINR,BER,EVM,PSL,ISLR,Contrast,ROC,CRB} | SINR |
| task_domain | enum | {comms, sensing, ISAC} | ISAC |
| data_availability | enum | {code+data, code-only, none} | code-only |

**OPA parameters (fill if applicable):**

| Field | Type | Description | Example |
|---|---|---|---|
| opa_N_elements | int | Number of elements | 4096 |
| opa_pitch_um | float | Element pitch (µm) | 6.0 |
| opa_phase_bits | int | Quantization bits | 2 |
| opa_scan_range_deg | float | ±scan range | 30 |
| opa_scan_rate_hz | float | Max scan rate | 1000 |

**RIS/metasurface parameters (fill if applicable):**

| Field | Type | Description | Example |
|---|---|---|---|
| ris_size_elems | int | Active elements (or equivalent area) | 2048 |
| ris_lattice | enum | {grid, aperiodic, blue-noise, hybrid} | blue-noise |
| ris_phase_states | int | Discrete phase levels | 4 |
| ris_response_ms | float | Element response time (ms) | 2.5 |
| ris_fill_factor | float | Active fill (0–1) | 0.72 |

**Propagation / turbulence / geometry:**

| Field | Type | Description | Example |
|---|---|---|---|
| z_total_m | float | Total path length | 120 |
| nlos_geometry | enum | {single-bounce, multi-bounce, around-the-corner} | single-bounce |
| Cn2 | float | Refractive index structure const. (m^-2/3) | 1e-14 |
| r0_m | float | Fried parameter (m) | 0.04 |
| rytov_var | float | Rytov variance σ_R^2 | 0.9 |
| regime | enum | {Fresnel, Fraunhofer, mixed} | Fresnel |

**Algorithms / pillars (tick what applies):**

| Field | Type | Description | Example |
|---|---|---|---|
| pillar_WD_JD | bool | Wigner-domain joint design used | true |
| pillar_RC_PR_T | bool | RIS-coded phase retrieval | true |
| pillar_BN_RIS | bool | Aperiodic/blue-noise design | false |
| pillar_RPB_Kol | bool | Robust pre-shaping under turbulence | true |
| pillar_HW_Q_CTRL | bool | Hardware-aware/quantization/calibration | true |
| optimizer | string | e.g., ADAM, SGD, GA, CMA-ES | ADAM |
| training_signal | string | pilot/PR masks used | m=16 coded masks |

**Outcomes (record at least one; use units shown):**

| Field | Type | Units | Example |
|---|---|---|---|
| snr_db | float | dB | 24.5 |
| sinr_db | float | dB | 18.2 |
| ber | float | — | 2.3e-4 |
| evm_pct | float | % | 3.8 |
| psl_db | float | dB | -17.2 |
| islr_db | float | dB | -11.0 |
| hpbw_deg | float | deg | 0.8 |
| contrast | float | ROI/background | 6.2 |
| roc_auc | float | 0–1 | 0.93 |
| crb_unit | string | parameter name & unit | angle (deg^2) |
| runtime_s | float | seconds | 42.3 |
| mem_gb | float | gigabytes | 3.1 |

**Reproducibility & bias flags (quick):**

| Field | Type | Description | Example |
|---|---|---|---|
| baselines_present | bool | Fair baselines/ablations? | true |
| realism_score | enum | {low, mid, high} | mid |
| rob_overall | enum | {low, some, high} | some |
| normalization_notes | string | Any rescaling/assumptions applied | SNR normalized per-meter |
| notes | string | Free-text caveats | Missing r0 unit; inferred from fig. |

**CSV header (copy into `/data/included_studies.csv`):**  
`record_id,doi_or_id,venue,year,title,authors,SRC,TRACE,architecture,channel_regime,wavelength_nm,primary_outcome,task_domain,data_availability,opa_N_elements,opa_pitch_um,opa_phase_bits,opa_scan_range_deg,opa_scan_rate_hz,ris_size_elems,ris_lattice,ris_phase_states,ris_response_ms,ris_fill_factor,z_total_m,nlos_geometry,Cn2,r0_m,rytov_var,regime,pillar_WD_JD,pillar_RC_PR_T,pillar_BN_RIS,pillar_RPB_Kol,pillar_HW_Q_CTRL,optimizer,training_signal,snr_db,sinr_db,ber,evm_pct,psl_db,islr_db,hpbw_deg,contrast,roc_auc,crb_unit,runtime_s,mem_gb,baselines_present,realism_score,rob_overall,normalization_notes,notes`

**Coding rules (consistency):**
- Use **nm** for wavelength, **m** for distances, **deg** for angles, **dB** for SNR/SINR/PSL/ISLR.  
- Booleans are `true/false`; enums exactly as listed.  
- If a value is missing, leave blank and explain in `notes`.  
- If paper units differ, convert; log any rescaling in `normalization_notes`.

**Extraction workflow:**
1. Create a new row per study in `/data/included_studies.csv`.  
2. Prefer the **main** scenario if multiple settings exist; mention alternates in `notes` (you can split per-scenario rows later).  
3. Keep PDFs out of the repo; manage them in your reference manager; store persistent IDs in `doi_or_id`.

### Pipeline Status (Reproducibility)
All scripts under `/scripts/analysis/` are versioned and runnable. Generated artifacts under `/results/` are being expanded iteratively. Where a table/figure is listed but not yet present, it is **planned** and will be added with a date-stamped commit; interim manual tables are linked in `/supplementary_material.md`.

### 3.2. Automated Counts & Tables

We auto-generate counts and synthesis tables from the CSVs:

- **PRISMA counts:** `python scripts/analysis/prisma_counts.py data/screening_log.csv`  
  Outputs `results/prisma_counts.json` and `results/synthesis_tables/prisma_counts.csv`.

- **Synthesis tables:** `python scripts/analysis/synth_make_tables.py data/included_studies.csv`  
  Emits pillar coverage, metrics coverage, hardware-awareness, and turbulence parameter summaries under `results/synthesis_tables/`.

For convenience, use the `Makefile`:

make all        # validate + prisma + synth
make validate   # schema & row checks
make prisma     # update PRISMA counts
make synth      # rebuild synthesis tables

### 3.3. Risk of Bias & Certainty of Evidence

- **Risk-of-Bias rubric:** `/protocol/risk_of_bias_tool.md` (**planned**; draft rubric to be committed with initial ROB pass).
- **ROB summaries:** `python scripts/analysis/rob_summary.py data/included_studies.csv`  
  → `results/synthesis_tables/rob_overall_counts.csv`, `results/synthesis_tables/rob_by_pillar.csv`.  
- **Certainty (SoF):** planned; initial SoF tables will be generated after the first ROB pass. Heuristics are provisional and will be overrideable after manual review.
  → `results/synthesis_tables/SoF_pillars.csv` (simple heuristic based on % Low ROB per pillar).

> Notes: We report ROB on the 3-level scale (low/some/high). SoF certainty labels (High/Moderate/Low) are derived heuristically and can be overridden after manual review.



## 4. Contribution & Open Science Statement
- To the best of our knowledge, this is the first PRISMA-aligned synthesis that explicitly frames OPA–RIS architectures within a unified optical ISAC context; we welcome prior-art pointers via Issues.
- All search strategies, data extraction, and synthesis code are published for transparency and reuse.
- **Open Access:** All materials in this repo are freely available for academic use.  
- **Data/Code Reuse Policy:** Cite this repo if you use the extraction templates, search protocols, or results in your own work.

---

## 5. Repository Structure (Key Files and Folders)
<code> 
├── README.md
├── LICENSE
├── data/
│   ├── included_studies.csv
│   ├── excluded_studies.csv
│   └── screening_log.csv
├── protocol/
│   ├── prisma_protocol.md
│   ├── prisma_checklist.pdf
│   ├── search_strategy.md
│   ├── data_extraction_form.xlsx
│   ├── risk_of_bias_tool.md
│   └── exclusion_reasons.md
├── results/
│   ├── prisma_flow_diagram.png
│   ├── prisma_counts.json
│   └── synthesis_tables/
│       ├── prisma_counts.csv
│       ├── pillars_summary.csv
│       ├── metrics_coverage.csv
│       ├── hardware_awareness.csv
│       ├── turbulence_params.csv
│       ├── rob_overall_counts.csv
│       ├── rob_by_pillar.csv
│       ├── SoF_pillars.csv
│       └── excluded_reasons.csv
├── scripts/
│   └── analysis/
│       ├── validate_included_studies.py
│       ├── prisma_counts.py
│       ├── excluded_reasons.py
│       ├── synth_make_tables.py
│       ├── rob_summary.py
│       └── make_prisma_flow.py
├── .github/
│   └── workflows/
│       └── validate-and-build.yml
├── manuscript/
│   └── review_article.md
├── docs/
└── supplementary_material.md</code>



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
