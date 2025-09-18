# A Systematic Review of Cascaded OPA–RIS Architectures for NLoS Optical Wireless ISAC
**Project Status:** Ongoing | **Last Updated:** 2025-09-17  
[![PRISMA 2020 Compliant](https://img.shields.io/badge/PRISMA-2020-blue.svg)](https://www.prisma-statement.org/)

---

## 1. Overview & Rationale
This repository documents a systematic review, conducted in strict accordance with the **PRISMA 2020** guidelines [[PRISMA Statement](https://www.prisma-statement.org/)], of cascaded Optical Phased Array (OPA)–Reconfigurable Intelligent Surface (RIS) architectures for non-line-of-sight (NLoS) optical wireless integrated sensing and communications (ISAC).  
The project aims to:
- Map state-of-the-art enabling technologies (OPA, RIS, metasurfaces) for robust ISAC in NLoS and turbulence-prone optical wireless channels.
- Identify technical challenges, underpinning theory, and application-driven performance metrics.
- Thematically analyze solutions and research gaps across the following **four pillars**:
  1. **Joint Spatio-Frequency Beamforming**
  2. **Channel Acquisition & Coded Phase Retrieval**
  3. **Grating Lobe Suppression & Aperiodic Design**
  4. **Turbulence-Robust Wavefront Shaping**

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
- **Population:** OWC/FSO/ISAC systems in NLoS/turbulent optical channels.
- **Intervention:** Implementation of OPA and/or optical RIS for beam steering, relaying or wavefront manipulation; focus on cascaded configurations.
- **Comparison:** Not restricted; comparative evaluations within each included study recorded where relevant.
- **Outcomes:** Theoretical/experimental/simulation results concerning:
  - Communication: BER, SNR, Channel Capacity, etc.
  - Sensing: Detection/Estimation Accuracy, Cramér-Rao Bound.
  - System/Hardware: Efficiency, FOV, Grating Lobe Suppression.

### 2.3. Information Sources & Search Strategy
- **Databases Searched:** IEEE Xplore, Scopus, Web of Science, Google Scholar, ArXiv.
- **Coverage:** 2019–Present.
- **Full Search Strategy:** See [`/protocol/search_strategy.md`](./protocol/search_strategy.md).
- **Screening & Inclusion Log:** [`/data/screening_log.csv`](./data/screening_log.csv)

---

## 3. Methodology & PRISMA Flow
Our methodology strictly tracks the PRISMA 2020 four-stage process (Identification → Screening → Eligibility → Inclusion).  
- **Flow Diagram:** [`/results/prisma_flow_diagram.png`](./results/prisma_flow_diagram.png)
- **Inclusion/Exclusion:** All decisions and rationales logged in `/data/screening_log.csv`.  
- **Transparency:** Full records of included (`included_studies.csv`) and excluded (`excluded_studies.csv`) studies are published.

### 3.1. Data Extraction and Synthesis
- **Extraction Template:** `/protocol/data_extraction_form.xlsx`
- **Database:** `/data/included_studies.csv` (Findings are thematically coded and traceable per SRQ)
- **Synthesis Approach:** Not mere summary: analysis is structured as thematic synthesis mapped to the project's four technical pillars.
- **Reproducibility:** All major code/scripts are under `/scripts/` and can be run on the published data for independent validation.

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
