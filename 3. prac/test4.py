import numpy as np


def encode_rle(x):
    index = np.nonzero(
        np.append(True, ~np.isclose(x[1:], x[:-1], equal_nan=True)))
    lengths = np.diff(np.append(index, len(x)))
    return x[index], lengths
