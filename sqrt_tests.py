import numpy as np
import random
from utilities import assert_delta

# assert square root is an increasing function
def test_square_root_1():
    x = random.uniform(1,100.0)
    assert  np.sqrt(x-1)<np.sqrt(x)<np.sqrt(x+1), "the square root of x is invalid, FAILED"

# test square root using the fact that x^2 is its inverse function
def test_square_root_2():
    x = random.uniform(1,100.0)
    assert_delta(x,(np.sqrt(x)**2))
    
# assert that square root fails for negative input (sqrt is not meant to give complex output so it should fail)
def test_square_root_3():
    x = random.uniform(-100, -1)
    try: np.sqrt(x)
    except Exception as e: print(e)
    else: raise AssertionError("Square root of negative number defined")
    