# Search Strategy — Snapshot 2025-09-18 (UTC+03)
Databases: IEEE Xplore, Scopus, Web of Science, Optica (OE/OL), arXiv (physics.optics, eess.SP); GS for snowballing only.

## Elicit — elicit_v1_2025-09-18
Query: ("optical phased array" OR OPA) AND … [full query]
Filters: Year ≥ 2019; English; Article/Conf/Preprint
Hits returned: 578


## IEEE Xplore (All Metadata)
QUERY_ID: ieee_v1_2025-09-18
("optical phased array" OR OPA) AND (RIS OR metasurface OR "intelligent reflecting surface")
AND (ISAC OR "integrated sensing" OR "joint sensing and communication" OR JSC)
AND ("non-line-of-sight" OR NLoS OR turbulence OR "Cn^2" OR "Fried parameter" OR Rytov)
AND (optical OR photonic) AND (2019:2025)
Filters: English; Article/Conference

## Scopus (TITLE-ABS-KEY) — scopus_v1_2025-09-18
…(same logic, Scopus syntax)…

## Web of Science — wos_v1_2025-09-18
…(syntax)…

## Optica Publishing — optica_v1_2025-09-18
…(site query)…

## arXiv — arxiv_v1_2025-09-18
…(syntax)…

Notes: export format, any portal quirks, and de-dup plan at DOI/arXiv-ID level.

## Screening Questions for Title/Abstract Review

These questions guide the initial screening process to determine eligibility for full-text review. Each question should be answered with a "Yes", "No", or "Unclear" based on the title and abstract.

*   **Comprehensive Coverage**
    *   **Question:** Does the study address all three required technology domains (OPA, RIS/metasurfaces, and ISAC) with demonstrated integration rather than only mentioning one or two domains superficially?

*   **ISAC Applications**
    *   **Question:** Does the study specifically discuss or demonstrate applications of ISAC (e.g., joint communication and sensing for specific scenarios like target detection, localization, or environmental monitoring)?

*   **Optical Implementation Focus**
    *   **Question:** Is the primary focus of the study on optical wireless systems, or does it primarily address RF systems with only a tangential mention of optical counterparts?

*   **Optical Phased Arrays**
    *   **Question:** Does the study explicitly involve Optical Phased Arrays (OPAs) or photonic phased arrays as a core component of its proposed system or analysis?

*   **Publication Quality**
    *   **Question:** Does the publication appear to be a peer-reviewed article (journal/conference) with sufficient academic rigor, or is it a preliminary abstract, editorial, or non-technical report?

*   **Reconfigurable Intelligent Surfaces**
    *   **Question:** Does the study explicitly involve Reconfigurable Intelligent Surfaces (RIS), intelligent reflecting surfaces, or optical metasurfaces as a core component of its proposed system or analysis?

*   **Technical Substance**
    *   **Question:** Does the study provide sufficient technical detail, methodologies, and performance metrics to allow for a meaningful assessment of its contributions?

*   **Technology Integration**
    *   **Question:** Does the study demonstrate a clear integration or interaction between OPA and RIS components, or are they discussed as separate, unrelated entities?

*   **NLoS & Turbulence Context:**
    *   **Question:** Does the study explicitly address non-line-of-sight (NLoS) propagation or atmospheric turbulence effects (e.g., scintillation, beam wander, Fried parameter $r_0$)?

*   **Joint OPA–RIS Beamforming / Wigner-space Design:**
    *   **Question:** Does the study propose or analyze joint design strategies for OPA→RIS cascades, including Wigner-space or space–frequency optimization methods?

*   **Phase Retrieval / Measurement Strategy:**
    *   **Question:** Does the study involve phase retrieval, coded measurement schemes (e.g., RIS-coded intensity-only acquisition), or related algorithmic recovery methods?

*   **Robustness & Performance Metrics:**
    *   **Question:** Does the study evaluate robustness under turbulence or hardware constraints, using metrics such as expected SNR, variance, contrast, ROC curves, or sidelobe suppression?
