# Comprehensive Data Extraction Template for OWISAC Systematic Review

## Instructions for Use
This template is designed for extracting data from studies included in systematic reviews of Optical Wireless Integrated Sensing and Communication (OWISAC) systems. Complete one form per study. Use "NR" for not reported and "NA" for not applicable.

## Study Identification

| Field | Description | Entry |
|-------|-------------|--------|
| Record ID | Unique identifier (e.g., FirstAuthor2024) | |
| DOI/ArXiv ID | Digital object identifier or ArXiv ID | |
| PubMed ID | PubMed identifier if available | |
| Title | Complete study title | |
| Authors | All authors (Last name, First initial) | |
| Year | Publication year | |
| Journal/Conference | Publication venue | |
| Volume/Issue | Journal volume and issue or conference details | |
| Pages | Page numbers | |
| Language | Publication language | |
| Country | Country of corresponding author | |
| Funding Source | Reported funding sources | |

## Study Characteristics

### Study Design
| Field | Options | Entry |
|-------|---------|-------|
| Study Type | Experimental/Simulation/Theoretical/Review/Mixed | |
| Study Setting | Laboratory/Field/Simulation/Hybrid | |
| Duration | Study duration in months | |
| Sample Size | Number of experiments/scenarios/trials | |
| Control Group | Yes/No/Multiple | |
| Blinding | Yes/No/Partial/NA | |
| Randomization | Yes/No/Quasi/NA | |

### Population/System Characteristics
| Field | Description | Entry |
|-------|-------------|-------|
| System Architecture | OPA-only/RIS-only/OPA-RIS/Other | |
| Channel Type | LoS/NLoS/Mixed/Turbulent | |
| Operating Frequency | Frequency or wavelength | |
| Distance Range | Communication range (meters) | |
| Environment | Indoor/Outdoor/Mixed | |

## Technical Specifications

### Optical Phased Array (OPA) Parameters
| Parameter | Units | Value | Notes |
|-----------|-------|-------|-------|
| Number of Elements | Count | | |
| Element Spacing | μm or λ | | |
| Aperture Size | mm² | | |
| Phase Resolution | bits | | |
| Beam Steering Range | degrees | | |
| Scan Rate | Hz | | |
| Wavelength | nm | | |
| Optical Power | mW | | |
| Efficiency | % | | |

### RIS/Metasurface Parameters  
| Parameter | Units | Value | Notes |
|-----------|-------|-------|-------|
| Number of Elements | Count | | |
| Element Size | μm | | |
| Unit Cell Pitch | μm | | |
| Phase States | Count | | |
| Response Time | ms | | |
| Operating Bandwidth | nm | | |
| Reflection Efficiency | % | | |
| Insertion Loss | dB | | |
| Control Method | Digital/Analog/Hybrid | | |

### Channel and Propagation
| Parameter | Units | Value | Notes |
|-----------|-------|-------|-------|
| Total Path Length | m | | |
| NLoS Geometry | Single-bounce/Multi-bounce | | |
| Atmospheric Conditions | Clear/Turbulent/Adverse | | |
| Cn² | m^(-2/3) | | |
| Fried Parameter (r0) | m | | |
| Rytov Variance | Dimensionless | | |
| Visibility | km | | |
| Wind Speed | m/s | | |

## ISAC Specifications

### Communication Parameters
| Parameter | Units | Value | Notes |
|-----------|-------|-------|-------|
| Data Rate | Gbps/Mbps | | |
| Modulation Scheme | OOK/PPM/PAM/Other | | |
| Error Correction | Type and rate | | |
| Symbol Rate | symbols/s | | |
| Signal Bandwidth | MHz/GHz | | |

### Sensing Parameters
| Parameter | Units | Value | Notes |
|-----------|-------|-------|-------|
| Sensing Range | m | | |
| Range Resolution | m | | |
| Velocity Resolution | m/s | | |
| Angular Resolution | degrees | | |
| Detection Probability | % | | |
| False Alarm Rate | % | | |
| Target Type | Point/Extended/Multiple | | |
| Sensing Accuracy | % or absolute | | |

## Outcomes and Results

### Primary Communication Outcomes
| Outcome | Units | Baseline | Intervention | Effect Size | CI/SE | P-value | Notes |
|---------|-------|----------|-------------|-------------|-------|---------|-------|
| SNR | dB | | | | | | |
| SINR | dB | | | | | | |
| BER | Log scale | | | | | | |
| EVM | % | | | | | | |
| Throughput | Gbps | | | | | | |
| Capacity | bits/s/Hz | | | | | | |
| Outage Probability | % | | | | | | |

### Primary Sensing Outcomes  
| Outcome | Units | Baseline | Intervention | Effect Size | CI/SE | P-value | Notes |
|---------|-------|----------|-------------|-------------|-------|---------|-------|
| Detection Probability | % | | | | | | |
| False Alarm Rate | % | | | | | | |
| Mean Square Error | Units vary | | | | | | |
| Cramér-Rao Bound | Units vary | | | | | | |
| ROC AUC | 0-1 | | | | | | |
| Estimation Accuracy | % | | | | | | |

### Beam/Optical Performance
| Outcome | Units | Baseline | Intervention | Effect Size | CI/SE | P-value | Notes |
|---------|-------|----------|-------------|-------------|-------|---------|-------|
| Peak Sidelobe Level | dB | | | | | | |
| Integrated Sidelobe Ratio | dB | | | | | | |
| Half-Power Beamwidth | degrees | | | | | | |
| Beam Steering Accuracy | degrees | | | | | | |
| Optical Efficiency | % | | | | | | |
| Gain | dB | | | | | | |

### System Performance
| Outcome | Units | Baseline | Intervention | Effect Size | CI/SE | P-value | Notes |
|---------|-------|----------|-------------|-------------|-------|---------|-------|
| Power Consumption | W | | | | | | |
| Processing Time | ms | | | | | | |
| Memory Usage | MB/GB | | | | | | |
| Convergence Time | iterations | | | | | | |
| Complexity | O(n) notation | | | | | | |

## Methodological Quality Assessment

### Study Design Quality
| Aspect | Rating (1-5) | Comments |
|--------|-------------|----------|
| Objectives Clarity | | |
| Method Description | | |
| Parameter Definition | | |
| Baseline Establishment | | |
| Control Implementation | | |
| Statistical Analysis | | |

### Technical Rigor
| Aspect | Yes/No/Partial | Comments |
|--------|----------------|----------|
| Realistic Channel Model | | |
| Appropriate Baselines | | |
| Fair Comparison | | |
| Statistical Significance | | |
| Reproducible Methods | | |
| Code/Data Availability | | |

## Risk of Bias Assessment

### Selection Bias
| Domain | Low/Some Concerns/High | Justification |
|--------|----------------------|---------------|
| System Selection | | |
| Parameter Selection | | |
| Scenario Selection | | |

### Performance Bias  
| Domain | Low/Some Concerns/High | Justification |
|--------|----------------------|---------------|
| Implementation | | |
| Measurement | | |
| Analysis | | |

### Detection Bias
| Domain | Low/Some Concerns/High | Justification |
|--------|----------------------|---------------|
| Outcome Assessment | | |
| Selective Reporting | | |

### Attrition Bias
| Domain | Low/Some Concerns/High | Justification |
|--------|----------------------|---------------|
| Incomplete Data | | |
| Lost Experiments | | |

### Reporting Bias
| Domain | Low/Some Concerns/High | Justification |
|--------|----------------------|---------------|
| Selective Outcome Reporting | | |
| Incomplete Results | | |

**Overall Risk of Bias:** Low / Some Concerns / High

## Additional Information

### Algorithms and Methods
| Aspect | Description |
|--------|-------------|
| Optimization Algorithm | |
| Beam Forming Method | |
| Channel Estimation | |
| Sensing Algorithm | |
| ISAC Integration Approach | |

### Innovations and Contributions
| Aspect | Description |
|--------|-------------|
| Novel Contributions | |
| Technical Innovations | |
| Theoretical Advances | |
| Practical Applications | |

### Limitations
| Aspect | Description |
|--------|-------------|
| Reported Limitations | |
| Methodological Concerns | |
| Generalizability Issues | |
| Missing Information | |

## Extractor Information
| Field | Entry |
|-------|-------|
| Extractor Name | |
| Date of Extraction | |
| Review Notes | |
| Conflicts of Interest | |
| Verification Status | |

## Data Verification
| Field | Yes/No | Notes |
|-------|--------|-------|
| Double Extraction | | |
| Conflicts Resolved | | |
| Author Contact Required | | |
| Additional Data Sources | | |

---

**Instructions for Extractors:**
1. Complete all relevant sections - use "NR" for not reported, "NA" for not applicable
2. For numerical values, include units and confidence intervals when available  
3. In the Notes columns, record any assumptions, conversions, or clarifications
4. Flag any unusual findings or methodological concerns
5. When in doubt, extract conservatively and note uncertainty
6. Contact review team for complex cases or conflicts

**Quality Control:**
- Each form should be reviewed by a second extractor
- Conflicts should be resolved through discussion or third-party arbitration
- Regular calibration exercises should be conducted
- Extraction forms should be pilot tested before full implementation

This comprehensive template ensures systematic and complete data extraction for high-quality synthesis in your OWISAC systematic review.