import numpy as np


def replace_nan_to_means(X):
    X_copy = X.copy()
    nans = np.where(np.isnan(X))
    X_copy[nans] = np.take(np.nan_to_num(np.nanmean(X, axis=0), copy=False),
                           nans[1])
    return X_copy
