import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

from src.detector.model_loader import get_model
from src.detector.inference import run_inference
from src.detector.logic import ball_on_spindle


def run_app():
    print("App started")
    root = tk.Tk()
    root.title("Roulette Detector")
    root.geometry("1000x700")

    model = get_model()

    confidence = tk.DoubleVar(value=0.5)

    def open_image():
        file_path = filedialog.askopenfilename(
            filetypes=[("JPEG files", "*.jpg *.jpeg")]
        )
        if not file_path:
            return

        img = cv2.imread(file_path)
        img = cv2.resize(img, (960, 540))

        spindle_box, ball_box = run_inference(
            model, img, confidence.get()
        )

        if spindle_box:
            cv2.rectangle(
                img,
                (spindle_box[0], spindle_box[1]),
                (spindle_box[2], spindle_box[3]),
                (0, 255, 0),
                2
            )

        if ball_on_spindle(spindle_box, ball_box):
            cv2.putText(
                img,
                "ball",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)

        image_label.config(image=img_tk)
        image_label.image = img_tk

    tk.Button(root, text="Open", command=open_image).pack(pady=10)

    tk.Label(root, text="Confidence").pack()
    tk.Spinbox(
        root,
        from_=0.3,
        to=1.0,
        increment=0.05,
        textvariable=confidence
    ).pack()

    image_label = tk.Label(root)
    image_label.pack()
    
    print("Entering mainloop")
    root.mainloop()