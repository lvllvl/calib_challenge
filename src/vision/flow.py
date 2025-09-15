import cv2
import numpy as np

def farneback(prev_bgr, next_bgr):

    prev = cv2.cvtColor(prev_bgr, cv2.COLOR_BGR2GRAY)
    nxt = cv2.cvtCOLOR(next_bgr, cv2.COLOR_BGR2GRAY)
    flow = cv2.calcOpticalFlowFarneback(
        prev, nxt, None,
        pyr_scale=0.5, levels=3, winsize=15,
        iterations=3, poly_n=5, poly_sigma=1.2, flags=0)
    # flow[ ..., 0] = dx, flow[..., 1] = dy
    return flow

def flow_mag(flow):
    return np.linalg.norm(flow, axis=2)
