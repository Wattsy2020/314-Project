import pytest
import numpy as np

# asserts that two values are equal within a delta
def assert_delta(x, y, delta=0.0001):
    assert abs(x - y) < delta, "x ({}) and y ({}) are not equal".format(x, y)

# asserts every value of the matrix is equal (within a delta) elementwise
def assert_matrix_equals(X, Y, delta=0.0001):
    if not X.shape == Y.shape:
        raise ValueError("X and Y have different shape")
    if not len(X.shape) == len(Y.shape) == 2:
        raise ValueError("X or Y are not 2 dimensional matrices")

    # loop through and assert every value is equal
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            assert_delta(X[i, j], Y[i, j], delta)
