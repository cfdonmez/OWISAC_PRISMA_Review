# PROSPERO Registration Template for OWISAC Systematic Review

## Basic Information

### 1. Review Title
**Working Title:** A Systematic Review of Cascaded Optical Phased Array-Reconfigurable Intelligent Surface Architectures for Non-Line-of-Sight Optical Wireless Integrated Sensing and Communication Systems

**Alternative Title (if needed):** ________________________________

### 2. Original Language Title
If your review is not in English, provide the original language title here:
________________________________

### 3. Anticipated or Actual Start Date
**Start Date:** [MM/DD/YYYY] _________________
**Note:** This should be the date when screening begins, not when you start planning.

### 4. Anticipated Completion Date
**Completion Date:** [MM/DD/YYYY] _________________
**Note:** When you expect to submit for publication or complete the final report.

### 5. Stage of Review at Time of Submission

Check all that apply:
- [ ] Preliminary searches
- [ ] Piloting of the study selection process
- [ ] Formal screening of search results against eligibility criteria
- [ ] Data extraction
- [ ] Risk of bias (quality) assessment
- [ ] Data analysis

**Additional Notes:** ________________________________

---

## Review Team Details

### 6. Named Contact
**Name:** ________________________________
**Title/Position:** ________________________________
**Institution:** ________________________________

### 7. Named Contact Email
**Email:** ________________________________

### 8. Named Contact Address
**Full Address:**
________________________________
________________________________
**Country:** ________________________________

### 9. Named Contact Phone Number
**Phone:** ________________________________

### 10. Organizational Affiliation of Review
**Primary Organization:** ________________________________
**Department/Faculty:** ________________________________
**Additional Affiliations:** ________________________________

### 11. Review Team Members
List all team members and their roles:

**Team Member 1:**
- Name: ________________________________
- Email: ________________________________
- Institution: ________________________________
- Role: Lead investigator / Co-investigator / Data extractor / Statistician / Domain expert

**Team Member 2:**
- Name: ________________________________
- Email: ________________________________
- Institution: ________________________________
- Role: ________________________________

**Additional Members (add as needed):**
________________________________

---

## Funding and Support

### 12. Funding Sources/Sponsors
**Funding Organizations:**
- ________________________________
- ________________________________

**Grant Numbers:**
- ________________________________
- ________________________________

**Note:** Include "No funding" if applicable.

### 13. Conflicts of Interest
**Financial Conflicts:** ________________________________
**Academic Conflicts:** ________________________________
**Other Conflicts:** ________________________________
**Declaration:** None / See above

### 14. Collaborators
**External Collaborators:**
- Name: _________________ Institution: _________________ Role: _________________
- Name: _________________ Institution: _________________ Role: _________________

---

## Review Methods

### 15. Review Question(s)
**Primary Research Question:**
What are the principal technical challenges, proposed algorithms, and performance trade-offs in implementing cascaded OPA-RIS architectures for optical wireless ISAC in non-ideal channels?

**Secondary Research Questions:**
1. How do different OPA-RIS configurations affect communication and sensing performance trade-offs?
2. What are the optimal design strategies for mitigating atmospheric turbulence and non-line-of-sight propagation effects?
3. How do hardware constraints (phase quantization, response time) impact system performance?
4. What are the key performance metrics and benchmarks used for evaluation?

### 16. Searches
**Databases to be Searched:**
- [ ] IEEE Xplore Digital Library
- [ ] Scopus
- [ ] Web of Science
- [ ] Optica Publishing Group (Optics Express, Optics Letters)
- [ ] arXiv (physics.optics, eess.SP)
- [ ] SPIE Digital Library
- [ ] Google Scholar (for grey literature)

**Additional Sources:**
- [ ] Reference lists of included studies
- [ ] Forward citation searching
- [ ] Conference proceedings
- [ ] Technical reports
- [ ] Expert consultation

**Search Restriction:**
- **Date Range:** 2019 to present
- **Language:** English
- **Document Types:** Peer-reviewed articles, conference papers, preprints with adequate methods

**Sample Search Strategy (IEEE Xplore):**
```
(("optical phased array" OR OPA) AND 
 (RIS OR metasurface OR "reconfigurable intelligent surface" OR "intelligent reflecting surface") AND
 (ISAC OR "integrated sensing" OR "joint sensing and communication" OR JSC) AND
 ("non-line-of-sight" OR NLoS OR turbulence OR "Cn^2" OR "Fried parameter" OR Rytov OR scintillation) AND
 (optical OR photonic OR "free space optics" OR FSO))
```

**Most Recent Search Date:** ________________________________

### 17. URL to Search Strategy
**Repository/Protocol Location:** https://github.com/cfdonmez/OWISAC_PRISMA_Review
**OSF Registration:** https://doi.org/10.17605/OSF.IO/57VRJ

### 18. Condition or Domain Being Studied
**Domain:** Optical wireless communication and sensing systems
**Specific Focus:** Integrated sensing and communication (ISAC) using cascaded optical phased arrays and reconfigurable intelligent surfaces
**Application Context:** Non-line-of-sight optical wireless links with atmospheric turbulence

### 19. Participants/Population
**System Characteristics:**
- Optical wireless communication systems operating in free-space environments
- Systems utilizing optical phased arrays (OPA) for beam steering
- Systems incorporating reconfigurable intelligent surfaces (RIS) or optical metasurfaces
- Non-line-of-sight propagation scenarios
- Turbulent atmospheric channels

**Exclusions:**
- Pure RF-only systems without optical components
- Line-of-sight only systems
- Systems without sensing capability (communication-only)

### 20. Intervention(s), Exposure(s)
**Primary Interventions:**
- Cascaded OPA-RIS architectures (OPA→RIS, OPA↔RIS configurations)
- Joint beamforming and surface configuration optimization
- Wigner-domain joint design methods
- RIS-coded phase retrieval techniques
- Aperiodic/blue-noise RIS designs
- Robust pre-shaping algorithms for turbulence mitigation
- Hardware-aware optimization and calibration methods

**Intervention Categories:**
- Architectural: Single-hop vs. cascaded configurations
- Algorithmic: Optimization methods and signal processing
- Hardware: Phase quantization, response time constraints
- Environmental: Turbulence mitigation strategies

### 21. Comparator(s)/Control
**Comparison Groups:**
- Conventional optical systems (lenses, mirrors)
- Single-hop FSO systems
- OPA-only systems (without RIS)
- RIS-only systems (without OPA)
- RF-based ISAC systems
- Method ablations and baselines

**Note:** Comparator is not mandatory for inclusion but will be recorded when present.

### 22. Types of Study to be Included
**Study Designs:**
- [ ] Experimental studies (laboratory, field trials)
- [ ] Simulation studies
- [ ] Theoretical/analytical studies
- [ ] Hybrid studies (theory + simulation + experiment)
- [ ] Proof-of-concept demonstrations

**Quality Criteria:**
- Peer-reviewed publications or high-quality preprints
- Sufficient methodological detail for quality assessment
- Clear reporting of system parameters and performance metrics
- Appropriate performance evaluation methods

### 23. Context
**Setting:** Laboratory environments, outdoor testbeds, simulation environments
**Geographic Scope:** Global (no geographic restrictions)
**Time Frame:** 2019 to present (to capture recent advances in OPA and RIS technologies)
**Other Considerations:** Studies must address integrated sensing and communication functionality

### 24. Primary Outcome(s)
**Communication Performance:**
- Signal-to-noise ratio (SNR) or signal-to-interference-plus-noise ratio (SINR) in dB
- Bit error rate (BER) or error vector magnitude (EVM)
- Data throughput (bps) or spectral efficiency (bits/s/Hz)
- Outage probability or capacity metrics

**Sensing Performance:**
- Detection probability (PD) and false alarm rate (PFA)
- Estimation accuracy metrics (mean square error, Cramér-Rao bound)
- ROC curve characteristics (AUC)
- Range, velocity, or angle estimation performance

**System Performance:**
- Beam steering accuracy and range
- Peak sidelobe level (PSL) and integrated sidelobe ratio (ISLR)
- Half-power beamwidth (HPBW) and beam quality metrics
- Power consumption and computational complexity

**At least one primary outcome must be reported for study inclusion.**

### 25. Secondary Outcome(s)
**Technical Metrics:**
- Optical efficiency and insertion loss
- Channel estimation accuracy
- Convergence behavior of optimization algorithms
- Robustness to system impairments

**Practical Considerations:**
- Implementation complexity
- Hardware requirements
- Cost analysis (when available)
- Scalability characteristics

### 26. Data Extraction (Selection and Coding)
**Selection Process:**
- Two independent reviewers will screen titles and abstracts
- Full-text screening by two independent reviewers
- Conflicts resolved through discussion or third reviewer
- Reasons for exclusion will be documented

**Data Extraction:**
- Standardized extraction form (see repository)
- Two independent extractors per study
- Pilot testing of extraction forms
- Regular calibration meetings

**Key Data Items:**
- Study characteristics and design
- System specifications (OPA, RIS parameters)
- Channel conditions and environment
- Performance outcomes and metrics
- Risk of bias assessment factors

### 27. Risk of Bias (Quality) Assessment
**Assessment Tools:**
- Modified Cochrane Risk of Bias tool (RoB 2.0) for experimental studies
- ROBINS-I for non-randomized studies
- Domain-specific quality criteria for optical communication studies
- Custom assessment criteria for ISAC integration

**Quality Domains:**
- Study design and methodology appropriateness
- System implementation and configuration validity
- Measurement and data collection procedures
- Statistical analysis and interpretation
- Reporting transparency and completeness
- ISAC-specific integration assessment

**Assessment Process:**
- Two independent assessors per study
- Conflicts resolved through discussion
- Overall quality rating: Low risk / Some concerns / High risk

### 28. Strategy for Data Synthesis
**Synthesis Approach:**
- **Primary:** Narrative synthesis organized by technical pillars:
  1. Wigner-domain joint design (WD-JD)
  2. RIS-coded phase retrieval (RC-PR-T)
  3. Blue-noise RIS design (BN-RIS)
  4. Robust pre-shaping for turbulence (RPB-Kol)
  5. Hardware-aware implementation (HW-Q/CTRL)

**Quantitative Analysis:**
- Meta-analysis will be conducted if ≥3 homogeneous studies report comparable outcomes
- Random-effects models will be used due to expected heterogeneity
- Subgroup analyses by system architecture, channel conditions, and performance metrics

**Heterogeneity Assessment:**
- Statistical heterogeneity using I² statistic
- Clinical heterogeneity through study characteristics comparison
- Methodological heterogeneity through risk of bias assessment

**Sensitivity Analyses:**
- Exclusion of high risk of bias studies
- Analysis by study design (experimental vs. simulation)
- Analysis by publication type (journal vs. conference)

### 29. Analysis of Subgroups or Subsets
**Planned Subgroup Analyses:**

**By System Architecture:**
- OPA→RIS vs. OPA↔RIS configurations
- Single-element vs. multi-element systems
- Different phase quantization levels

**By Channel Conditions:**
- Turbulence strength (weak, moderate, strong)
- Propagation distance (short <100m, medium 100-1km, long >1km)
- Operating wavelength bands

**By Application Domain:**
- Communication-dominant vs. sensing-dominant systems
- Indoor vs. outdoor environments
- Static vs. mobile scenarios

**Subgroup Analysis Methods:**
- Test for interaction between subgroups
- Report effect sizes with confidence intervals for each subgroup
- Use meta-regression for continuous moderator variables

---

## Dissemination Plans

### 30. Type and Method of Review
**Review Type:** Systematic review with meta-analysis (if appropriate)
**Methodology Framework:** PRISMA 2020
**Registration:** PROSPERO + OSF pre-registration

### 31. Language
**Primary Language:** English
**Translation:** No translation required (English-only inclusion)

### 32. Country
**Primary Country:** Turkey
**Multi-national Team:** Yes (if applicable)

### 33. Other Registration Details
**Other Registrations:** Open Science Framework (OSF)
**OSF DOI:** https://doi.org/10.17605/OSF.IO/57VRJ
**Protocol Amendments:** All amendments will be documented in protocol log

### 34. Reference and/or URL for Published Protocol
**GitHub Repository:** https://github.com/cfdonmez/OWISAC_PRISMA_Review
**Protocol File:** `/protocol/prisma_protocol.md`
**Access:** Public repository with open access

### 35. Dissemination Plans
**Primary Publication:** High-impact journal in optical communications or systems engineering
**Target Journals:** 
- IEEE Transactions on Communications
- Journal of Lightwave Technology  
- IEEE Transactions on Wireless Communications
- Optics Express

**Additional Dissemination:**
- Conference presentations at major optical communication conferences
- Preprint on arXiv
- Open access publication when possible
- Summary reports for practitioners

### 36. Keywords
**Primary Keywords:**
- Optical phased array (OPA)
- Reconfigurable intelligent surface (RIS)
- Integrated sensing and communication (ISAC)
- Non-line-of-sight (NLoS)
- Optical wireless communication
- Free-space optics
- Atmospheric turbulence
- Systematic review
- PRISMA 2020

### 37. Details of Any Existing Review of the Same Topic
**Literature Search Results:**
- No existing systematic reviews identified on this specific topic
- Several narrative reviews on related topics (OPA, RIS, ISAC separately)
- Justification for new review: First comprehensive systematic synthesis of cascaded OPA-RIS for ISAC

### 38. Current Review Status
**Status:** ☐ Ongoing ☐ Completed ☐ Discontinued ☐ Other: ________________
**Completion Percentage:** _____%
**Expected Completion:** ________________

---

## Additional Information

### 39. Any Other Information
**Special Considerations:**
- Rapid evolution of the field requires quarterly search updates
- Close collaboration with domain experts for technical validation
- Plan to update review as living systematic review if significant new evidence emerges

**Contact for Updates:**
- Primary contact information above
- GitHub repository for real-time updates
- OSF project for protocol amendments

### 40. Details of Final Report/Publication Plans
**Manuscript Structure:** PRISMA 2020 compliant full-length systematic review
**Target Length:** 8,000-12,000 words
**Supplementary Materials:** Full search strategies, excluded studies list, extracted data tables
**Open Science Commitment:** All materials will be made openly available

---

**Submission Checklist:**
- [ ] All required fields completed
- [ ] Search strategy tested and documented  
- [ ] Team roles and responsibilities defined
- [ ] Conflicts of interest declared
- [ ] Dissemination plan established
- [ ] Repository and registration links verified

**Submitted by:** ________________________________
**Date:** ________________________________
**PROSPERO ID:** (To be assigned)