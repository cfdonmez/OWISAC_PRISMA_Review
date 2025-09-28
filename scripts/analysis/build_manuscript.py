from pathlib import Path
import re

sections = [
    "00_abstract.md",
    "01_introduction.md",
    "02_methods.md",
    "03_results.md",
    "04_discussion.md",
    "05_conclusion.md",
    "06_acknowledgments.md",
    "07_references.md",
]

out_file = Path("manuscript/full_article.md")
out_file.parent.mkdir(exist_ok=True)

INCLUDE_RE = re.compile(r"<!--\s*INCLUDE:\s*(.+?)\s*-->")

def expand_includes(text: str) -> str:
    def repl(m):
        p = Path(m.group(1))
        if p.exists():
            return p.read_text(encoding="utf-8").strip()
        return f"<!-- MISSING INCLUDE: {p} -->"
    return INCLUDE_RE.sub(repl, text)

with out_file.open("w", encoding="utf-8") as out:
    for sec in sections:
        p = Path("manuscript/sections") / sec
        if p.exists():
            raw = p.read_text(encoding="utf-8").strip()
            expanded = expand_includes(raw)
            out.write(expanded)
            out.write("\n\n")
        else:
            out.write(f"<!-- Missing section: {sec} -->\n\n")

print(f"[ok] Built {out_file} (includes expanded)")