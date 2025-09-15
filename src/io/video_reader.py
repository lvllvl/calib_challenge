import cv2

def iter_frames(path, max_frames=None, scale=1.0):

    cap = cv2.VideoCapture(path)
    n = 0

    while True:
        ok, frame = cap.read()
        if not ok: break
        if scale != 1.0:
            frame = cv2.resize(frame, None, fx=scale, fy=scale)
        yield frame
        n += 1
        if max_frames and n >= max_frames: break
    cap.release()

