import numpy as np

def swap_rows(M,a,b):
    M[[a,b],:] = M[[b,a],:]


def swap_cols(M,a,b):
    M[:,[a,b]] = M[:, [b,a]]