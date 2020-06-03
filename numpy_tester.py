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

# note in future needs to record and print number of failures and where
def run_tests():
    for i in range(100):
        test_inverse_1()
        test_inverse_2()
        test_inverse_3()
        test_inverse_4()

# run tests on our functions such as assert_matrix_equals
def test_testing_tool():
    for i in range(100):
        test_assert_matrix_equals()
    
if __name__ == '__main__':
    run_tests()
    test_testing_tool()
