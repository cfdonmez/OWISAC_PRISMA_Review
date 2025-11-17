# Active Context

**Now:**
- Status: Providing a plan of action.
- Blockers: None.
- Next actions:
  - [ ] Data Extraction and Validation: Ensure the `included_studies.csv` file contains the minimum required fields and QA flags are properly set. Address any warnings found in the `results/qa_data_report.txt`.
  - [ ] PRISMA Flow Diagram and Counts: Verify the generation of the PRISMA flow diagram and counts. Ensure that the counts in `results/prisma_counts.json` are accurate and the diagram in `results/figures/prisma_flow.png` is complete.
  - [ ] Synthesis Tables: Build and verify the synthesis tables. Run the scripts `scripts/analysis/synth_build_subgroups.py` and `scripts/analysis/synth_build_architectures.py` and verify the outputs in `results/synthesis_tables/`.
  - [ ] Manuscript Generation: Compile the manuscript sections in the `manuscript/` directory into a full article. Use the script `scripts/analysis/build_manuscript.py` to generate the manuscript.
  - [ ] OSF Registration: Prepare the OSF registration steps and protocol templates.

**Memory Bank:**
- Project Brief: PRISMA 2020 compliant systematic review and synthesis makalesi (OW-ISAC: OPA→RIS, NLoS & türbülans, birlikte ışın şekillendirme/SINR-kontrast).
- Product Context: Akademik okuyucu (haberleşme/fotonik), doktora jürisi.
- Tech Context: Python 3.10+, `pip install -r requirements.txt`, `python scripts/run_pipeline.py`.
- Data contracts: `included_studies.csv` min fields: record_id, title, venue, year, doi, scenario, hardware, metrics, tags. QA flags: `optical_ok`, `opa_ok`, `ris_ok`, `casc_ok`, `chan_ok`, `tech_ok`
