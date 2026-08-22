#!/usr/bin/env python3
from ultralytics import YOLO
import os

# 加载模型
model = YOLO("models/best.pt")

# 检测 demo 目录下的图片
image_dir = "demo/images"
if os.path.exists(image_dir):
    results = model(image_dir, save=True, project="results/demo_results")
    print("✅ 检测完成，结果保存在 results/demo_results/")
else:
    print("⚠️ 请先将测试图片放入 demo/images/ 目录")
