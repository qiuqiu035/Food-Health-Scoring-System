import pandas as pd
import matplotlib.pyplot as plt
import os

df_n = pd.read_csv("8n/results.csv")
df_s = pd.read_csv("8s/results.csv")

df_n.columns = [col.replace(" (B)", "").replace("(B)", "") for col in df_n.columns]
df_s.columns = [col.replace(" (B)", "").replace("(B)", "") for col in df_s.columns]

df_n["model"] = "YOLOv8n"
df_s["model"] = "YOLOv8s"

df = pd.concat([df_n, df_s], ignore_index=True)

metrics = [
    "metrics/mAP50", 
    "metrics/mAP50-95", 
    "metrics/precision", 
    "metrics/recall", 
    "train/box_loss", 
    "val/box_loss"
]

os.makedirs("results/compare_plots", exist_ok=True)

for metric in metrics:
    plt.figure(figsize=(8, 5))
    for model_name in df["model"].unique():
        sub = df[df["model"] == model_name]
        plt.plot(sub["epoch"], sub[metric], label=model_name)
    plt.title(f"{metric} over epochs")
    plt.xlabel("Epoch")
    plt.ylabel(metric.split("/")[-1])
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"results/compare_plots/{metric.replace('/', '_')}.png")
    plt.close()


