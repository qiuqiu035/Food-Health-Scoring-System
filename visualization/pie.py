import os
import json
import matplotlib.pyplot as plt

# 输入路径
JSON_PATH = "data/health_analysis.json"
SAVE_DIR = "results/pie_charts"
os.makedirs(SAVE_DIR, exist_ok=True)

# 读取 JSON 数据
with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

for img_name, result in data.items():
    percent = result.get("nutrient_energy_percent", {})
    fat = percent.get("fat_percent", 0)
    protein = percent.get("protein_percent", 0)
    carb = percent.get("carbohydrate_percent", 0)

    labels = ['Fat', 'Protein', 'Carbohydrate']
    sizes = [fat, protein, carb]

    # 忽略为 0 的项
    filtered = [(l, s) for l, s in zip(labels, sizes) if s > 0]
    if not filtered:
        continue
    labels, sizes = zip(*filtered)

    # 绘制 Pie Chart
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Nutrient Energy Ratio - {img_name}')
    plt.axis('equal')

    # 保存图像
    save_path = os.path.join(SAVE_DIR, img_name.replace(".jpg", ".png"))
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()

print(f"✅ Pie charts saved to: {SAVE_DIR}")
