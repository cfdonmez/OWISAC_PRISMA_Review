# Methods

<!-- PRISMA items 5-15: Eligibility, Sources, Search, Selection, Data items, RoB, Effect measures, Synthesis, Reporting bias, Certainty -->

## 1. Protocol and Registration

This systematic review was conducted and reported following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 statement. The review protocol was pre-registered on the Open Science Framework (OSF) [ADD OSF LINK/DOI HERE]. The search was limited to studies published between January 1, 2019, and December 31, 2025, and restricted to articles written in English.

## 2. Information Sources and Search Strategy

We performed a systematic search of the following electronic databases: IEEE Xplore, Scopus, Web of Science, and the arXiv preprint server. The search strategy was designed to identify studies on the intersection of OPAs, RIS, and optical ISAC for NLoS scenarios.

The primary query string used was:
`("optical phased array" OR OPA) AND (RIS OR "reconfigurable intelligent surface" OR metasurface) AND (ISAC OR "integrated sensing and communication")`

The full search strategy, including any variations for specific databases, is documented in the `protocol/search_strategy.md` file. We also screened the reference lists of included articles to identify additional relevant studies (i.e., snowballing).

## 3. Eligibility Criteria

Studies were selected based on the following criteria:

### Inclusion Criteria
- Must address optical wireless communication, sensing, or ISAC.
- Must explicitly involve Optical Phased Arrays (OPAs) and/or Reconfigurable Intelligent Surfaces (RIS) in the optical domain.
- Must address challenges related to non-line-of-sight (NLoS) propagation, blockage mitigation, or atmospheric turbulence.

### Exclusion Criteria
- Studies focused exclusively on radio-frequency (RF) technologies without direct application or adaptation to the optical domain.
- Works limited to fiber-optic systems with no free-space component.
- Editorials, commentaries, or abstracts lacking sufficient technical detail, methods, or performance metrics.

## 4. Selection Process

The study selection was performed in two stages. First, titles and abstracts of all retrieved records were screened for relevance by two independent reviewers. Second, the full texts of potentially eligible articles were assessed against the inclusion and exclusion criteria. Any disagreements between reviewers were resolved through discussion and consensus.

## 5. Data Extraction and Items

A structured data extraction form was used to collect key information from each included study. The extracted data items included:
- **Bibliographic Information:** Citation details, year of publication.
- **System Architecture:** Key components (e.g., OPA type, RIS design), and overall system configuration.
- **Channel Conditions:** Turbulence parameters (e.g., Cn², r₀), NLoS scenario descriptions.
- **Beamforming Strategy:** Algorithms and methods used for beam steering and shaping.
- **Performance Metrics:** Reported values for SINR, bit-error rate (BER), sensing contrast, half-power beamwidth (HPBW), and peak sidelobe level (PSL).

The detailed codebook defining each data item is available in `protocol/codebook.md`.

## 6. Risk of Bias Assessment

The quality and risk of bias of each included study were assessed using a custom tool based on seven key domains relevant to the field: (1) study design and reproducibility, (2) realism of physics and channel modeling, (3) inclusion of comparative baselines, (4) hardware realism and feasibility, (5) appropriateness of turbulence modeling, (6) availability of data and code, and (7) context for reported performance metrics.

## 7. Synthesis Methods

We synthesized the extracted data using a narrative approach, supplemented by summary tables to compare system architectures, performance metrics, and channel conditions across studies. Where possible, we performed a qualitative synthesis of the trade-offs between sensing and communication performance. Subgroup analyses were planned based on the type of OPA/RIS technology and the NLoS scenario.
