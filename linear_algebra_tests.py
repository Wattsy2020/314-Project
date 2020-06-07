import numpy as np
from random import randrange, random
from utilities import assert_delta, assert_matrix_equals

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

# test determinant using the property that the absolute value
# of it doesn’t change when rows are swapped
# (determinant can flip signs depending on which rows are swapped)
def test_determinant_1():
    # determinant can become quite large for large matrices
    # throwing off assert_delta, so the dimension must be restricted to 50
    d = randrange(1, 50)
    A = np.random.rand(d, d)
    B = np.copy(A)
    
    # swap two random rows in B
    row1, row2 = randrange(0, d), randrange(0, d)
    B[[row1, row2]] = B[[row2, row1]]
    
    assert_delta(abs(np.linalg.det(A)), abs(np.linalg.det(B)))

# test determinant using the property that it scales by A when a row is multiplied by A
def test_determinant_2():
    d = randrange(1, 50)
    scale_factor = random()
    A = np.random.rand(d, d)
    B = np.copy(A)
    B[randrange(0, d), :] *= scale_factor # scale a random row by scale_factor
    
    assert_delta(scale_factor*np.linalg.det(A), np.linalg.det(B))

# test determinant using the property that if the determinant of a matrix is
# A then determinant of the inverse is 1/A
def test_determinant_3():
    d = randrange(1, 50)
    A = np.random.rand(d, d)
    B = np.linalg.inv(A)
    
    assert_delta(np.linalg.det(A), 1/np.linalg.det(B))

# test that determinant fails for non square matrix
def test_determinant_4():
    a = randrange(1, 100)
    b = randrange(1, 100)
    while b == a: # generate b until it's different to a
        b = randrange(1, 100)
        
    try: np.linalg.det(np.random.rand(a, b))
    except: pass
    else: raise AssertionError("Determinant of a non square matrix is defined")
