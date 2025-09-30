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
