import numpy as np

def bottom_strip_mask(h, w, frac=0.40): # keep bottom 40%
    """
    Apply mask before pooling flow. Repeat w/ frac = 0.30, 0.50 to see
    stability differences.
    """
    mask = np.zeros((h,w), dtype=bool)
    start = int(h * (1.0 - frac))

    mask[ start:, :] = True

    return mask