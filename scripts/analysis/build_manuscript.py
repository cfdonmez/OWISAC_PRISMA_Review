from pathlib import Path
import re

p = Path("scripts/analysis/build_manuscript.py")
s = p.read_text(encoding="utf-8")

old_block = """def expand_includes(text: str) -> str:
    def repl(m):
        p = Path(m.group(1))
        if not p.exists():
            return f"<!-- MISSING INCLUDE: {p} -->"
        # Görsel dosyaları Markdown embed
        if p.suffix.lower() in {'.png','.jpg','.jpeg','.gif','.svg'}:
            return f"![]({p.as_posix()})"
        try:
            return p.read_text(encoding="utf-8").strip()
        except Exception:
            return f"<!-- BINARY OR NON-UTF8 INCLUDE: {p} (skipped) -->"
    return INCLUDE_RE.sub(repl, text)
"""

new_block = """def expand_includes(text: str) -> str:
    def repl(m):
        p = Path(m.group(1))
        if not p.exists():
            return f"<!-- MISSING INCLUDE: {p} -->"
        # Görsel dosyaları Markdown embed
        if p.suffix.lower() in {'.png','.jpg','.jpeg','.gif','.svg'}:
            return f"![]({p.as_posix()})"
        try:
            return p.read_text(encoding="utf-8").strip()
        except Exception:
            return f"<!-- BINARY OR NON-UTF8 INCLUDE: {p} (skipped) -->"
    return INCLUDE_RE.sub(repl, text)
"""

if old_block in s:
    s = s.replace(old_block, new_block)
else:
    s = re.sub(r"def expand_includes\(text: str\).*?return INCLUDE_RE\.sub\(repl, text\)\n",
               new_block, s, flags=re.S)

p.write_text(s, encoding="utf-8")
print("[patched] build_manuscript.py updated to handle images safely")
