from ultralytics import YOLO
import os
import json


model = YOLO(model_path)
class_names = model.model.names

results_dict = {}

for img_name in os.listdir(image_dir):
    if not img_name.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue
    img_path = os.path.join(image_dir, img_name)
    results = model.predict(source=img_path, conf=conf_threshold, verbose=False)
    
    boxes = results[0].boxes
    class_ids = boxes.cls.int().tolist() if boxes is not None else []
    detected_labels = list(set([class_names[i] for i in class_ids]))
    
    results_dict[img_name] = detected_labels

with open(output_json, "w", encoding="utf-8") as f:
    json.dump(results_dict, f, indent=4, ensure_ascii=False)

print(f"Detection results saved to: {output_json}")
