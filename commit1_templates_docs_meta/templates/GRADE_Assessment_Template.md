# GRADE Assessment Template for OWISAC Systematic Review

## Overview
This template implements the GRADE (Grading of Recommendations Assessment, Development and Evaluation) approach to assess the certainty of evidence for outcomes in systematic reviews of Optical Wireless Integrated Sensing and Communication (OWISAC) systems.

## Study Information
- **Outcome:** ________________________________
- **Comparison:** ________________________________ 
- **Population/Setting:** ________________________________
- **Studies Included:** ________________________________
- **Assessor:** ________________________________
- **Date:** ________________________________

## Initial Rating

### Study Design Classification
- [ ] **Randomized Controlled Trials** → Start with **HIGH** certainty
- [ ] **Non-randomized Studies (Observational)** → Start with **LOW** certainty

**Initial Certainty Level:** HIGH / LOW

**Justification:** ________________________________

---

## GRADE Assessment Domains

### Domain 1: Risk of Bias
**Assessment Question:** Do the included studies have important methodological limitations?

**Considerations:**
- Adequacy of study design for the research question
- Implementation and configuration validity  
- Measurement procedures and instrumentation
- Statistical analysis appropriateness
- Selective reporting of results

**Evidence Review:**
- Number of studies with low risk of bias: ______ / ______
- Number of studies with some concerns: ______ / ______  
- Number of studies with high risk of bias: ______ / ______

**Impact on Results:**
- [ ] **No serious limitations** - Most studies have low risk of bias
- [ ] **Serious limitations** - Most studies have some concerns or significant flaws
- [ ] **Very serious limitations** - Most studies have high risk of bias or fundamental flaws

**Rating Decision:** No downgrade / Downgrade 1 level / Downgrade 2 levels

**Justification:** ________________________________

---

### Domain 2: Inconsistency
**Assessment Question:** Are the results across studies consistent?

**Statistical Heterogeneity:**
- I² statistic: ______% 
- P-value for heterogeneity test: ______
- Prediction interval: ______

**Clinical/Practical Heterogeneity:**
- System architectures vary significantly: Yes / No
- Operating conditions vary substantially: Yes / No
- Measurement methods differ importantly: Yes / No

**Consistency Assessment:**
- Direction of effects consistent: Yes / No / Mixed
- Magnitude of effects consistent: Yes / No / Varies widely
- Confidence intervals overlap: Yes / No / Minimal

**Impact on Results:**
- [ ] **No serious inconsistency** - Results are reasonably consistent
- [ ] **Serious inconsistency** - Significant variation that is concerning but explainable  
- [ ] **Very serious inconsistency** - Results vary widely with no clear explanation

**Rating Decision:** No downgrade / Downgrade 1 level / Downgrade 2 levels

**Justification:** ________________________________

---

### Domain 3: Indirectness
**Assessment Question:** Do the studies directly address the research question?

**Population/System Indirectness:**
- Target systems vs. studied systems: Direct / Some differences / Major differences
- Operating conditions relevance: High / Moderate / Low
- Performance requirements alignment: Good / Fair / Poor

**Intervention Indirectness:**
- OPA-RIS configurations match review question: Yes / Partially / No
- Implementation approaches are relevant: Yes / Partially / No
- Scale and complexity are appropriate: Yes / Partially / No

**Outcome Indirectness:**  
- Outcomes directly relevant to ISAC performance: Yes / Partially / No
- Measurement methods are appropriate: Yes / Partially / No
- Follow-up duration is adequate: Yes / Partially / No / NA

**Comparison Indirectness:**
- Comparators are relevant: Yes / Partially / No / NA
- Baseline conditions are appropriate: Yes / Partially / No

**Impact on Results:**
- [ ] **No serious indirectness** - Evidence directly addresses the question
- [ ] **Serious indirectness** - Some concerns about applicability
- [ ] **Very serious indirectness** - Major concerns about applicability

**Rating Decision:** No downgrade / Downgrade 1 level / Downgrade 2 levels

**Justification:** ________________________________

---

### Domain 4: Imprecision
**Assessment Question:** Are the results precise enough to make confident decisions?

**Sample Size Considerations:**
- Total number of observations/experiments: ______
- Number of studies: ______
- Average study size: ______

**Confidence Intervals:**
- 95% CI for main effect: [______, ______]
- CI includes null effect: Yes / No
- CI includes clinically important effects: Yes / No
- CI width is: Narrow / Moderate / Wide

**Optimal Information Size:**
- Required sample size for adequate power: ______
- Actual total sample size: ______
- Meets optimal information size: Yes / No

**Statistical Significance:**
- Primary analysis p-value: ______
- Effect crosses conventional significance threshold: Yes / No

**Impact on Results:**
- [ ] **No serious imprecision** - Results are sufficiently precise
- [ ] **Serious imprecision** - Some uncertainty due to limited precision
- [ ] **Very serious imprecision** - High uncertainty due to very limited precision

**Rating Decision:** No downgrade / Downgrade 1 level / Downgrade 2 levels

**Justification:** ________________________________

---

### Domain 5: Publication Bias
**Assessment Question:** Are all relevant studies likely to have been included?

**Search Comprehensiveness:**
- Systematic search conducted: Yes / Partially / No
- Grey literature searched: Yes / No
- Multiple databases searched: Yes / No
- Language restrictions applied: Yes / No

**Publication Bias Tests:**
- Funnel plot assessment: Symmetric / Asymmetric / Cannot assess
- Egger's test p-value: ______ (if applicable)
- Number of studies: ______ (minimum 10 for formal tests)

**Evidence of Missing Studies:**
- Industry-funded studies vs. independent studies: Balanced / Imbalanced
- Positive vs. negative results: Balanced / Imbalanced  
- Recent vs. older studies: Balanced / Imbalanced

**Expert Knowledge:**
- Known unpublished studies: None / Some / Many
- Conference abstracts vs. full publications: Consistent / Inconsistent

**Impact on Results:**
- [ ] **Undetected** - No evidence of publication bias
- [ ] **Suspected** - Some evidence suggesting possible bias
- [ ] **Strongly suspected** - Clear evidence of publication bias

**Rating Decision:** No downgrade / Downgrade 1 level / Downgrade 2 levels

**Justification:** ________________________________

---

## Upgrading Factors (For Observational Studies Only)

### Upgrade Factor 1: Large Effect Size
**Assessment:** Is there a large or very large effect?

**Effect Size Magnitude:**
- Relative risk or odds ratio: ______
- Standardized effect size: ______
- Clinical significance threshold: ______

**Effect Size Categories:**
- [ ] **Large effect** (RR >2 or <0.5) → Upgrade 1 level
- [ ] **Very large effect** (RR >5 or <0.2) → Upgrade 2 levels  
- [ ] **Not applicable** → No upgrade

**Justification:** ________________________________

---

### Upgrade Factor 2: Dose-Response Relationship
**Assessment:** Is there evidence of a dose-response gradient?

**Dose-Response Evidence:**
- Clear gradient observed: Yes / No / Unclear
- Multiple dose/exposure levels: Yes / No
- Trend test significant: Yes / No / Not performed

**Relationship Characteristics:**
- [ ] **Clear dose-response** → Upgrade 1 level
- [ ] **Not applicable or unclear** → No upgrade

**Justification:** ________________________________

---

### Upgrade Factor 3: Opposing Plausible Confounding
**Assessment:** Would all plausible confounders reduce the demonstrated effect?

**Confounding Analysis:**
- Direction of likely confounding: Reduces effect / Increases effect / Unclear
- Magnitude of possible confounding: Large / Moderate / Small
- Adjustment for confounders: Yes / Partial / No

**Confounding Assessment:**
- [ ] **All plausible confounders would reduce effect** → Upgrade 1 level
- [ ] **Not applicable or unclear** → No upgrade

**Justification:** ________________________________

---

## Final GRADE Assessment

### Summary of Rating Changes

**Starting Level:** HIGH / LOW

**Risk of Bias:** -0 / -1 / -2 levels
**Inconsistency:** -0 / -1 / -2 levels  
**Indirectness:** -0 / -1 / -2 levels
**Imprecision:** -0 / -1 / -2 levels
**Publication Bias:** -0 / -1 / -2 levels

**Total Downgrading:** -______ levels

**Upgrading (Observational studies only):**
**Large Effect:** +0 / +1 / +2 levels
**Dose-Response:** +0 / +1 levels
**Opposing Confounding:** +0 / +1 levels

**Total Upgrading:** +______ levels

---

### Final Certainty Rating

**Final Certainty:** HIGH / MODERATE / LOW / VERY LOW

**Certainty Definitions:**
- **HIGH:** Very confident that the true effect lies close to the estimate of effect
- **MODERATE:** Moderately confident in the effect estimate; true effect is likely close to the estimate, but may be substantially different  
- **LOW:** Limited confidence in the effect estimate; true effect may be substantially different from the estimate
- **VERY LOW:** Very little confidence in the effect estimate; true effect is likely to be substantially different from the estimate

---

## Evidence Summary Table

| Outcome | Studies (n) | Participants/Observations | Effect Estimate (95% CI) | Certainty | Comments |
|---------|-------------|-------------------------|-------------------------|-----------|-----------|
| [Outcome 1] | | | | HIGH/MODERATE/LOW/VERY LOW | |
| [Outcome 2] | | | | HIGH/MODERATE/LOW/VERY LOW | |
| [Outcome 3] | | | | HIGH/MODERATE/LOW/VERY LOW | |

---

## Summary of Findings

### Main Results
**Effect Direction:** Beneficial / Harmful / No effect / Unclear
**Effect Magnitude:** Large / Moderate / Small / Negligible  
**Consistency:** Consistent / Mostly consistent / Inconsistent
**Precision:** Precise / Imprecise / Very imprecise

### Key Limitations
1. ________________________________
2. ________________________________  
3. ________________________________

### Applicability
**Direct Applicability:** High / Moderate / Low
**Population:** Applicable / Somewhat applicable / Limited applicability
**Intervention:** Applicable / Somewhat applicable / Limited applicability  
**Setting:** Applicable / Somewhat applicable / Limited applicability

### Implications for Practice
**Strength of Recommendation:** 
- [ ] Strong recommendation supported by high/moderate certainty evidence
- [ ] Conditional recommendation due to low/very low certainty evidence
- [ ] No recommendation possible due to insufficient evidence

**Clinical/Practical Significance:**
________________________________

---

## Quality Control

### Reviewer Information
**Primary Assessor:** ________________________________
**Secondary Assessor:** ________________________________
**Resolution of Disagreements:** Consensus / Third reviewer / Team discussion

### Assessment Validation
- [ ] All domains systematically assessed
- [ ] Judgments supported by evidence
- [ ] Consistent with GRADE methodology
- [ ] Reviewed by second assessor

### Documentation
- [ ] All decisions justified in writing
- [ ] Supporting quotes from studies included
- [ ] Missing information clearly noted
- [ ] Assessment form complete

---

**Assessment Completed by:** ________________________________  
**Date:** ________________________________
**Review Status:** Draft / Final / Revised

**Notes for Systematic Review Team:**
________________________________

---

## Appendix: GRADE Rating Examples for OWISAC Domain

### Communication Performance Examples

**SNR/SINR Improvements:**
- Large effect: >10 dB improvement
- Moderate effect: 3-10 dB improvement  
- Small effect: 1-3 dB improvement

**BER Improvements:**
- Large effect: >2 orders of magnitude improvement
- Moderate effect: 1-2 orders of magnitude improvement
- Small effect: <1 order of magnitude improvement

### Sensing Performance Examples

**Detection Performance:**
- Large effect: >20% improvement in detection probability
- Moderate effect: 10-20% improvement
- Small effect: 5-10% improvement

**Estimation Accuracy:**
- Large effect: >50% reduction in MSE
- Moderate effect: 20-50% reduction in MSE
- Small effect: 10-20% reduction in MSE

### Implementation Considerations
- Practical feasibility with current technology
- Scalability to realistic system sizes
- Power consumption and complexity trade-offs
- Environmental robustness and reliability