from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # 用nano版本最快


if __name__ == '__main__':
    model = YOLO("yolov8n.pt")
    
    model.train(
        data="./cow_image/data.yaml",
        epochs=20,
        imgsz=640,
        batch=16,
        device=0,
        workers=2,
        project="runs/train",
        name="mounting_detector",
        exist_ok=True,
        pretrained=True,
        patience=20,
        seed=42
    )
    
print("训练完成！模型保存在 runs/train/mounting_detector/weights/best.pt")