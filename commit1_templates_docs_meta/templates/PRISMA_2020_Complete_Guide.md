# Comprehensive PRISMA 2020 Implementation Guide

## Overview
This document provides a complete implementation guide for creating a systematic review following PRISMA 2020 guidelines, specifically designed to complement your OWISAC (Optical Wireless Integrated Sensing and Communication) PRISMA Review repository.

## Repository Structure Enhancement

Your current repository structure is excellent. Here are recommendations for additional components:

```
├── templates/
│   ├── prisma_2020_checklist_detailed.xlsx
│   ├── data_extraction_template_comprehensive.xlsx  
│   ├── risk_of_bias_templates/
│   │   ├── rob2_template.xlsx
│   │   ├── robins_i_template.xlsx
│   │   └── custom_rob_template.xlsx
│   ├── grade_assessment_template.xlsx
│   └── prospero_registration_template.docx
├── workflows/
│   ├── screening_workflow.md
│   ├── quality_assurance_checklist.md
│   └── manuscript_preparation_guide.md
├── tools/
│   ├── search_string_generator.py
│   ├── duplicate_checker.py
│   └── citation_formatter.py
└── examples/
    ├── sample_manuscripts/
    ├── completed_templates/
    └── best_practice_examples/
```

## PRISMA 2020 Complete 27-Item Checklist

### Title and Abstract
1. **Title** - Identify the report as a systematic review
2. **Abstract** - See PRISMA 2020 for Abstracts checklist

### Introduction  
3. **Rationale** - Describe rationale in context of existing knowledge
4. **Objectives** - Provide explicit statement of objectives/questions

### Methods
5. **Eligibility criteria** - Specify inclusion/exclusion criteria and study grouping
6. **Information sources** - Specify all databases, registers, websites, organizations searched
7. **Search strategy** - Present full search strategies for all sources
8. **Selection process** - Specify methods for deciding study inclusion
9. **Data collection process** - Explain methods for collecting data from studies
10. **Data items** - List and define all outcomes and variables sought
11. **Study risk of bias assessment** - Specify methods for assessing bias
12. **Effect measures** - Specify effect measures used for each outcome
13. **Synthesis methods** - Describe processes for synthesizing evidence
14. **Reporting bias assessment** - Describe methods for assessing reporting bias
15. **Certainty assessment** - Describe methods for assessing certainty of evidence

### Results
16a. **Study selection** - Describe search and selection results with flow diagram
16b. **Study selection** - Cite excluded studies and explain exclusions
17. **Study characteristics** - Cite and present characteristics of included studies
18. **Risk of bias in studies** - Present risk of bias assessments
19. **Results of individual studies** - Present summary statistics and effect estimates
20a. **Results of syntheses** - Summarize characteristics and bias of contributing studies
20b. **Results of syntheses** - Present results of all statistical syntheses
20c. **Results of syntheses** - Present results of all investigations of possible causes of differences
20d. **Results of syntheses** - Present results of all sensitivity analyses
21. **Reporting biases** - Present assessments of risk of bias due to missing results
22. **Certainty of evidence** - Present assessments of certainty for each outcome

### Discussion
23a. **Discussion** - Provide general interpretation of results
23b. **Discussion** - Discuss limitations of evidence included in review
23c. **Discussion** - Discuss limitations of review processes used
23d. **Discussion** - Discuss implications for practice, policy, and future research

### Other Information
24a. **Registration and protocol** - Provide registration information
24b. **Registration and protocol** - Indicate where protocol can be accessed
24c. **Registration and protocol** - Describe amendments to information
25. **Support** - Describe sources of financial support
26. **Competing interests** - Declare any competing interests
27. **Availability of data, code, and other materials** - Report availability

## Implementation Workflow

### Phase 1: Planning and Protocol Development
1. **Research Question Formulation**
   - Use PICO(T) framework
   - Ensure alignment with ISAC domain requirements
   - Validate with domain experts

2. **Protocol Development**
   - Complete PROSPERO registration
   - Develop comprehensive search strategy
   - Create inclusion/exclusion criteria
   - Design data extraction forms

### Phase 2: Search and Selection
1. **Systematic Search**
   - Execute searches across all planned databases
   - Document search strategies and results
   - Export and manage citations

2. **Study Selection**
   - Remove duplicates
   - Screen titles/abstracts (dual reviewers)
   - Full-text screening (dual reviewers)
   - Document reasons for exclusion

### Phase 3: Data Extraction and Quality Assessment
1. **Data Extraction**
   - Pilot extraction forms
   - Extract data (dual extractors)
   - Resolve conflicts through consensus

2. **Quality Assessment**
   - Apply appropriate risk of bias tools
   - Assess methodological quality
   - Grade certainty of evidence using GRADE

### Phase 4: Synthesis and Reporting
1. **Data Synthesis**
   - Narrative synthesis
   - Quantitative synthesis (if appropriate)
   - Subgroup analyses

2. **Manuscript Preparation**
   - Follow PRISMA 2020 checklist
   - Create flow diagram
   - Prepare tables and figures

## Risk of Bias Assessment Tools Guide

### For Randomized Controlled Trials
- **RoB 2.0** (Cochrane Risk of Bias Tool Version 2)
  - Domains: Randomization, deviations from intended interventions, missing outcome data, measurement of outcome, selection of reported result
  - Judgments: Low risk, Some concerns, High risk

### For Non-Randomized Studies
- **ROBINS-I** (Risk Of Bias In Non-randomized Studies - of Interventions)
  - Domains: Confounding, selection of participants, classification of interventions, deviations from intended interventions, missing data, measurement of outcomes, selection of reported result

### For Your OWISAC Domain
Consider developing custom risk of bias criteria for:
- Optical system characterization completeness
- Channel modeling accuracy
- Performance metric standardization
- Experimental setup realism

## GRADE Assessment Implementation

### Four Levels of Certainty
1. **High** - Very confident that true effect lies close to estimate
2. **Moderate** - Moderately confident in effect estimate  
3. **Low** - Limited confidence; true effect may be substantially different
4. **Very Low** - Very little confidence; true effect likely substantially different

### Five Domains for Rating Down
1. **Risk of bias** - Study design and execution limitations
2. **Inconsistency** - Heterogeneity in results across studies
3. **Indirectness** - Evidence from different populations, interventions, or outcomes
4. **Imprecision** - Wide confidence intervals, small sample sizes
5. **Publication bias** - Selective reporting of results

### Three Domains for Rating Up (Observational Studies Only)
1. **Large effect** - Substantial beneficial or harmful effect
2. **Dose-response** - Evidence of dose-response relationship
3. **Opposing plausible confounding** - Residual confounding would reduce demonstrated effect

## Quality Assurance Procedures

### Screening Quality Control
- Inter-rater reliability assessment (Cohen's kappa ≥ 0.80)
- Regular calibration sessions
- Third reviewer for conflicts

### Data Extraction Quality Control
- Pilot testing with 5-10 studies
- Double data extraction for all studies
- Standardized extraction forms
- Regular team meetings for clarification

### Synthesis Quality Control
- Pre-specified analysis plan
- Sensitivity analyses
- Subgroup analyses justification
- Publication bias assessment

## Automation and Tools Integration

### Search Strategy Management
```python
# Example search strategy documentation
search_strategies = {
    'ieee_xplore': {
        'query': '("optical phased array" OR OPA) AND (RIS OR metasurface)',
        'filters': ['2019-2025', 'English'],
        'results': 1250,
        'date_searched': '2025-09-17'
    }
}
```

### Citation Management
- Use Zotero/Mendeley for reference management
- Implement systematic tagging system
- Regular backup procedures

### Data Analysis Scripts
- Python scripts for quantitative synthesis
- R scripts for meta-analysis (if applicable)
- Automated table/figure generation

## Reporting and Dissemination

### Manuscript Structure
1. **Title Page** - PRISMA 2020 compliant title
2. **Abstract** - Structured abstract following PRISMA for Abstracts
3. **Introduction** - Rationale and objectives
4. **Methods** - Complete methodology description
5. **Results** - PRISMA flow diagram, study characteristics, synthesis results
6. **Discussion** - Interpretation, limitations, conclusions
7. **References** - Complete citation list
8. **Supplementary Materials** - Additional data, search strategies, excluded studies

### Transparency and Reproducibility
- Open Science Framework registration
- GitHub repository with all materials
- Raw data and analysis code availability
- Comprehensive supplementary materials

## Timeline and Milestones

### Month 1-2: Planning
- [ ] Protocol development
- [ ] PROSPERO registration
- [ ] Search strategy finalization
- [ ] Team training

### Month 3-4: Search and Selection  
- [ ] Systematic searches
- [ ] Duplicate removal
- [ ] Title/abstract screening
- [ ] Full-text screening

### Month 5-6: Data Extraction
- [ ] Form piloting
- [ ] Data extraction
- [ ] Quality assessment
- [ ] Data verification

### Month 7-8: Analysis and Synthesis
- [ ] Statistical analysis
- [ ] GRADE assessment
- [ ] Sensitivity analyses
- [ ] Results interpretation

### Month 9-10: Reporting
- [ ] Manuscript drafting
- [ ] Internal review
- [ ] External peer review
- [ ] Revision and submission

This guide provides the foundation for implementing a comprehensive, high-quality systematic review following PRISMA 2020 guidelines in your specific domain of optical wireless ISAC systems.