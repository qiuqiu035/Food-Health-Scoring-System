import os

output_file = os.path.join(root_dir, "all_labels.txt")

with open(output_file, "w") as out_f:
    for class_folder in range(1, 257):
        folder_path = os.path.join(root_dir, str(class_folder))
        label_path = os.path.join(folder_path, "bb_info.txt")

        if not os.path.exists(label_path):
            continue

        with open(label_path, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) != 5:
                    continue
                if parts[0] == "img" or parts[1] == "x1":
                    continue 
                img_name, x1, y1, x2, y2 = parts
                img_id = os.path.splitext(img_name)[0]
                out_f.write(f"{img_id} {class_folder - 1} {x1} {y1} {x2} {y2}\n")


