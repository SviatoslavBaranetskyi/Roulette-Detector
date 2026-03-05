import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

from src.detector.model_loader import get_model
from src.detector.inference import run_inference
from src.detector.logic import ball_on_spindle


class RouletteApp:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Roulette Spindle Detector")
        self.root.geometry("1200x700")
        self.root.resizable(False, False)

        self.model = get_model()

        self.confidence = tk.DoubleVar(value=0.5)

        self.image_label = None
        self.result_label = None
        self.status_label = None

        self.create_layout()

    def create_layout(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        image_frame = tk.Frame(main_frame, width=960, height=540, bg="black")
        image_frame.pack(side="left")

        self.image_label = tk.Label(image_frame)
        self.image_label.pack()

        control_frame = tk.Frame(main_frame, width=200)
        control_frame.pack(side="right", fill="y", padx=20)

        tk.Label(
            control_frame,
            text="Controls",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        open_button = tk.Button(
            control_frame,
            text="Open Image",
            width=15,
            height=2,
            command=self.open_image
        )
        open_button.pack(pady=10)

        tk.Label(
            control_frame,
            text="Confidence"
        ).pack(pady=5)

        conf_slider = tk.Scale(
            control_frame,
            from_=0.3,
            to=1.0,
            resolution=0.05,
            orient="horizontal",
            variable=self.confidence
        )
        conf_slider.pack(pady=5)

        tk.Label(
            control_frame,
            text="Result",
            font=("Arial", 12, "bold")
        ).pack(pady=20)

        self.result_label = tk.Label(
            control_frame,
            text="None",
            font=("Arial", 12),
            fg="gray"
        )
        self.result_label.pack()

        self.status_label = tk.Label(
            self.root,
            text="Status: Ready",
            bd=1,
            relief="sunken",
            anchor="w"
        )
        self.status_label.pack(fill="x", side="bottom")

    def open_image(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("JPEG files", "*.jpg *.jpeg")]
        )

        if not file_path:
            return

        self.status_label.config(text="Status: Running detection...")

        img = cv2.imread(file_path)

        self.run_detection(img)

    def run_detection(self, img):
        img = cv2.resize(img, (960, 540))

        spindle_box, ball_box = run_inference(
            self.model,
            img,
            self.confidence.get()
        )

        if spindle_box:
            cv2.rectangle(
                img,
                (spindle_box[0], spindle_box[1]),
                (spindle_box[2], spindle_box[3]),
                (0, 255, 0),
                2
            )

        result = "No ball"

        if ball_on_spindle(spindle_box, ball_box):

            result = "Ball detected"

            cv2.putText(
                img,
                "ball",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                3
            )

        self.result_label.config(text=result)

        self.update_image(img)

        self.status_label.config(text="Status: Detection complete")

    def update_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        pil_img = Image.fromarray(img_rgb)

        tk_img = ImageTk.PhotoImage(pil_img)

        self.image_label.configure(image=tk_img)
        self.image_label.image = tk_img

    def run(self):
        self.root.mainloop()


def run_app():
    app = RouletteApp()
    app.run()