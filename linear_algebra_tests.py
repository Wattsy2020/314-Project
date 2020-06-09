import numpy as np
from random import randrange, random
from utilities import assert_delta, assert_matrix_equals, gen_matrix

# test the matrix inverse transformation using the property
# that the inverse of an inverse matrix A^-1 is A
def test_inverse_1():
    A = gen_matrix(100, 100, square=True, non_singular=True) # matrix needs to be non_singular to inver
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
    A = gen_matrix(100, 100, non_square=True)
    try: np.linalg.inv(A)
    except: pass
    else: raise AssertionError("Inverse of a non square matrix is defined")

# test matrix inverse using the property that I^-1 = I
def test_inverse_4():
    A = np.identity(randrange(1, 100))
    B = np.linalg.inv(A)
    assert_matrix_equals(A, B)



# test the pseudo-inverse, an inverse that works for rectangular matrices
# first test that the pseudo-inverse behaves likes the standard inverse for square matrices
def test_pseudo_inverse_1():
    A = gen_matrix(100, 100, square=True, non_singular=True)
    B = np.linalg.pinv(np.linalg.pinv(A))
    assert_matrix_equals(A, B)
    
# the below 4 tests are based on the properties the pseudo inverse has as described on wikipedia
# here: https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse#Definition
def test_pseudo_inverse_2():
    A = gen_matrix(100, 100)
    B = np.linalg.pinv(A)
    assert_matrix_equals(A, np.dot(np.dot(A, B), A))

def test_pseudo_inverse_3():
    A = gen_matrix(100, 100)
    B = np.linalg.pinv(A)
    assert_matrix_equals(B, np.dot(np.dot(B, A), B))

def test_pseudo_inverse_4():
    A = gen_matrix(100, 100)
    B = np.linalg.pinv(A)
    AB = np.dot(A, B)
    assert_matrix_equals(AB, AB.T)

def test_pseudo_inverse_5():
    A = gen_matrix(100, 100)
    B = np.linalg.pinv(A)
    BA = np.dot(B, A)
    assert_matrix_equals(BA, BA.T)


# test determinant using the property that the absolute value
# of it doesn’t change when rows are swapped
# (determinant can flip signs depending on which rows are swapped)
def test_determinant_1():
    # determinant can become quite large for large matrices
    # throwing off assert_delta, so the dimension must be restricted to 50
    A = gen_matrix(50, 50, square=True)
    B = np.copy(A)
    
    # swap two random rows in B
    row1, row2 = randrange(0, B.shape[0]), randrange(0, B.shape[0])
    B[[row1, row2]] = B[[row2, row1]]
    
    assert_delta(abs(np.linalg.det(A)), abs(np.linalg.det(B)))

# test determinant using the property that it scales by A when a row is multiplied by A
def test_determinant_2():
    A = gen_matrix(50, 50, square=True)
    B = np.copy(A)
    scale_factor = random()
    B[randrange(0, B.shape[0]), :] *= scale_factor # scale a random row by scale_factor
    
    assert_delta(scale_factor*np.linalg.det(A), np.linalg.det(B))

# test determinant using the property that if the determinant of a matrix is
# A then determinant of the inverse is 1/A
def test_determinant_3():
    A = gen_matrix(50, 50, square=True, non_singular=True)
    B = np.linalg.inv(A)
    assert_delta(np.linalg.det(A), 1/np.linalg.det(B))

# test that determinant fails for non square matrix
def test_determinant_4():
    A = gen_matrix(50, 50, non_square=True)
    try: np.linalg.det(A)
    except: pass
    else: raise AssertionError("Determinant of a non square matrix is defined")



# test the matrix_rank calculation using the property that swapping rows doesn't affect rank
def test_rank_1():
    A = gen_matrix(100, 100)
    B = np.copy(A)
    
    # swap two random rows in B
    row1, row2 = randrange(0, B.shape[0]), randrange(0, B.shape[0])
    B[[row1, row2]] = B[[row2, row1]]

    assert np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B), "ranks not equal"
    
# test the matrix_rank calculation using the property that
# if one row is a linearly scaled version of the other the rank decreases by 1
def test_rank_2():
    A = gen_matrix(100, 100)
    B = np.copy(A)
    
    # make one row = a linearly scaled version of another
    row1, row2 = randrange(0, B.shape[0]), randrange(0, B.shape[0])
    B[row1, :] = random()*B[row2, :] + random()
    
    assert np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B), "ranks not equal"

# rank of the inverse matrix should be the same
def test_rank_3():
    A = gen_matrix(100, 100, square=True, non_singular=True)
    B = np.linalg.inv(A)
    assert np.linalg.matrix_rank(A) == np.linalg.matrix_rank(B), "ranks not equal"

# the rank of a matrix <= min(number of rows, number of colums)
def test_rank_4():
    A = gen_matrix(100, 100)
    assert np.linalg.matrix_rank(A) <= min(A.shape), "rank is greater than number of rows"
    
    

# test transpose using the fact that A^T^T = A
def test_transpose_1():
    A = gen_matrix(100, 100)
    assert_matrix_equals(A, A.T.T)

# test transpose using the fact that it must swap the dimensions of a matrix
def test_transpose_2():
    A = gen_matrix(100, 100)
    assert list(A.T.shape) == list(reversed(A.shape)), "Dimensions don't swap"
    
# test transpose using the fact that transposing a diagonal matrix doesn't change it
def test_transpose_3():
    A = np.identity(randrange(1, 100))*random()
    assert_matrix_equals(A, A.T)
    


# test eigenvalue solving using the fact that the eigenvalues of A and A.T are the same
def test_eigen_1():
    A = gen_matrix(100, 100, square=True)
    # calculate the eigenvalues and sort them so we can compare (as eigenvalue are given in not necessarily the same order)
    A_eigenvalue = np.sort(np.linalg.eig(A)[0])
    AT_eigenvalue = np.sort(np.linalg.eig(A.T)[0])
    
    # reshape into a 2 dimensional matrix so we can use assert_matrix_equals to compare
    shape = [A.shape[0], 1]
    assert_matrix_equals(A_eigenvalue.reshape(shape), AT_eigenvalue.reshape(shape))

# test eigenvector solving using the fact that the eigenvectors of A and A inverse are the same
def test_eigen_2():
    A = gen_matrix(100, 100, square=True)
    # calculate the eigenvectors and values
    A_eigenvalue, A_eigenvector = np.linalg.eig(A)
    AI_eigenvalue, AI_eigenvector = np.linalg.eig(np.linalg.inv(A))
    
    # sort the eigenvectors using the fact that A_eigenvalue[i] is the corresponding
    # eigenvalue for A_eigenvector[i]
    # and also that the eigenvalues of A_inverse = 1/eigenvalues of A
    A_eigenvector = A_eigenvector[np.argsort(A_eigenvalue)] # sort vectors how the values would be sorted
    AI_sorting_order = np.array(list(reversed(np.argsort(A_eigenvalue)))) # needs to be reversed due to comment above
    AI_eigenvector = AI_eigenvector[AI_sorting_order]
    
    assert_matrix_equals(A_eigenvector, AI_eigenvector)

# test eigenvector and eigenvalue solving using the fact that they satisfy the property
# Ax = lambda*x   (the property used to define what eigenvalues and vectors are)


# assert that eigensolving only works on square matrices
