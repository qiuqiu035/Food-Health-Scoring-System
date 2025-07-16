## Food Health Scoring System
This project implements an AI-powered system to assess the healthiness of meals using food images. It combines deep learning-based food detection with nutritional data retrieval and rule-based scoring to give visual and interpretable feedback.

## Features

- Detects food items in user-uploaded images using YOLOv8 (`v8s`, `v8n` comparison available)
- Retrieves real-time nutritional information via OpenFoodFacts API
- Applies rule-based logic to evaluate balance of calories, sugar, protein, and fat
- Generates annotated images and pie charts for clear health feedback
- Includes comparison of YOLOv8 models (`v8s` vs `v8n`)
- Fully automated label conversion and validation with error handling

## Tech Stack

- **Languages**: Python  
- **Computer Vision**: YOLOv8 (Ultralytics)  
- **Nutrition Data**: OpenFoodFacts API  
- **Visualization**: Matplotlib, PIL  
- **Other Tools**: JSON, Requests, OS, Logging

## Project Structure

```
food-health-scoring/
├── coco/
│   └── toyolo.py                # COCO annotation to YOLO format converter
├── dataset/
│   └── coco/
│       ├── annotations/         # Contains instances_val2017.json
│       ├── val2017/            # Raw COCO validation images
│       └── coco_yolo/          # YOLO formatted images + labels
├── outputs/                    # Analysis results from COCO dataset
│   ├── food_cooccurrence.txt
│   ├── top_healthy_images.txt
│   ├── top_unhealthy_images.txt
├── runs/                       # YOLOv5 output directory
├── scripts/
│   └── food_analysis.py        # Food detection and scoring logic
├── test.jpg                    # Custom input image for demo
├── yolov5/                     # YOLOv5 cloned repo
├── yolov5s.pt                  # Pretrained YOLOv5 weights
├── requirements.txt
└── README.md
```


## Example Output

Example outputs are included in the `images/` folder, such as annotated detection results and corresponding nutrition pie charts.

## YOLOv8 Model Comparison

A performance comparison between YOLOv8s and YOLOv8n has been generated and included in the `images/` folder.

## How to Run

1. Clone the repository:

- git clone https://github.com/qiuqiu035/food-health-scoring.git
- cd food-health-scoring

2. Install dependencies:

- pip install -r requirements.txt

3. Run the notebook or script:

- Open `yolov8_detection.ipynb` for the full detection and scoring pipeline.
- The OpenFoodFacts API does not require authentication, but requests are rate-limited.

## Notes

- All labels have been regenerated and cleaned (`all_labels.txt`)
- Data conversion completed, YOLO format annotations have been generated
- Incorrect number of fields on line 47, skipping: `...`
- Error converting line 89 (skipped): `... → ValueError(...)`

## Author

**Hongyu Guo**  
MSc Data Science  
University of Padua  
GitHub: [qiuqiu035](https://github.com/qiuqiu035)
