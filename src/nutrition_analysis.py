import json
import os

DEFAULT_PORTIONS = {
    "rice": 150,
    "eels on rice": 200,
    "pilaf": 200,
    "chicken-'n'-egg on rice": 250,
    "pork cutlet on rice": 250,
    "beef curry": 250,
    "sushi": 120,
    "chicken rice": 250,
    "fried rice": 250,
    "tempura bowl": 280,
    "bibimbap": 300,
    "toast": 70,
    "croissant": 60,
    "roll bread": 80,
    "raisin bread": 80,
    "chip butty": 100,
    "hamburger": 220,
    "pizza": 250,
    "sandwiches": 180,
    "udon noodle": 300,
    "tempura udon": 320,
    "soba noodle": 300,
    "ramen noodle": 350,
    "beef noodle": 350,
    "tensin noodle": 350,
    "fried noodle": 300,
    "spaghetti": 300,
    "Japanese-style pancake": 180,
    "takoyaki": 150,
    "gratin": 250,
    "sauteed vegetables": 200,
    "croquette": 150,
    "grilled eggplant": 120,
    "sauteed spinach": 100,
    "vegetable tempura": 150,
    "miso soup": 180,
    "potage": 200,
    "sausage": 100,
    "oden": 200,
    "omelet": 150,
    "ganmodoki": 120,
    "jiaozi": 160,
    "stew": 300,
    "teriyaki grilled fish": 200,
    "fried fish": 180,
    "grilled salmon": 180,
    "salmon meuniere": 200,
    "sashimi": 150,
    "grilled pacific saury": 200,
    "sukiyaki": 300,
    "sweet and sour pork": 250,
    "lightly roasted fish": 180,
    "steamed egg hotchpotch": 160,
    "tempura": 200,
    "fried chicken": 180,
    "sirloin cutlet": 220,
    "nanbanzuke": 200,
    "boiled fish": 180,
    "seasoned beef with potatoes": 250,
    "hambarg steak": 220,
    "steak": 250,
    "dried fish": 150,
    "ginger pork saute": 220,
    "spicy chili-flavored tofu": 180,
    "yakitori": 100,
    "cabbage roll": 160,
    "egg sunny-side up": 80,
    "natto": 80,
    "cold tofu": 100,
    "egg roll": 120,
    "chilled noodle": 300,
    "stir-fried beef and peppers": 220,
    "simmered pork": 220,
    "boiled chicken and vegetables": 250,
    "sashimi bowl": 300,
    "sushi bowl": 320,
    "fish-shaped pancake with bean jam": 140,
    "shrimp with chill source": 200,
    "roast chicken": 250,
    "steamed meat dumpling": 120,
    "omelet with fried rice": 300,
    "cutlet curry": 300,
    "spaghetti meat sauce": 320,
    "fried shrimp": 150,
    "potato salad": 120,
    "green salad": 80,
    "macaroni salad": 150,
    "Japanese tofu and vegetable chowder": 250,
    "pork miso soup": 200,
    "chinese soup": 180,
    "beef bowl": 300,
    "kinpira-style sauteed burdock": 100,
    "rice ball": 120,
    "pizza toast": 180,
    "dipping noodles": 300,
    "hot dog": 200,
    "french fries": 160,
    "mixed rice": 200,
    "goya chanpuru": 250,
    "green curry": 280,
    "okinawa soba": 300,
    "mango pudding": 100,
    "almond jelly": 100,
    "jjigae": 250,
    "dak galbi": 300,
    "dry curry": 250,
    "kamameshi": 300,
    "rice vermicelli": 250,
    "paella": 280,
    "tanmen": 300,
    "kushikatu": 180,
    "yellow curry": 280,
    "pancake": 150,
    "champon": 320,
    "crape": 120,
    "tiramisu": 130,
    "waffle": 130,
    "rare cheese cake": 130,
    "shortcake": 150,
    "chop suey": 250,
    "twice cooked pork": 250,
    "mushroom risotto": 300,
    "samul": 200,
    "zoni": 250,
    "french toast": 150,
    "fine white noodles": 300,
    "minestrone": 250,
    "pot au feu": 300,
    "chicken nugget": 160,
    "namero": 150,
    "french bread": 100,
    "rice gruel": 200,
    "broiled eel bowl": 300,
    "clear soup": 180,
    "yudofu": 200,
    "mozuku": 100,
    "inarizushi": 120,
    "pork loin cutlet": 250,
    "pork fillet cutlet": 250,
    "chicken cutlet": 220,
    "ham cutlet": 220,
    "minced meat cutlet": 220,
    "thinly sliced raw horsemeat": 150,
    "bagel": 120,
    "scone": 100,
    "tortilla": 120,
    "tacos": 150,
    "nachos": 150,
    "meat loaf": 220,
    "scrambled egg": 120,
    "rice gratin": 300,
    "lasagna": 300,
    "Caesar salad": 150,
    "oatmeal": 200,
    "fried pork dumplings served in soup": 250,
    "oshiruko": 180,
    "muffin": 100,
    "popcorn": 50,
    "cream puff": 90,
    "doughnut": 100,
    "apple pie": 140,
    "parfait": 200,
    "fried pork in scoop": 220,
    "lamb kebabs": 200,
    "dish consisting of stir-fried potato, eggplant and green pepper": 250,
    "roast duck": 250,
    "hot pot": 400,
    "pork belly": 200,
    "xiao long bao": 120,
    "moon cake": 100,
    "custard tart": 100,
    "beef noodle soup": 350,
    "pork cutlet": 250,
    "minced pork rice": 220,
    "fish ball soup": 250,
    "oyster omelette": 220,
    "glutinous oil rice": 200,
    "trunip pudding": 150,
    "stinky tofu": 180,
    "lemon fig jelly": 100,
    "khao soi": 300,
    "Sour prawn soup": 250,
    "Thai papaya salad": 150,
    "boned, sliced Hainan-style chicken with marinated rice": 300,
    "hot and sour, fish and vegetable ragout": 300,
    "stir-fried mixed vegetables": 200,
    "beef in oyster sauce": 250,
    "pork satay": 180,
    "spicy chicken salad": 200,
    "noodles with fish curry": 300,
    "Pork Sticky Noodles": 300,
    "Pork with lemon": 250,
    "stewed pork leg": 300,
    "charcoal-boiled pork neck": 250,
    "fried mussel pancakes": 250,
    "Deep Fried Chicken Wing": 180,
    "Barbecued red pork in sauce with rice": 300,
    "Rice with roast duck": 300,
    "Rice crispy pork": 300,
    "Wonton soup": 250,
    "Chicken Rice Curry With Coconut": 300,
    "Crispy Noodles": 300,
    "Egg Noodle In Chicken Yellow Curry": 300,
    "coconut milk soup": 250,
    "pho": 350,
    "Hue beef rice vermicelli soup": 350,
    "Vermicelli noodles with snails": 300,
    "Fried spring rolls": 200,
    "Steamed rice roll": 200,
    "Shrimp patties": 150,
    "ball shaped bun with pork": 120,
    "Coconut milk-flavored crepes with shrimp and beef": 180,
    "Small steamed savory rice pancake": 180,
    "Glutinous Rice Balls": 150,
    "loco moco": 300,
    "haupia": 100,
    "malasada": 100,
    "laulau": 200,
    "spam musubi": 200,
    "oxtail soup": 300,
    "adobo": 250,
    "lumpia": 150,
    "brownie": 100,
    "churro": 80,
    "jambalaya": 300,
    "nasi goreng": 280,
    "ayam goreng": 250,
    "ayam bakar": 250,
    "bubur ayam": 250,
    "gulai": 280,
    "laksa": 300,
    "mie ayam": 280,
    "mie goreng": 300,
    "nasi campur": 300,
    "nasi padang": 300,
    "nasi uduk": 300,
    "babi guling": 300,
    "kaya toast": 120,
    "bak kut teh": 300,
    "curry puff": 120,
    "chow mein": 300,
    "zha jiang mian": 300,
    "kung pao chicken": 250,
    "crullers": 100,
    "eggplant with garlic sauce": 200,
    "three cup chicken": 250,
    "bean curd family style": 250,
    "salt & pepper fried shrimp with shell": 200,
    "baked salmon": 200,
    "braised pork meat ball with napa cabbage": 250,
    "winter melon soup": 250,
    "steamed spareribs": 250,
    "chinese pumpkin pie": 120,
    "eight treasure rice": 200,
    "hot & sour soup": 250
}

import os
import json

# 文件路径
DETECTIONS_PATH = "data/detections.json"
LOOKUP_PATH = "data/nutrition_lookup.json"
OUTPUT_PATH = "data/health_analysis.json"


with open(DETECTIONS_PATH, "r", encoding="utf-8") as f:
    detections = json.load(f)

with open(LOOKUP_PATH, "r", encoding="utf-8") as f:
    lookup = json.load(f)

results = {}

for img_name, foods in detections.items():
    total_energy = total_fat = total_protein = total_carb = total_sugar = total_satfat = 0.0
    portions_used = {}
    missing_items = []

    for food in foods:
        key = food.lower()
        nutri = lookup.get(key)

        if nutri is None:
            missing_items.append(food)
            continue

        portion = DEFAULT_PORTIONS.get(key, 100)
        portions_used[food] = portion

        total_energy  += (nutri.get("energy_100g") or 0) * portion / 100
        total_fat     += (nutri.get("fat_100g") or 0) * portion / 100
        total_protein += (nutri.get("proteins_100g") or 0) * portion / 100
        total_carb    += (nutri.get("carbohydrates_100g") or 0) * portion / 100
        total_sugar   += (nutri.get("sugars_100g") or 0) * portion / 100
        total_satfat  += (nutri.get("saturated_fat_100g") or 0) * portion / 100

    # ====== 营养百分比分布 ======
    if total_energy > 0:
        fat_pct     = total_fat * 9 / total_energy * 100
        protein_pct = total_protein * 4 / total_energy * 100
        carb_pct    = total_carb * 4 / total_energy * 100
    else:
        fat_pct = protein_pct = carb_pct = 0.0

    # ====== 健康分析建议 ======
    suggestions = []

    if total_energy > 700:
        suggestions.append("High in calories.")
    elif total_energy < 300:
        suggestions.append("Low in calories.")
    else:
        suggestions.append("Moderate calorie level.")

    if fat_pct > 35:
        suggestions.append("High fat proportion.")
    if protein_pct < 10:
        suggestions.append("Low protein proportion.")
    if total_sugar > 15:
        suggestions.append("High sugar content.")
    if total_satfat > 5:
        suggestions.append("High saturated fat content.")

    # ====== 写入结果 ======
    results[img_name] = {
        "foods_detected": foods,
        "portion_grams_used": portions_used,
        "total_energy_kcal": round(total_energy, 1),
        "nutrient_grams": {
            "fat_g": round(total_fat, 1),
            "protein_g": round(total_protein, 1),
            "carbohydrate_g": round(total_carb, 1),
            "sugars_g": round(total_sugar, 1),
            "saturated_fat_g": round(total_satfat, 1)
        },
        "nutrient_energy_percent": {
            "fat_percent": round(fat_pct, 1),
            "protein_percent": round(protein_pct, 1),
            "carbohydrate_percent": round(carb_pct, 1)
        },
        "health_analysis": " ".join(suggestions),
        "missing_items": missing_items or None
    }

# ====== 写出 JSON 文件 ======
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ Health analysis saved to {OUTPUT_PATH}")

