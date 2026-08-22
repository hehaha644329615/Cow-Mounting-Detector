"""
母牛爬跨行为检测脚本
使用训练好的 YOLOv8 模型进行推理
"""

import argparse
from pathlib import Path
from ultralytics import YOLO


def main():
    parser = argparse.ArgumentParser(description="母牛爬跨行为检测")
    parser.add_argument("--source", type=str, default="demo/images/",
                        help="图片/视频路径或目录")
    parser.add_argument("--model", type=str, default="models/best.pt",
                        help="模型权重路径")
    parser.add_argument("--conf", type=float, default=0.25,
                        help="置信度阈值")
    parser.add_argument("--save", action="store_true", default=True,
                        help="是否保存结果")
    args = parser.parse_args()

    # 加载模型
    model = YOLO(args.model)
    print(f"✅ 模型加载成功: {args.model}")

    # 执行检测
    results = model(
        args.source,
        conf=args.conf,
        save=args.save,
        project="results",
        name="demo_results"
    )

    print(f"✅ 检测完成，结果保存在 results/demo_results/")


if __name__ == "__main__":
    main()