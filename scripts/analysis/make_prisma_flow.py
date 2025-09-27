import json
from pathlib import Path

OUT = Path("results/figures/prisma_flow.png")
COUNTS = Path("results/prisma_counts.json")

def read_counts(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def render_png(text, out_path):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        raise SystemExit("Pillow missing. Install with: pip install pillow")
    lines = text.splitlines()
    width = max(800, max((len(l) for l in lines), default=80) * 8)
    height = max(300, 20 + 20*len(lines))
    img = Image.new("RGB", (width, height), color=(255,255,255))
    draw = ImageDraw.Draw(img)
    y = 10
    for l in lines:
        draw.text((10, y), l, fill=(0,0,0))
        y += 20
    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path)

def main():
    if not COUNTS.exists():
        raise SystemExit("Missing results/prisma_counts.json. Create it first (Step 6A).")
    c = read_counts(COUNTS)
    lines = [
        "PRISMA Flow (Smoke Test)",
        f"identified         : {c.get('identified')}",
        f"deduplicated      : {c.get('deduplicated')}",
        f"screened          : {c.get('screened')}",
        f"excluded_title_abs: {c.get('excluded_title_abs')}",
        f"fulltext_assessed : {c.get('fulltext_assessed')}",
        f"fulltext_excluded : {c.get('fulltext_excluded')}",
        f"included_qual     : {c.get('included_qual')}",
        f"included_quant    : {c.get('included_quant')}",
        f"last_updated      : {c.get('last_updated')}",
    ]
    render_png("\n".join(lines), OUT)
    print(f"[ok] wrote {OUT}")

if __name__ == "__main__":
    main()
