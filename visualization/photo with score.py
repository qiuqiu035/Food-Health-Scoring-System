import os
import json
from PIL import Image, ImageDraw, ImageFont

IMG_DIR   = "data/test_images"
JSON_PATH = "data/health_analysis.json"
SAVE_DIR  = "results/annotated_images"
os.makedirs(SAVE_DIR, exist_ok=True)

with open(JSON_PATH, "r", encoding="utf-8") as f:
    analysis = json.load(f)

try:
    font = ImageFont.truetype("arial.ttf", 15)
except:
    font = ImageFont.load_default()

def wrap_text(text, width):
    words = text.split()
    lines, line = [], ""
    for word in words:
        if len(line + " " + word) <= width:
            line += " " + word if line else word
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines

for img_name, result in analysis.items():
    img_path = os.path.join(IMG_DIR, img_name)
    if not os.path.exists(img_path):
        print(f"Don't exist: {img_path}")
        continue

    img = Image.open(img_path).convert("RGB")
    draw = ImageDraw.Draw(img, "RGBA")

    energy = result.get("total_energy_kcal", 0)
    analysis_text = result.get("health_analysis", "")
    food_list = result.get("foods_detected", [])

    max_line_length = 40
    foods_text = "Foods: " + ", ".join(food_list)
    lines = wrap_text(foods_text, max_line_length)
    lines.append(f"Energy: {energy:.1f} kcal")
    lines += wrap_text(analysis_text, max_line_length)

    padding = 10
    line_sizes = [draw.textbbox((0, 0), line, font=font) for line in lines]
    widths  = [x[2] - x[0] for x in line_sizes]
    heights = [x[3] - x[1] for x in line_sizes]

    max_w = max(widths)
    total_h = sum(heights) + padding * (len(lines) + 1)

    background_box = [0, 0, max_w + padding * 2, total_h]
    draw.rectangle(background_box, fill=(0, 0, 0, 180))

    y = padding
    for i, line in enumerate(lines):
        draw.text((padding, y), line, font=font, fill="white")
        y += heights[i] + padding

    save_path = os.path.join(SAVE_DIR, img_name)
    img.save(save_path)

print(f"All images annotated and saved to: {SAVE_DIR}")





