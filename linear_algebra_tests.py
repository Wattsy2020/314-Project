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
    except np.linalg.LinAlgError: pass
    else: raise AssertionError("Inverse of a singular matrix is defined")

# inverse of a non square matrix should be undefined
def test_inverse_3():
    A = gen_matrix(100, 100, non_square=True)
    try: np.linalg.inv(A)
    except np.linalg.LinAlgError: pass
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
    A = gen_matrix(25, 25, square=True)
    B = np.copy(A)
    
    # swap two random rows in B
    row1, row2 = randrange(0, B.shape[0]), randrange(0, B.shape[0])
    B[[row1, row2]] = B[[row2, row1]]
    
    assert_delta(abs(np.linalg.det(A)), abs(np.linalg.det(B)))

# test determinant using the property that it scales by A when a row is multiplied by A
def test_determinant_2():
    A = gen_matrix(25, 25, square=True)
    B = np.copy(A)
    scale_factor = random()
    B[randrange(0, B.shape[0]), :] *= scale_factor # scale a random row by scale_factor
    
    assert_delta(scale_factor*np.linalg.det(A), np.linalg.det(B))

# test determinant using the property that if the determinant of a matrix is
# A then determinant of the inverse is 1/A
def test_determinant_3():
    A = gen_matrix(25, 25, square=True, non_singular=True)
    B = np.linalg.inv(A)
    assert_delta(np.linalg.det(A), 1/np.linalg.det(B))

# test that determinant fails for non square matrix
def test_determinant_4():
    A = gen_matrix(25, 25, non_square=True)
    try: np.linalg.det(A)
    except np.linalg.LinAlgError: pass
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
    A_eigenvalues = np.sort(np.linalg.eig(A)[0])
    AT_eigenvalues = np.sort(np.linalg.eig(A.T)[0])
    
    # reshape into a 2 dimensional matrix so we can use assert_matrix_equals to compare
    shape = [A.shape[0], 1]
    assert_matrix_equals(A_eigenvalues.reshape(shape), AT_eigenvalues.reshape(shape))

# test eigenvector and eigenvalue solving using the fact that they satisfy the property
# Ax = lambda*x   (the property used to define what eigenvalues and vectors are)
def test_eigen_2():
    A = gen_matrix(100, 100, square=True)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    # assert the property holds for each vector and value pair
    Ax = np.dot(A, eigenvectors)
    lx = eigenvalues.reshape(1, A.shape[0])*eigenvectors # multiply each eigenvalue by corresponding vector
    assert_matrix_equals(Ax, lx)
    
# eigensolving should throw an exception for non square matrices
def test_eigen_3():
    A = gen_matrix(100, 100, non_square=True)
    try: np.linalg.eig(A)
    except np.linalg.LinAlgError: pass
    else: raise AssertionError("Eigensolver should not be able to solve a non square matrix") 
    
    
    
# test the (frobenius) norm of a matrix, norm = sqrt(sum of squares of all values in the matrix)
# first using the fact it shouldn't change for the transpose of a matrix
def test_norm_1():
    A = gen_matrix(100, 100)
    assert_delta(np.linalg.norm(A), np.linalg.norm(A.T))
    
# second use the fact that when the matrix is scaled by a scalar B the norm should also be scaled by abs(B)
def test_norm_2():
    A = gen_matrix(100, 100)
    scalar = random()*2 - 1 # random number on interval [-1, 1]
    assert_delta(np.linalg.norm(scalar*A), abs(scalar)*np.linalg.norm(A))
    
# the norm should always be >= 0
def test_norm_3():
    A = gen_matrix(100, 100)
    assert np.linalg.norm(A) >= 0
    
# As https://mathworld.wolfram.com/MatrixNorm.html points out the above properties are met
# by any matrix norm, not specifically the frobenius norm, this test ensures that the frobenius norm
# is being calculated using the fact that the norm of a diagonal matrix can be calculates as below 
# norm(aI) = sqrt(a^2 + a^2 + ... a^2) = sqrt(I.shape*a^2) = abs(a)*sqrt(I.shape)
def test_norm_4():
    I = np.identity(randrange(1, 100))
    a = random()*2 - 1
    assert_delta(np.linalg.norm(a*I), np.abs(a)*np.sqrt(I.shape[0])) 



# test the linalg.solve(A, b) which solves for x in the equation Ax = b
# linalg.solve(A, Identity) and linalg.solve(Identity, A) should be the inverse of each other
# as you can transform Ax = I by multiplying by x_inv to see A = Ix_inv i.e. Ix_inv = A
def test_solve_1():
    A = gen_matrix(100, 100, square=True)
    I = np.identity(A.shape[0])
    X1 = np.linalg.solve(A, I)
    X2 = np.linalg.solve(I, A)
    assert_matrix_equals(X1, np.linalg.inv(X2))

# linalg.solve(Identity, random_vector) should give x = random_vector
def test_solve_2():
    vector = gen_matrix(100, 2) # generates a random vector with size randrange(1, 100), 1
    X = np.linalg.solve(np.identity(vector.shape[0]), vector)
    assert_matrix_equals(X, vector)

# linalg.solve(A, Ainverse) should give x = (Ainverse)^2
def test_solve_3():
    A = gen_matrix(100, 100, square=True)
    Ainv = np.linalg.inv(A)
    X = np.linalg.solve(A, Ainv)
    assert_matrix_equals(X, np.dot(Ainv, Ainv))

# check that it fails for non square matrices
def test_solve_4():
    A = gen_matrix(100, 100, non_square=True)
    try: np.linalg.solve(A, A)
    except np.linalg.LinAlgError: pass
    else: raise AssertionError("Solver should not solve for non-square matrices")

# check that it fails for incorrect dimensions e.g. if A is X by X but b is 2*X by 1
def test_solve_5():
    A = gen_matrix(10, 10, square=True)
    B = gen_matrix(100, 2)
    # ensure that B has more rows than A
    while B.shape[0] <= A.shape[0]:
        B = gen_matrix(100, 2)
        
    try: np.linalg.solve(A, B)
    except ValueError: pass
    else: raise AssertionError("Solve should not solve for incorrect dimensions")
