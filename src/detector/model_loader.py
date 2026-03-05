from ultralytics import YOLO
import os

MODEL_PATH = os.path.join("models", "best.pt")

_model = None

def get_model():
    global _model
    if _model is None:
        print("Loading model...")
        _model = YOLO(MODEL_PATH)
        print("Model loaded")
    return _model