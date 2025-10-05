#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
repo_inventory.py — GitHub/Git deposu dosya envanteri -> CSV

Çıktı sütunları:
repo_root, path_rel, name, ext, parent, depth, size_bytes, mtime_iso, git_tracked
"""

import argparse, csv, hashlib, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

def is_git_repo(path: Path) -> bool:
    try:
        subprocess.run(["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False

def load_git_tracked_set(repo_root: Path):
    try:
        out = subprocess.check_output(
            ["git", "-C", str(repo_root), "ls-files", "--full-name"],
            text=True
        )
        return set(p.strip() for p in out.splitlines() if p.strip())
    except Exception:
        return set()

def should_skip(path: Path, repo_root: Path, exclude_patterns):
    rel = path.relative_to(repo_root).as_posix()
    # default exclusions
    defaults = [
        ".git/", ".github/", ".venv/", "venv/", "__pycache/", ".mypy_cache/",
        ".pytest_cache/", ".idea/", ".vscode/", ".DS_Store", "node_modules/",
        ".ruff_cache/", ".eggs/", "build/", "dist/", ".next/", ".cache/"
    ]
    patterns = defaults + exclude_patterns
    for pat in patterns:
        # klasör benzeri eşleşme
        if pat.endswith("/") and rel.startswith(pat):
            return True
        # dosya/desen eşleşmesi (basit contains)
        if pat and pat in rel:
            return True
    return False

def mtime_iso(p: Path):
    try:
        ts = p.stat().st_mtime
        return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
    except Exception:
        return ""

def size_bytes(p: Path):
    try:
        return p.stat().st_size
    except Exception:
        return ""

def main():
    ap = argparse.ArgumentParser(description="Depodaki tüm dosyaları CSV olarak envanterle.")
    ap.add_argument("repo_root", help="Depo kök klasörü (ör. /path/to/repo)")
    ap.add_argument("-o", "--out", default="repo_inventory.csv", help="Çıkış CSV dosyası")
    ap.add_argument("-e", "--exclude", action="append", default=[],
                    help="Hariç tutma deseni (çoklu kullanılır). Örn: -e data/raw/ -e .ipynb_checkpoints")
    ap.add_argument("--include-hidden", action="store_true",
                    help="Gizli dosyaları/klasörleri dahil et (varsayılan: hariç).")
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    if not repo_root.exists():
        print(f"Hata: {repo_root} bulunamadı.", file=sys.stderr)
        sys.exit(1)
    if not repo_root.is_dir():
        print(f"Hata: {repo_root} bir klasör değil.", file=sys.stderr)
        sys.exit(1)

    git_on = is_git_repo(repo_root)
    tracked = load_git_tracked_set(repo_root) if git_on else set()

    rows = []
    for p in repo_root.rglob("*"):
        if p.is_dir():
            # Sadece dosyaları raporlayacağız; dizinleri atla
            continue
        # Gizli dosya/klasörleri atla (istemezsen --include-hidden kullan)
        if not args.include_hidden:
            parts = p.relative_to(repo_root).parts
            if any(part.startswith(".") for part in parts if part not in (".", "..")):
                continue
        if should_skip(p, repo_root, args.exclude):
            continue

        rel = p.relative_to(repo_root)
        parent = rel.parent.as_posix()
        depth = len(rel.parts) - 1
        name = p.name
        ext = p.suffix
        sz = size_bytes(p)
        mt = mtime_iso(p)
        rel_posix = rel.as_posix()
        git_tr = "yes" if rel_posix in tracked else ("no" if git_on else "")
        rows.append({
            "repo_root": str(repo_root),
            "path_rel": rel_posix,
            "name": name,
            "ext": ext,
            "parent": parent,
            "depth": depth,
            "size_bytes": sz,
            "mtime_iso": mt,
            "git_tracked": git_tr,
        })

    # Tutarlı, deterministik sıralama (önce klasör derinliği, sonra alfabetik)
    rows.sort(key=lambda r: (r["depth"], r["parent"], r["name"]))

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else
                                ["repo_root","path_rel","name","ext","parent","depth","size_bytes","mtime_iso","git_tracked"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"✔ Yazıldı: {args.out}  (Toplam dosya: {len(rows)})")

if __name__ == "__main__":
    main()
