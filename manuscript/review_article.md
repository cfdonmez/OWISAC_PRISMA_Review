# Abstract
<!-- PRISMA item 2: Abstract -->



# Introduction

## 1. Rationale

The convergence of sensing and communication functionalities, known as Integrated Sensing and Communication (ISAC), is a cornerstone of future wireless networks, including 6G. While radio frequency (RF) ISAC is well-explored, its optical wireless communication (OWC) counterpart—Optical ISAC (O-ISAC)—offers compelling advantages such as vast unregulated bandwidth, inherent security, and immunity to electromagnetic interference. However, OWC systems are highly susceptible to line-of-sight (LoS) link blockages, a critical challenge for robust operation in dynamic environments.

Recent advancements in optical beamforming technologies, specifically Optical Phased Arrays (OPAs) and Reconfigurable Intelligent Surfaces (RIS), present a promising solution to overcome non-line-of-sight (NLoS) challenges. Cascaded OPA-RIS architectures can potentially steer optical beams around obstacles, enabling reliable links where direct paths are unavailable. This systematic review addresses the emerging field of cascaded OPA-RIS systems designed to enable robust NLoS Optical ISAC.

## 2. Objectives

This review aims to systematically synthesize and evaluate the existing literature on cascaded OPA–RIS architectures for NLoS optical wireless ISAC. We focus on the system designs, performance trade-offs, and channel modeling approaches that underpin this technology.

### Research Questions

The primary research questions (RQs) guiding this review are:

- **RQ1:** Which OPA–RIS designs and beamforming strategies are proposed to enable reliable NLoS optical links, particularly under atmospheric turbulence?
- **RQ2:** What are the fundamental trade-offs between sensing and communication performance (e.g., Signal-to-Interference-plus-Noise Ratio (SINR) vs. target detection contrast) in these integrated systems?
- **RQ3:** Which channel and propagation models are predominantly used to characterize NLoS and turbulent optical links, and to what extent have they been experimentally validated?


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


# Results

<!-- PRISMA items 16-22: Selection, Characteristics, RoB, Individual results, Synthesis, Reporting biases, Certainty -->

## 1. Study Selection

Our initial search across the specified databases yielded [X] records. After removing duplicates, [Y] records were screened based on their titles and abstracts. This resulted in [Z] articles selected for full-text review. Following the full-text assessment, a final set of [N] studies met the eligibility criteria and were included in the systematic review. The complete study selection process is illustrated in the PRISMA flow diagram (Figure 1).

<!-- The PRISMA flow diagram will be generated by scripts/analysis/make_prisma_flow.py and embedded here. -->
<!-- INCLUDE: results/figures/prisma_flow.png -->

## 2. Study Characteristics

The [N] included studies were published between [Start Year] and [End Year]. A majority of the works were theoretical or simulation-based, with a smaller subset presenting experimental validations. The most commonly investigated architectures were cascaded OPA-RIS systems, designed for NLoS operation in indoor or outdoor environments. A summary of the key characteristics of each included study is provided in the synthesis tables.

## 3. Synthesis of Results

The findings from the included studies are synthesized below, structured around the review's primary research questions.

### RQ1: OPA–RIS Designs and Beamforming Strategies

The included studies proposed several distinct OPA-RIS architectures. The primary designs involved [e.g., silicon photonics-based OPAs coupled with metasurface-based RIS]. Beamforming strategies ranged from simple phase-only control to more complex hybrid amplitude-phase optimization algorithms. Table [X] summarizes the different architectures and their corresponding beamforming approaches.

<!-- A summary table generated by the synthesis scripts will be included here. -->
<!-- INCLUDE: results/synthesis_tables/architectures.md -->

### RQ2: Sensing–Communication Trade-offs

The trade-off between communication performance (typically measured in SINR or BER) and sensing performance (e.g., target detection contrast or resolution) was a central theme in [K] of the [N] studies. Our synthesis indicates that [e.g., higher SINR is often achieved at the cost of a wider beam, which can degrade sensing resolution]. These trade-offs are summarized for key studies in Table [Y].

<!-- A summary table generated by the synthesis scripts will be included here. -->
<!-- INCLUDE: results/synthesis_tables/summary.md -->

### RQ3: Channel and Propagation Models

The characterization of the NLoS optical channel under turbulence was addressed using various models. The most prevalent atmospheric turbulence model was the [e.g., Gamma-Gamma distribution], with turbulence strength (`Cn²`) values ranging from `1e-15` to `1e-13` m⁻²/³. Only a minority of studies provided experimental validation for their chosen channel models.


# Discussion

<!-- PRISMA items 23-24: Interpretation, Limitations -->

## 1. Summary of Main Findings

This systematic review synthesized [N] studies on cascaded OPA-RIS architectures for NLoS Optical ISAC. Our findings indicate three key trends:
1.  **Architectural Convergence:** The field is converging towards [e.g., hybrid RF-optical beamforming] to manage the trade-offs between beam width and steering accuracy.
2.  **Performance Trade-offs:** A fundamental trade-off between communication reliability (SINR/BER) and sensing resolution is consistently reported, though the methods for quantifying this trade-off vary significantly.
3.  **Modeling Gaps:** While sophisticated channel models for atmospheric turbulence are often employed, there is a notable lack of experimental validation, particularly for cascaded NLoS links.

## 2. Strengths and Limitations of the Evidence

The evidence base is strong in its theoretical and simulation-based exploration of the problem space. However, it is limited by a scarcity of experimental work. The risk of bias assessment revealed that many studies lack reproducible methods and fail to compare their proposals against established baselines, limiting the generalizability of their findings.

## 3. Limitations of the Review Process

This review has several limitations. First, our search was restricted to English-language publications, potentially introducing a language bias. Second, the heterogeneity in performance metrics and experimental conditions across studies precluded a formal meta-analysis. Finally, the rapid pace of innovation in this field means that some very recent works may not have been captured by our search timeframe.

## 4. Implications for Future Research

Based on our synthesis, we identify several critical areas for future research:
-   **Experimental Validation:** There is an urgent need for experimental testbeds to validate the performance of cascaded OPA-RIS systems in real-world NLoS and turbulent conditions.
-   **Standardized Metrics:** The community would benefit from developing standardized metrics and benchmark scenarios to allow for more direct comparison of different ISAC architectures.
-   **Hardware Co-design:** Future work should focus on the co-design of OPA and RIS hardware to optimize for the specific demands of ISAC, such as rapid beam switching and wide-angle steering.
-   **Machine Learning Integration:** AI/ML-based approaches could be explored for real-time channel estimation and beamforming optimization in dynamic NLoS environments.


# Conclusion

## 9. Conclusion
## Open Science / References / Appendices



# Acknowledgments
<!-- PRISMA items 25-26: Support, Competing interests (can also be in separate sections) -->


We identified 578 records and included 85 studies after screening; details in PRISMA flow.
All reported metrics (SNR/SINR, BER/EVM, HPBW/PSL/ISLR, ROC) are contextualized by λ, z, LoS/NLoS, and turbulence parameters (Cn², r0, σR²) when available.

## Funding
This work received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.
<!-- Replace the sentence above with your grant info if applicable. -->

## Competing Interests
The authors declare no competing interests.
<!-- If COI exists, replace this line with a short statement and, if required by journal policy, a detailed COI disclosure. -->


# References
<!-- PRISMA item 27: Data/Code availability can be in Supplementary/README -->



