from bisect import bisect_right
from copy import deepcopy


def is_correct(ijx, ra, ca):
    return isinstance(ijx[0], int) and \
        isinstance(ijx[1], int) and type(ijx[2]) in [int, float] and \
        (0 <= ijx[0] < ra) and (0 <= ijx[1] < ca)


def raise_(ex):
    raise ex


class CooSparseMatrix:
    def __init__(s, ijx_list, shape):
        # check correct shape

        if type(ijx_list) is dict:
            s.ra, s.ca = shape
            s.im = {0: ijx_list}
            return

        if not (type(shape) is tuple) or len(shape) != 2 \
                or list(map(type, shape)) != [int, int]:
            raise TypeError
        # check correct data
        if not (type(ijx_list) is list):
            raise TypeError
        s.ra, s.ca = shape
        s.shape = shape
        s.im = dict()
        for ijx in ijx_list:
            if is_correct(ijx, s.ra, s.ca):
                if ijx[0] not in s.im:
                    s.im[ijx[0]] = dict()
                s_l = s.im[ijx[0]]
                if ijx[1] not in s_l:
                    s_l[ijx[1]] = ijx[2]
                else:
                    raise TypeError
            else:
                raise TypeError

    def __getitem__(s, ij):

        if type(ij) is int and (0 <= ij < s.ra):
            if ij in s.im:
                return CooSparseMatrix(s.im[ij], (1, s.ca))
            else:
                return CooSparseMatrix({}, (1, s.ca))
        elif type(ij) is tuple and list(map(type, ij)) == [int, int] \
                and (0 <= ij[0] < s.ra) and (0 <= ij[1] < s.ca):
            if ij[0] in s.im:
                s_l = s.im[ij[0]]
                if ij[1] in s_l:
                    return s_l[ij[1]]
                return 0
            else:
                return 0
        else:
            raise TypeError

    def __setitem__(s, ij, v):
        if type(ij) is tuple and list(map(type, ij)) == [int, int] \
                and type(v) in [float, int] and (0 <= ij[0] < s.ra) and \
                (0 <= ij[1] < s.ca):
            if ij[0] not in s.im:
                s.im[ij[0]] = dict()
            s_l = s.im[ij[0]]
            # find index for insert
            if v == 0:
                if ij[1] in s_l:
                    del s_l[ij[1]]
                    if len(s_l) == 0:
                        del s.im[ij[0]]
            else:
                s_l[ij[1]] = v
        else:
            raise TypeError

    def to_array(s):
        return [[s[i, j] for j in range(s.ca)] for i in range(s.ra)]

    def __setattr__(s, n, v):
        if n not in ['shape', 'T']:
            super().__setattr__(n, v)
            return
        if n == 'T':
            raise AttributeError
        if not (type(v) is tuple) or len(v) != 2 \
                or list(map(type, v)) != [int, int]:
            raise TypeError
        if v[0] * v[1] != s.ca * s.ra:
            raise TypeError

        if v == (s.ra, s.ca):
            super().__setattr__(n, v)
            return
        bra, bca = s.ra, s.ca
        s.ra, s.ca = v[0], v[1]
        res = CooSparseMatrix([], (v[0], v[1]))
        for rkey, row in s.im.items():
            for ckey in row.keys():
                shift = rkey * bra + ckey
                rnkey = shift // v[1]
                cnkey = shift % v[1]
                res[rnkey, cnkey] = row[ckey]
        s.im = res.im
        super().__setattr__(n, v)
        return

    def __getattr__(s, n):
        if n != 'T':
            super().__getattr__(n)
            return
        res = CooSparseMatrix([], (s.ca, s.ra))
        for rkey, row in s.im.items():
            for ckey in row.keys():
                res[ckey, rkey] = row[ckey]
        return res
