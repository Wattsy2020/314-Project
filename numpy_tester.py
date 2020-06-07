from linear_algebra_tests import *
from utilities import *

# note in future needs to record and print number of failures and where
def run_tests():
    for i in range(100):
        test_inverse_1()
        test_inverse_2()
        test_inverse_3()
        test_inverse_4()
        
        test_determinant_1()
        test_determinant_2()
        test_determinant_3()
        test_determinant_4()
        
        test_rank_1()
        test_rank_2()
        test_rank_3()
        test_rank_4()
    
if __name__ == '__main__':
    run_tests()
    print("Numpy tests passed")
