import pandas as pd
import matplotlib.pyplot as plt
import os

# 加载 CSV
df_n = pd.read_csv("8n/results.csv")
df_s = pd.read_csv("8s/results.csv")

# 清洗列名：去除所有列名中的 "(B)"
df_n.columns = [col.replace(" (B)", "").replace("(B)", "") for col in df_n.columns]
df_s.columns = [col.replace(" (B)", "").replace("(B)", "") for col in df_s.columns]

# 添加模型标签
df_n["model"] = "YOLOv8n"
df_s["model"] = "YOLOv8s"

# 合并数据
df = pd.concat([df_n, df_s], ignore_index=True)

# 指定要对比的指标
metrics = [
    "metrics/mAP50", 
    "metrics/mAP50-95", 
    "metrics/precision", 
    "metrics/recall", 
    "train/box_loss", 
    "val/box_loss"
]

# 创建图像输出目录
os.makedirs("results/compare_plots", exist_ok=True)

# 绘制对比图
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

print("✅ 所有对比图已生成，保存在 results/compare_plots/")

