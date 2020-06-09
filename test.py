import numpy as np
from random import randrange, random
from utilities import assert_delta, assert_matrix_equals, gen_matrix


def matrix_addition():
    A = gen_matrix(100, 100)
    B = -A
    O = np.zeros(A.shape)  # additive inverse (zero matrix of the same dimensions as A)
    print("A")
    print(A)
    print("B")
    print(B)
    print(O)
    result = A + B
    print(result)
    assert_matrix_equals(result, O)


def matrix_addition_fail():
    try:
        A = gen_matrix(6, 6)
        B = gen_matrix(6, 6)
        A_row = A.shape[0]
        A_col = A.shape[1]
        B_row = B.shape[0]
        B_col = B.shape[1]
        print("A")
        print(A)
        print("B")
        print(B)
        A = np.matrix(A)
        B = np.matrix(B)
        np.add(A, B)
    except ValueError:
        print("Test passed")
    else:
        raise AssertionError("Test Failed")

matrix_addition_fail()

