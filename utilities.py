import numpy as np
from random import randrange

# asserts that two values are equal within a delta
def assert_delta(x, y, delta=0.0001):
    assert abs(x - y) < delta, "x and y not equal"

# asserts every value of the matrix is equal (within a delta) elementwise
def assert_matrix_equals(X, Y, delta=0.0001):
    assert X.shape == Y.shape, "X and Y have different shape"
    assert len(X.shape) == 2, "X and Y are not 2 dimensional matrices"

    # loop through and assert every value is equal
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            assert_delta(X[i, j], Y[i, j], delta)

# test the testing tool
def test_assert_matrix_equals():
    dims = randrange(1, 100), randrange(1, 100)
    A = np.random.random_sample(dims)
    B = A - randrange(1, 500)
    try:
        assert_matrix_equals(A, B)
    except:
        pass # test passed, assert_matrix should through exception
    else:
        raise AssertionError("assert_matrix_equals claims two unequal matrices are equal")
