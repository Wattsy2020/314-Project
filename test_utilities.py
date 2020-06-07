import pytest
import numpy as np
from random import randrange
from utilities import assert_matrix_equals, assert_delta

# test that assert_matrix_equals throws an AssertError for unequal matrices
def test_assert_matrix_equals_1():
    dims = randrange(1, 100), randrange(1, 100)
    A = np.random.random_sample(dims)
    B = A - randrange(1, 500)
    
    # assert that this raises an error
    with pytest.raises(AssertionError):
        assert_matrix_equals(A, B)

# test there is no error for equal matrices
def test_assert_matrix_equals_2():
    dims = randrange(1, 100), randrange(1, 100)
    A = np.random.random_sample(dims)
    assert_matrix_equals(A, A)
    
# check it throws ValueError for matrices of different dimensions
def test_assert_matrix_equals_3():
    dims_a = randrange(1, 50), randrange(1, 50)
    dims_b = randrange(50, 100), randrange(50, 100)
    A = np.random.random_sample(dims_a)
    B = np.random.random_sample(dims_b)
    
    with pytest.raises(ValueError):
        assert_matrix_equals(A, B)

# check it throws ValueError for matrices for non 2 dimensional matrices
def test_assert_matrix_equals_4():
    dims = randrange(1, 100), randrange(1, 100), randrange(1, 100)
    A = np.random.random_sample(dims)
    
    with pytest.raises(ValueError):
        assert_matrix_equals(A, A)
        
if __name__ == '__main__':
    pytest.main()