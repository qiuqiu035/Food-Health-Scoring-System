import json
import requests
import time
import os

# 输入文件路径
detections_path = "data/detections.json"
output_path = "data/nutrition_lookup.json"

# 如果已有则跳过已查询内容
if os.path.exists(output_path):
    with open(output_path, "r", encoding="utf-8") as f:
        nutrition_data = json.load(f)
else:
    nutrition_data = {}

# 加载检测到的食物类别
with open(detections_path, "r", encoding="utf-8") as f:
    detections = json.load(f)

# 获取所有唯一类别
all_labels = set()
for labels in detections.values():
    all_labels.update(labels)

# 查询函数：使用 OpenFoodFacts
def query_food_nutrition_openfoodfacts(food_name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        'search_terms': food_name,
        'search_simple': 1,
        'action': 'process',
        'json': 1,
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None

    products = response.json().get("products", [])
    energy_vals = []
    selected_product = None

    for product in products:
        nutriments = product.get("nutriments", {})
        name = product.get("product_name", "").lower()

        # 过滤无关产品（如调料、酱料等）
        if any(bad in name for bad in ["sauce", "dressing", "mayonnaise", "powder", "cream"]):
            continue

        energy = nutriments.get("energy_100g")
        if energy and 50 < energy < 1000:  # 合理范围过滤
            energy_vals.append(energy)
            if not selected_product:
                selected_product = product
        if len(energy_vals) >= 3:
            break

    if energy_vals and selected_product:
        avg_energy = sum(energy_vals) / len(energy_vals)
        return {
            "food_name": selected_product.get("product_name", food_name),
            "energy_100g": avg_energy,
            "fat_100g": nutriments.get("fat_100g"),
            "saturated_fat_100g": nutriments.get("saturated-fat_100g"),
            "carbohydrates_100g": nutriments.get("carbohydrates_100g"),
            "sugars_100g": nutriments.get("sugars_100g"),
            "proteins_100g": nutriments.get("proteins_100g"),
            "nutriscore_grade": selected_product.get("nutriscore_grade"),
            "url": selected_product.get("url")
        }

    return None

# 执行查询
for label in all_labels:
    if label in nutrition_data:
        print(f"✅ 已存在：{label}")
        continue

    print(f"🔍 查询中：{label}")
    result = query_food_nutrition_openfoodfacts(label)
    if result:
        nutrition_data[label] = result
        print(f"✅ 获取成功：{label}")
    else:
        print(f"⚠️ 无法获取：{label}")
    time.sleep(1.5)  # 避免频率限制

# 保存结果
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(nutrition_data, f, indent=4, ensure_ascii=False)

print(f"\n🎉 所有营养信息已保存到 {output_path}")

