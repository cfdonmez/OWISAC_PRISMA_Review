# A Systematic Review of Cascaded OPA-RIS Architectures for NLoS Optical Wireless ISAC

**Project Status:** `Ongoing` 

## 1. Overview

This repository contains all the documentation, data, and analysis scripts for a systematic review conducted in accordance with the **PRISMA 2020** (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines.

The primary objective of this review is to systematically identify, analyze, and synthesize the existing literature on the use of a **cascaded architecture**—where an **Optical Phased Array (OPA)** dynamically targets a **Reconfigurable Intelligent Surface (RIS)**—to enable reliable **Integrated Sensing and Communication (ISAC)** in non-line-of-sight (NLoS) and turbulent optical wireless environments.

This project aims to:
-   Map the state-of-the-art in the enabling technologies (OPA, RIS, Optical ISAC).
-   Identify the key technical challenges and performance metrics.
-   Analyze the potential of the cascaded OPA-RIS architecture.
-   Highlight the unresolved research gaps and propose future research directions.

## 2. Research Protocol (PRISMA-P)

The protocol for this systematic review is documented in this repository to ensure transparency and reproducibility.

### 2.1. Research Questions

The review is guided by the following primary research question:
> What are the primary technical challenges, potential architectures, and performance metrics in implementing a cascaded optical wireless system using an OPA dynamically targeting a RIS for ISAC applications in non-ideal channels?

### 2.2. Eligibility Criteria (PICO Framework)

Studies were included based on the following PICO criteria:

-   **Population:** Optical wireless communication (OWC/FSO) systems operating in non-ideal channels (e.g., NLoS, blockage, atmospheric turbulence).
-   **Intervention:** Systems employing at least one of the following for beam steering, relaying, or wavefront manipulation:
    -   Optical Phased Arrays (OPAs)
    -   Reconfigurable Intelligent Surfaces (RIS), Metasurfaces, Spatial Light Modulators (SLMs), Digital Micromirror Devices (DMDs), or LCoS.
-   **Comparison:** No specific comparator is required, but studies comparing the proposed systems to conventional LoS, RF, or adaptive optics solutions are of high interest.
-   **Outcome:** Studies reporting on at least one of the following:
    -   Communication performance metrics (e.g., BER, SNR, data rate).
    -   Sensing performance metrics (e.g., accuracy, RMSE, CRB).
    -   System/hardware metrics (e.g., FOV, efficiency, switching speed).
    -   Channel models or theoretical analyses.

### 2.3. Information Sources and Search Strategy

-   **Databases Searched:** IEEE Xplore, Scopus, Web of Science, Google Scholar, and ArXiv.
-   **Search Period:** January 1, 2019 – September 1, 2024.
-   **Search Strategy:** The detailed search queries combining keywords with Boolean operators are documented in `/protocol/search_strategy.md`.

## 3. Methodology

This review follows the PRISMA 2020 statement. The entire process, from identification to inclusion, is documented.

### 3.1. Selection Process

A multi-stage screening process was employed:
1.  **Identification:** Automated searches were conducted across the specified databases.
2.  **Screening:** Duplicates were removed, followed by a title and abstract screening phase.
3.  **Eligibility:** Full-text articles of the remaining studies were assessed for eligibility against the PICO criteria.

The complete selection process is visualized in the PRISMA 2020 flow diagram located at `/results/prisma_flow_diagram.png`.

### 3.2. Data Extraction and Management

Data from the included studies were extracted and managed using a structured spreadsheet. The extracted data includes bibliographic information, study design, technical specifications of the intervention (OPA/RIS), reported performance metrics, and key findings.

-   **Included Studies Database:** `data/included_studies.csv`
-   **Data Extraction Template:** `protocol/data_extraction_form.xlsx`

## 4. Repository Structure
