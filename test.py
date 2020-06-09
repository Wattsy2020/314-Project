import numpy as np
from random import randrange
from utilities import *


def multiplication_test():
    dim = randrange(1, 100)
    A = gen_matrix(dim, dim, square=True)  # generate a random square matrix
    B = np.linalg.inv(A)
    dot = np.dot(A, B)  # this should be = identity matrix
    print("dot")
    print(dot)
    identity = np.identity(A.shape[0])  # create the identity matrix with the same shape as A
    print("identity")
    print(identity)
    assert_matrix_equals(dot, identity)


def matrix_multiplication2():
    dim = randrange(1, 100)
    random_int = randrange(1, 1000)
    A = gen_matrix(dim, dim, square=True)
    scalar_product = random_int*A
    scalar_product = np.dot(scalar_product, A)
    dot = np.dot(A, A)
    dot = dot*random_int
    print("scalar")
    print(scalar_product)
    print("dot")
    print(dot)
    assert_matrix_equals(scalar_product, dot)

multiplication_test()
matrix_multiplication2()


