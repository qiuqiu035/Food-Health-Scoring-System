import pandas as pd

df = pd.read_csv(
    sep='\t',
    header=None,
    names=['id', 'name'],
    skiprows=1 
)
df['id'] = df['id'].astype(int)
with open("yolov8/uec256.yaml", "w") as f:
    f.write("path: ../data/uec256_yolo_format\n")
    f.write("train: images/train\n")
    f.write("val: images/val\n\n")
    f.write("names:\n")
    for i, name in zip(df['id'], df['name']):
        f.write(f"  {i-1}: {name}\n")  
