import os
import json
import matplotlib.pyplot as plt

JSON_PATH = "data/health_analysis.json"
SAVE_DIR = "results/pie_charts"
os.makedirs(SAVE_DIR, exist_ok=True)

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

for img_name, result in data.items():
    percent = result.get("nutrient_energy_percent", {})
    fat = percent.get("fat_percent", 0)
    protein = percent.get("protein_percent", 0)
    carb = percent.get("carbohydrate_percent", 0)

    labels = ['Fat', 'Protein', 'Carbohydrate']
    sizes = [fat, protein, carb]

    filtered = [(l, s) for l, s in zip(labels, sizes) if s > 0]
    if not filtered:
        continue
    labels, sizes = zip(*filtered)

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Nutrient Energy Ratio - {img_name}')
    plt.axis('equal')

    save_path = os.path.join(SAVE_DIR, img_name.replace(".jpg", ".png"))
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()

print(f"Pie charts saved to: {SAVE_DIR}")
