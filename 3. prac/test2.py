import numpy as np
import time


# информация про as_strided взята отсюда
# https://stackoverflow.com/questions/19414673/in-numpy-how-to-efficiently-list-all-fixed-size-submatrices
def calc_expectations(h, w, X, Q):
    if h == 1 and w == 1:
        return Q * X
    sub_shape = (h, w)
    Q = np.pad(Q, ((w - 1, 0), (h - 1, 0)))
    view_shape = tuple(np.subtract(Q.shape, sub_shape) + 1) + sub_shape
    Q_view = np.lib.stride_tricks.as_strided(Q, view_shape, Q.strides * 2)
    Q_view = np.add.reduce(Q_view, axis=(-1, -2))
    return Q_view * X
