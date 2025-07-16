import pandas as pd

# 读取你提供的类别表（例如叫 food_labels.csv）
df = pd.read_csv(
    r"C:\Users\vghy0\OneDrive\Desktop\final\vision\FOOD_HEALTH_ANALYSIS\data\UECFOOD256\category.txt",
    sep='\t',
    header=None,
    names=['id', 'name'],
    skiprows=1  # ✅ 跳过第一行标题 'id name'
)
df['id'] = df['id'].astype(int)
with open("yolov8/uec256.yaml", "w") as f:
    f.write("path: ../data/uec256_yolo_format\n")
    f.write("train: images/train\n")
    f.write("val: images/val\n\n")
    f.write("names:\n")
    for i, name in zip(df['id'], df['name']):
        f.write(f"  {i-1}: {name}\n")  # 注意：YOLO 类别从 0 开始，原始是从 1 开始的
