# Apply Commit 1 files: run this script INSIDE your repo root.
# It will create the required folders and copy in templates/docs/meta files.
# Usage:
#     python apply_commit1.py

import os, shutil

SRC = os.path.dirname(os.path.abspath(__file__))
REPO = os.getcwd()

def copytree(src, dst):
    for base, dirs, files in os.walk(src):
        rel = os.path.relpath(base, src)
        target = os.path.join(dst, rel) if rel != '.' else dst
        os.makedirs(target, exist_ok=True)
        for f in files:
            s = os.path.join(base, f)
            d = os.path.join(target, f)
            if os.path.exists(d):
                print(f"[skip] {os.path.relpath(d, dst)} exists")
                continue
            shutil.copy2(s, d)
            print(f"[add]  {os.path.relpath(d, dst)}")

if __name__ == "__main__":
    copytree(os.path.join(SRC, "templates"), os.path.join(REPO, "templates"))
    copytree(os.path.join(SRC, "docs"), os.path.join(REPO, "docs"))
    for fname in ["LICENSE", "CITATION.cff", "CONTRIBUTING.md"]:
        s = os.path.join(SRC, fname)
        d = os.path.join(REPO, fname)
        if os.path.exists(d):
            print(f"[skip] {fname} exists")
        else:
            shutil.copy2(s, d)
            print(f"[add]  {fname}")
    print("\nDone. Review changes, then commit.")
