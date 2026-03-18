"""
Generate simple textbook-style PNG diagrams for the Operators chapter.
Outputs into ./diagrams

Run:
  python make_diagrams.py
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BASE_DIR = Path(__file__).resolve().parent
OUT_DIR = BASE_DIR / "diagrams"


def load_font(size: int) -> ImageFont.ImageFont:
    # Try common fonts; fall back to default.
    candidates = [
        "arial.ttf",
        "calibri.ttf",
        "times.ttf",
        "segoeui.ttf",
    ]
    for name in candidates:
        try:
            return ImageFont.truetype(name, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_title(draw: ImageDraw.ImageDraw, title: str, w: int, pad: int = 24) -> int:
    font = load_font(34)
    draw.text((pad, pad), title, fill=(0, 0, 0), font=font)
    return pad + 46


def save(img: Image.Image, filename: str) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    img.save(OUT_DIR / filename)


def diagram_math_operators() -> None:
    w, h = 1400, 900
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    y = draw_title(d, "Mathematical Operators", w)

    font_op = load_font(48)
    font_txt = load_font(26)
    font_ex = load_font(22)

    items = [
        ("+", "Addition", "5 + 3 = 8"),
        ("-", "Subtraction", "10 - 4 = 6"),
        ("*", "Multiplication", "6 * 4 = 24"),
        ("/", "Division", "12 / 4 = 3.0"),
        ("//", "Floor division", "13 // 4 = 3"),
        ("%", "Remainder", "13 % 4 = 1"),
        ("**", "Power", "2 ** 3 = 8"),
    ]

    cols = 3
    cell_w = (w - 80) // cols
    cell_h = 190
    start_x = 40
    start_y = y + 30

    for idx, (op, label, ex) in enumerate(items):
        r = idx // cols
        c = idx % cols
        x0 = start_x + c * cell_w
        y0 = start_y + r * cell_h
        x1 = x0 + cell_w - 20
        y1 = y0 + cell_h - 20
        d.rounded_rectangle([x0, y0, x1, y1], radius=18, outline=(180, 180, 180), width=3)
        d.text((x0 + 26, y0 + 22), op, fill=(0, 0, 0), font=font_op)
        d.text((x0 + 26, y0 + 92), label, fill=(0, 0, 0), font=font_txt)
        d.text((x0 + 26, y0 + 132), ex, fill=(60, 60, 60), font=font_ex)

    save(img, "math_operators_grid.png")


def diagram_comparison_operators() -> None:
    w, h = 1400, 860
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    y = draw_title(d, "Comparison Operators", w)

    font_hd = load_font(28)
    font_row = load_font(24)

    headers = ["Operator", "Meaning", "Example", "Result"]
    rows = [
        ("==", "equal to", "5 == 5", "True"),
        ("!=", "not equal to", "5 != 3", "True"),
        (">", "greater than", "8 > 10", "False"),
        ("<", "less than", "5 < 10", "True"),
        (">=", "greater or equal", "70 >= 70", "True"),
        ("<=", "less or equal", "3 <= 5", "True"),
    ]

    x0, y0 = 40, y + 40
    col_w = [180, 420, 420, 240]
    row_h = 70

    # Header
    x = x0
    for i, hd in enumerate(headers):
        d.rectangle([x, y0, x + col_w[i], y0 + row_h], outline=(0, 0, 0), width=2)
        d.text((x + 16, y0 + 18), hd, fill=(0, 0, 0), font=font_hd)
        x += col_w[i]

    # Rows
    for r_idx, row in enumerate(rows):
        y_row = y0 + row_h * (r_idx + 1)
        x = x0
        for c_idx, cell in enumerate(row):
            d.rectangle([x, y_row, x + col_w[c_idx], y_row + row_h], outline=(180, 180, 180), width=2)
            d.text((x + 16, y_row + 20), cell, fill=(0, 0, 0), font=font_row)
            x += col_w[c_idx]

    save(img, "comparison_operators_table.png")


def diagram_logical_truth_table() -> None:
    w, h = 1400, 900
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    y = draw_title(d, "Logical Operators (Truth Tables)", w)

    font_hd = load_font(30)
    font_cell = load_font(24)

    # AND table
    x0, y0 = 60, y + 30
    d.text((x0, y0), "AND", fill=(0, 0, 0), font=font_hd)
    y0 += 50
    and_rows = [("A", "B", "A and B"), ("T", "T", "T"), ("T", "F", "F"), ("F", "T", "F"), ("F", "F", "F")]
    col_w = [80, 80, 220]
    row_h = 55
    for r, row in enumerate(and_rows):
        x = x0
        for c, cell in enumerate(row):
            d.rectangle([x, y0 + r * row_h, x + col_w[c], y0 + (r + 1) * row_h], outline=(180, 180, 180), width=2)
            d.text((x + 22, y0 + r * row_h + 14), cell, fill=(0, 0, 0), font=font_cell)
            x += col_w[c]

    # OR table
    x1, y1 = 520, y + 30
    d.text((x1, y1), "OR", fill=(0, 0, 0), font=font_hd)
    y1 += 50
    or_rows = [("A", "B", "A or B"), ("T", "T", "T"), ("T", "F", "T"), ("F", "T", "T"), ("F", "F", "F")]
    for r, row in enumerate(or_rows):
        x = x1
        for c, cell in enumerate(row):
            d.rectangle([x, y1 + r * row_h, x + col_w[c], y1 + (r + 1) * row_h], outline=(180, 180, 180), width=2)
            d.text((x + 22, y1 + r * row_h + 14), cell, fill=(0, 0, 0), font=font_cell)
            x += col_w[c]

    # NOT table
    x2, y2 = 1000, y + 30
    d.text((x2, y2), "NOT", fill=(0, 0, 0), font=font_hd)
    y2 += 50
    not_rows = [("A", "not A"), ("T", "F"), ("F", "T")]
    col_w2 = [100, 140]
    for r, row in enumerate(not_rows):
        x = x2
        for c, cell in enumerate(row):
            d.rectangle([x, y2 + r * row_h, x + col_w2[c], y2 + (r + 1) * row_h], outline=(180, 180, 180), width=2)
            d.text((x + 22, y2 + r * row_h + 14), cell, fill=(0, 0, 0), font=font_cell)
            x += col_w2[c]

    save(img, "logical_operators_truth_table.png")


def diagram_bodmas_ladder() -> None:
    w, h = 1200, 900
    img = Image.new("RGB", (w, h), (255, 255, 255))
    d = ImageDraw.Draw(img)
    y = draw_title(d, "Operator Precedence (BODMAS)", w)

    font_step = load_font(28)
    font_sub = load_font(22)

    steps = [
        ("1. Brackets", "( )"),
        ("2. Orders (powers)", "**"),
        ("3. Multiply / Divide", "*, /, //, % (left to right)"),
        ("4. Add / Subtract", "+, - (left to right)"),
    ]

    x0 = 120
    y0 = y + 60
    box_w = w - 240
    box_h = 120
    for i, (title, detail) in enumerate(steps):
        top = y0 + i * (box_h + 30)
        d.rounded_rectangle([x0, top, x0 + box_w, top + box_h], radius=18, outline=(180, 180, 180), width=3)
        d.text((x0 + 30, top + 22), title, fill=(0, 0, 0), font=font_step)
        d.text((x0 + 30, top + 66), detail, fill=(60, 60, 60), font=font_sub)
        if i < len(steps) - 1:
            # arrow down
            ax = x0 + box_w // 2
            ay1 = top + box_h + 6
            ay2 = top + box_h + 24
            d.line([ax, ay1, ax, ay2], fill=(0, 0, 0), width=4)
            d.polygon([(ax - 8, ay2 - 2), (ax + 8, ay2 - 2), (ax, ay2 + 10)], fill=(0, 0, 0))

    save(img, "bodmas_ladder.png")


def main() -> None:
    diagram_math_operators()
    diagram_comparison_operators()
    diagram_logical_truth_table()
    diagram_bodmas_ladder()
    print(f"Saved diagrams to: {OUT_DIR}")


if __name__ == "__main__":
    main()

