import numpy as np
from random import randrange
from utilities import *

# test the matrix inverse transformation using the property
# that the inverse of an inverse matrix A^-1 is A
def test_inverse_1():
    d = randrange(1, 100)
    A = np.random.rand(d, d) # matrix must be square to invert
    # regenerate matrix if it is singular (i.e. can't be inverted)
    while np.linalg.matrix_rank(A) < A.shape[0]: 
        A = np.random.rand(d, d)
    
    B = np.linalg.inv(np.linalg.inv(A))
    assert_matrix_equals(A, B)

# inverse of matrix with 0 determinant should be undefined and throw an exception
def test_inverse_2():
    d = randrange(1, 100)
    try: np.linalg.inv(np.zeros((d, d)))
    except: pass
    else: raise AssertionError("Inverse of a singular matrix is defined")

# inverse of a non square matrix should be undefined
def test_inverse_3():
    a = randrange(1, 100)
    b = randrange(1, 100)
    while b == a: # generate b until it's different to a
        b = randrange(1, 100)

    try: np.linalg.inv(np.random.rand(a, b))
    except: pass
    else: raise AssertionError("Inverse of a non square matrix is defined")

# test matrix inverse using the property that I^-1 = I
def test_inverse_4():
    A = np.identity(randrange(1, 100))
    B = np.linalg.inv(A)
    assert_matrix_equals(A, B)
