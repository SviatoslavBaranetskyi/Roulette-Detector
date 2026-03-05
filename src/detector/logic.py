def ball_on_spindle(spindle_box, ball_box):
    if not spindle_box or not ball_box:
        return False

    sx1, sy1, sx2, sy2 = spindle_box
    bx1, by1, bx2, by2 = ball_box

    cx = (bx1 + bx2) / 2
    cy = (by1 + by2) / 2

    return sx1 <= cx <= sx2 and sy1 <= cy <= sy2