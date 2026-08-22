# 🐄 Cow Mounting Detector

基于 YOLOv8 的母牛爬跨行为检测系统，用于畜牧业智能化管理，辅助精准配种。

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-ultralytics-green.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)

---

## 📊 模型性能

| 指标 | 数值 |
|------|------|
| **mAP@0.5** | **0.995** |
| **mAP@0.5:0.95** | **0.95** |
| **Precision** | **0.99** |
| **Recall** | **0.99** |
| **F1-Score** | **1.00** |

### 性能曲线

| Precision-Confidence Curve | Precision-Recall Curve |
|:---:|:---:|
| ![P Curve](results/curves/BoxP_curve.png) | ![PR Curve](results/curves/BoxPR_curve.png) |

| Recall-Confidence Curve | F1-Confidence Curve |
|:---:|:---:|
| ![R Curve](results/curves/BoxR_curve.png) | ![F1 Curve](results/curves/BoxF1_curve.png) |

### 混淆矩阵

| Confusion Matrix | Normalized |
|:---:|:---:|
| ![CM](results/confusion/confusion_matrix.png) | ![CM Norm](results/confusion/confusion_matrix_normalized.png) |

### 训练过程

![Training Results](results/results.png)

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/hehaha644329615/Cow-Mounting-Detector.git
cd Cow-Mounting-Detector

---

## 添加 requirements.txt

```bash
cat > requirements.txt << 'EOF'
ultralytics>=8.0.0
torch>=1.8.0
torchvision>=0.9.0
opencv-python>=4.5.0
matplotlib>=3.3.0
numpy>=1.19.0
Pillow>=8.0.0
