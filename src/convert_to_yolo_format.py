import os
import shutil
from PIL import Image
from sklearn.model_selection import train_test_split

# 配置路径
raw_image_dir = r"C:\Users\vghy0\OneDrive\Desktop\final\vision\FOOD_HEALTH_ANALYSIS\data\UECFOOD256\images"
raw_label_file = r"C:\Users\vghy0\OneDrive\Desktop\final\vision\FOOD_HEALTH_ANALYSIS\data\UECFOOD256\all_labels.txt"
output_dir = r"C:\Users\vghy0\OneDrive\Desktop\final\vision\FOOD_HEALTH_ANALYSIS\data\uec256_yolo_format"

# 输出结构
img_out = os.path.join(output_dir, "images")
lbl_out = os.path.join(output_dir, "labels")
os.makedirs(img_out, exist_ok=True)
os.makedirs(lbl_out, exist_ok=True)

# 读取所有标注
with open(raw_label_file, "r") as f:
    lines = f.readlines()

# 拆分训练和验证集（你也可以根据需要固定）
image_ids = list(set([line.strip().split()[0] for line in lines]))
train_ids, val_ids = train_test_split(image_ids, test_size=0.2, random_state=42)

def get_set(image_id):
    return "train" if image_id in train_ids else "val"

# 遍历所有标注行
for line_num, line in enumerate(lines):
    parts = line.strip().split()
    if len(parts) != 6:
        print(f"⚠️ 第 {line_num+1} 行字段数错误，跳过：{line.strip()}")
        continue
    try:
        img_id = parts[0]
        cls = int(parts[1])
        x1 = int(parts[2])
        y1 = int(parts[3])
        x2 = int(parts[4])
        y2 = int(parts[5])
    except ValueError as e:
        print(f"❌ 第 {line_num+1} 行转换出错（跳过）：{line.strip()} → {e}")
        continue

    
    img_file = os.path.join(raw_image_dir, f"{img_id}.jpg")
    if not os.path.exists(img_file):
        continue

    # 获取图像尺寸
    with Image.open(img_file) as img:
        w, h = img.size

    # 计算 YOLO 格式 bbox（归一化中心坐标和宽高）
    x_center = ((x1 + x2) / 2) / w
    y_center = ((y1 + y2) / 2) / h
    bbox_width = (x2 - x1) / w
    bbox_height = (y2 - y1) / h

    # 写入对应 label txt 文件
    set_name = get_set(img_id)
    label_dir = os.path.join(lbl_out, set_name)
    image_dir = os.path.join(img_out, set_name)
    os.makedirs(label_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)

    label_file = os.path.join(label_dir, f"{img_id}.txt")
    with open(label_file, "a") as f:
        f.write(f"{cls} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")

    # 复制图像文件
    shutil.copy2(img_file, os.path.join(image_dir, f"{img_id}.jpg"))

print("✅ 数据转换完成，YOLO 格式已生成。")

