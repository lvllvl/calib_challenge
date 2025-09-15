import numpy as np

def robust_pool( flow, mask ):

    dx = flow[ ..., 0 ][ mask ]
    dy = flow[ ..., 1 ][ mask ]

    # median is robust; mean is sensitive to cars/pedestrians
    return np.median( dx ), np.median( dy )