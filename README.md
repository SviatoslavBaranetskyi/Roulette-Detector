# 🎰 Roulette Spindle & Ball Detector

Computer vision application that detects the roulette spindle and determines whether a ball is present on it.

The project uses a YOLO-based object detection model and a desktop GUI built with Tkinter.


# 📌 Problem Statement

Given a JPG image:

1. Detect the **roulette spindle**
2. If the spindle is detected — determine **whether a ball is present on it**

The application must:

- Load an image from disk
- Detect the spindle using a configurable **confidence threshold**
- Draw a bounding box around the spindle
- Display **"ball"** in the top-left corner if a ball is detected on the spindle

# 🛠 Tech Stack

- Python 3.12
- Ultralytics YOLOv8
- PyTorch
- OpenCV
- Pillow
- Tkinter

# ⚙ Installation

Clone the repository:

```bash
git clone git@github.com:SviatoslavBaranetskyi/Roulette-Detector.git
cd Roulette-Detector
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the GUI:

```bash
python main.py
```

# 📊 Model Performance

Validation results:

| Class | Precision | Recall | mAP50 | mAP50-95 |
|------|------|------|------|------|
| spindle | 0.707 | 0.785 | 0.816 | 0.541 |
| ball | 1.000 | 0.453 | 0.674 | 0.321 |
| **overall** | **0.854** | **0.619** | **0.745** | **0.431** |

Note: The recall for the **ball** class is lower due to:

- small object size
- motion blur
- limited number of ball samples in the dataset (~40 images)

# 👨‍💻 Developer
Sviatoslav Baranetskyi

Email: svyatoslav.baranetskiy738@gmail.com