import numpy as np


def get_nonzero_diag_product(X):
    if len(X.shape) != 2:
        return None
    a = np.diag(X)
    a = a[a != 0]
    if len(a):
        return np.prod(a)
    else:
        return None
