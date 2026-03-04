from ultralytics import YOLO

def train():
    model = YOLO("yolov8n.pt")

    model.train(
        data="dataset/dataset.yaml",
        epochs=120,
        imgsz=960,
        batch=8,
        project="runs",
        name="roulette_detector",
        pretrained=True
    )

if __name__ == "__main__":
    train()