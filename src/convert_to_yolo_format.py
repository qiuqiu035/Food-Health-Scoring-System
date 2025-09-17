import os
import shutil
from PIL import Image
from sklearn.model_selection import train_test_split


img_out = os.path.join(output_dir, "images")
lbl_out = os.path.join(output_dir, "labels")
os.makedirs(img_out, exist_ok=True)
os.makedirs(lbl_out, exist_ok=True)

with open(raw_label_file, "r") as f:
    lines = f.readlines()

image_ids = list(set([line.strip().split()[0] for line in lines]))
train_ids, val_ids = train_test_split(image_ids, test_size=0.2, random_state=42)

def get_set(image_id):
    return "train" if image_id in train_ids else "val"

for line_num, line in enumerate(lines):
    parts = line.strip().split()
    if len(parts) != 6:
        print(f"{line_num+1} error, skip)
    try:
        img_id = parts[0]
        cls = int(parts[1])
        x1 = int(parts[2])
        y1 = int(parts[3])
        x2 = int(parts[4])
        y2 = int(parts[5])
    except ValueError as e:
        print(f" {line_num+1} error：{line.strip()} → {e}")
        continue

    
    img_file = os.path.join(raw_image_dir, f"{img_id}.jpg")
    if not os.path.exists(img_file):
        continue

    with Image.open(img_file) as img:
        w, h = img.size

    x_center = ((x1 + x2) / 2) / w
    y_center = ((y1 + y2) / 2) / h
    bbox_width = (x2 - x1) / w
    bbox_height = (y2 - y1) / h

    set_name = get_set(img_id)
    label_dir = os.path.join(lbl_out, set_name)
    image_dir = os.path.join(img_out, set_name)
    os.makedirs(label_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    label_file = os.path.join(label_dir, f"{img_id}.txt")
    with open(label_file, "a") as f:
        f.write(f"{cls} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")

    shutil.copy2(img_file, os.path.join(image_dir, f"{img_id}.jpg"))


