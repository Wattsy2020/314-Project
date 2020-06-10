import numpy as np
from random import randrange

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

#square = True - creates a square matrix
#non_square = True - creates a non-square rectangle
#non_singular = True - creates a non singular matrix
# a convenience function for generating different type of random matrices
def gen_matrix(height_max, width_max, square = False, non_square = False, non_singular = False):
    if square and non_square:
        raise ValueError("Matrix cannot be square and non square")
    if square and height_max != width_max:
        raise ValueError("Max dimensions of a Square matrix must be the same")
    
    height = randrange(1, height_max + 1)
    width = height if square else randrange(1, width_max + 1)
    while non_square and height == width:
        width = randrange(1, width_max)
    
    A = np.random.uniform(-1, 1, (height, width)) # each entry is a random number in [-1, 1]
    while non_singular and np.linalg.matrix_rank(A) < min(A.shape): 
        A = np.random.rand(height, width)*2 - 1
    return A
