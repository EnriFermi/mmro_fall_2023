import numpy as np


def get_max_before_zero(x):
    mx = x[1:]
    zero = np.isclose(np.diff(x), mx)
    if not np.any(zero):
        return None
    return np.max(mx[zero])
