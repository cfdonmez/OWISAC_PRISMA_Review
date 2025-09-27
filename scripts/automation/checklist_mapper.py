from pathlib import Path

# Basit eşleme tablosu: item no -> ilgili section dosyası
MAPPING = {
    "Item 2": "manuscript/sections/00_abstract.md",
    "Item 3": "manuscript/sections/01_introduction.md",
    "Item 4": "manuscript/sections/01_introduction.md",
    "Item 5": "manuscript/sections/02_methods.md",
    "Item 6": "manuscript/sections/02_methods.md",
    "Item 7": "manuscript/sections/02_methods.md",
    "Item 8": "manuscript/sections/02_methods.md",
    "Item 9": "manuscript/sections/02_methods.md",
    "Item 10": "manuscript/sections/02_methods.md",
    "Item 11": "manuscript/sections/02_methods.md",
    "Item 12": "manuscript/sections/02_methods.md",
    "Item 13": "manuscript/sections/02_methods.md",
    "Item 14": "manuscript/sections/02_methods.md",
    "Item 15": "manuscript/sections/02_methods.md",
    "Item 16": "manuscript/sections/03_results.md",
    "Item 17": "manuscript/sections/03_results.md",
    "Item 18": "manuscript/sections/03_results.md",
    "Item 19": "manuscript/sections/03_results.md",
    "Item 20": "manuscript/sections/03_results.md",
    "Item 21": "manuscript/sections/03_results.md",
    "Item 22": "manuscript/sections/03_results.md",
    "Item 23": "manuscript/sections/04_discussion.md",
    "Item 24": "manuscript/sections/04_discussion.md",
    "Item 25": "manuscript/sections/06_acknowledgments.md",
    "Item 26": "manuscript/sections/06_acknowledgments.md",
    "Item 27": "manuscript/sections/07_references.md",
}

CHECKLIST = Path("protocol/prisma_checklist.md")
OUT = Path("protocol/prisma_checklist_mapped.md")

def main():
    if not CHECKLIST.exists():
        raise SystemExit("Missing protocol/prisma_checklist.md")

    lines = []
    for line in CHECKLIST.read_text(encoding="utf-8").splitlines():
        added = False
        for item, path in MAPPING.items():
            if line.strip().startswith(item):
                lines.append(line)
                lines.append(f"  ↳ Covered in: `{path}`")
                added = True
                break
        if not added:
            lines.append(line)

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[ok] Wrote mapped checklist to {OUT}")

if __name__ == "__main__":
    main()
