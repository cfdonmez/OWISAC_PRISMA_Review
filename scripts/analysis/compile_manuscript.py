import os
from pathlib import Path

def main():
    """
    Combines section files into the main manuscript file.
    """
    manuscript_dir = Path("manuscript")
    sections_dir = manuscript_dir / "sections"
    output_file = manuscript_dir / "review_article.md"

    # Section files in the correct order
    section_files = [
        "00_abstract.md",
        "01_introduction.md",
        "02_methods.md",
        "03_results.md",
        "04_discussion.md",
        "05_conclusion.md",
        "06_acknowledgments.md",
        "07_references.md",
    ]

    with open(output_file, "w", encoding="utf-8") as outfile:
        for filename in section_files:
            filepath = sections_dir / filename
            if filepath.exists():
                print(f"Appending: {filepath}")
                outfile.write(filepath.read_text(encoding="utf-8"))
                outfile.write("\n\n")
            else:
                print(f"Skipping missing file: {filepath}")

    print(f"\n[ok] Manuscript compiled successfully at: {output_file}")

if __name__ == "__main__":
    main()
