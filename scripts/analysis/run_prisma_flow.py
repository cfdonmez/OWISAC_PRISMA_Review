import subprocess, sys

def run(cmd):
    p = subprocess.run(cmd, text=True)
    return p.returncode

# 1) Validate counts against schema
rc = run([sys.executable, "scripts/analysis/validate_prisma_counts.py"])
if rc != 0:
    sys.exit(rc)

# 2) If OK, build the flow figure
rc = run([sys.executable, "scripts/analysis/make_prisma_flow.py"])
sys.exit(rc)
