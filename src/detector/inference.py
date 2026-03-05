def run_inference(model, image, conf_threshold):
    results = model(image)[0]

    spindle_box = None
    ball_box = None

    for box in results.boxes:
        cls = int(box.cls[0])
        conf = float(box.conf[0])

        if conf < conf_threshold:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        if cls == 0:
            if spindle_box is None:
                spindle_box = (x1, y1, x2, y2)

        elif cls == 1:
            if ball_box is None:
                ball_box = (x1, y1, x2, y2)

    return spindle_box, ball_box