import os
import shutil

source_root = r"C:\Users\vghy0\OneDrive\Desktop\final\vision\FOOD_HEALTH_ANALYSIS\data\UECFOOD256"
target_folder = os.path.join(source_root, "images")
os.makedirs(target_folder, exist_ok=True)

for class_folder in range(1, 257):
    class_path = os.path.join(source_root, str(class_folder))
    if not os.path.isdir(class_path):
        continue
    for file in os.listdir(class_path):
        if file.endswith(".jpg"):
            src = os.path.join(class_path, file)
            dst = os.path.join(target_folder, file)
            shutil.copy2(src, dst)
