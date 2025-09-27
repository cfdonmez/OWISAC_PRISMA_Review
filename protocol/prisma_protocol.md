# Protocol for Systematic Review

**Title:** A Systematic Review of Cascaded OPA–RIS Architectures for NLoS Optical Wireless ISAC

**Short title:** OPA–RIS for NLoS Optical ISAC

**Date generated:** 2025-09-28

## Protocol & Registration

- OSF: <add OSF link/DOI>
- PROSPERO: <add PROSPERO ID>

## Timeframe

- From: 2019-01-01
- To: 2025-12-31

## Information Sources (Databases & Interfaces)

- IEEE Xplore (interface: web)
- Scopus (interface: web)
- Web of Science (interface: web)
- arXiv (interface: api)

## Search Strategy

### Query Strings
- **OPA+RIS+ISAC**: `("optical phased array" OR OPA) AND (RIS OR metasurface) AND (ISAC OR "integrated sensing and communication")`

- Grey literature: yes
- Last search run: <add ISO datetime>

## Eligibility Criteria
### Inclusion

- Optical wireless ISAC or closely related optical sensing+comm
- OPA and/or RIS explicitly involved
- NLoS or blockage mitigation addressed

### Exclusion

- Pure RF without optical adaptation
- Theoretical pieces without optical relevance
- No methods or performance metrics

## Research Questions

- RQ1: Which OPA–RIS designs enable reliable NLoS optical links under turbulence?
- RQ2: What sensing–communication trade-offs (SINR vs. contrast) emerge?
- RQ3: Which channel/propagation models are used and validated?

## Core Data Items for Extraction

- citation
- year
- architecture_components
- turbulence_params
- beamforming_strategy
- metrics:(SINR, contrast, BER, HPBW, PSL)

> This protocol is **auto-generated** from `config/review.yml` (SSOT). Edit the YAML to update this document.
