#!/usr/bin/env python3
import csv, os, sys
from collections import Counter, defaultdict

INCLUDED = sys.argv[1] if len(sys.argv) > 1 else "data/included_studies.csv"
OUT_DIR = "results/synthesis_tables"

PILLAR_COLS = ["pillar_WD_JD","pillar_RC_PR_T","pillar_BN_RIS","pillar_RPB_Kol","pillar_HW_Q_CTRL"]
METRIC_COLS = ["snr_db","sinr_db","ber","evm_pct","psl_db","islr_db","hpbw_deg","contrast","roc_auc","crb_unit"]
HW_COLS = ["opa_N_elements","opa_phase_bits","opa_scan_range_deg","ris_size_elems","ris_phase_states","ris_response_ms","ris_fill_factor"]
TURB_COLS = ["Cn2","r0_m","rytov_var","nlos_geometry","z_total_m"]

def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames

def nonempty(x):
    return x is not None and str(x).strip() != ""

def write_csv(path, header, rows):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in rows:
            w.writerow(row)

def main():
    rows, fields = read_rows(INCLUDED)

    # 1) Pillar coverage
    pillar_counts = Counter()
    for r in rows:
        for c in PILLAR_COLS:
            if c in fields and str(r.get(c,"")).lower() == "true":
                pillar_counts[c] += 1
    write_csv(os.path.join(OUT_DIR,"pillars_summary.csv"),
              ["pillar","count"], [[k,v] for k,v in pillar_counts.items()])

    # 2) Metrics coverage (kaç kayıtta bu metrik doldurulmuş?)
    metric_counts = []
    for c in METRIC_COLS:
        if c in fields:
            cnt = sum(1 for r in rows if nonempty(r.get(c)))
            metric_counts.append([c, cnt])
    write_csv(os.path.join(OUT_DIR,"metrics_coverage.csv"),
              ["metric","nonempty_count"], metric_counts)

    # 3) Hardware awareness (OPA/RIS alanları ne kadar dolu?)
    hw_counts = []
    for c in HW_COLS:
        if c in fields:
            cnt = sum(1 for r in rows if nonempty(r.get(c)))
            hw_counts.append([c, cnt])
    write_csv(os.path.join(OUT_DIR,"hardware_awareness.csv"),
              ["field","nonempty_count"], hw_counts)

    # 4) Turbulence params coverage
    turb_counts = []
    for c in TURB_COLS:
        if c in fields:
            cnt = sum(1 for r in rows if nonempty(r.get(c)))
            turb_counts.append([c, cnt])
    write_csv(os.path.join(OUT_DIR,"turbulence_params.csv"),
              ["field","nonempty_count"], turb_counts)

    print("Built synthesis tables under results/synthesis_tables/")

if __name__ == "__main__":
    main()
