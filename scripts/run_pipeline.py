import subprocess, sys

STEPS = [
  ("Validate data files",                [sys.executable, "scripts/analysis/validate_data_files.py"]),
  ("Compute PRISMA counts",              [sys.executable, "scripts/analysis/compute_prisma_counts.py"]),
  ("Validate PRISMA counts",             [sys.executable, "scripts/analysis/validate_prisma_counts.py"]),
  ("Build PRISMA flow figure",           [sys.executable, "scripts/analysis/make_prisma_flow.py"]),
  ("Synthesis validate",                 [sys.executable, "scripts/analysis/synth_validate.py"]),
  ("Synthesis build tables",             [sys.executable, "scripts/analysis/synth_build_table.py"]),
  ("Build manuscript",                   [sys.executable, "scripts/analysis/build_manuscript.py"]),
]

def run_step(name, cmd):
  print(f"\n=== {name} ===")
  rc = subprocess.run(cmd, text=True).returncode
  if rc != 0:
    print(f"[fail] {name} (exit {rc})")
    sys.exit(rc)
  print(f"[ok] {name}")

def main():
  for name, cmd in STEPS:
    run_step(name, cmd)
  print("\n[ok] Pipeline completed successfully.")

if __name__ == "__main__":
  main()
