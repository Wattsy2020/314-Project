from linear_algebra_tests import *
from utilities import *

# note in future needs to record and print number of failures and where
def run_tests():
    for i in range(100):
        test_inverse_1()
        test_inverse_2()
        test_inverse_3()
        test_inverse_4()
        
        test_pseudo_inverse_1()
        test_pseudo_inverse_2()
        test_pseudo_inverse_3()
        test_pseudo_inverse_4()
        test_pseudo_inverse_5()
        
        test_determinant_1()
        test_determinant_2()
        test_determinant_3()
        test_determinant_4()
        
        test_rank_1()
        test_rank_2()
        test_rank_3()
        test_rank_4()

        test_transpose_1()
        test_transpose_2()
        test_transpose_3()
        
        test_eigen_1()
        test_eigen_2()
        test_eigen_3()
        
        test_norm_1()
        test_norm_2()
        test_norm_3()
        test_norm_4()
        
        test_solve_1()
        test_solve_2()
        test_solve_3()
        test_solve_4()
        test_solve_5()
    
if __name__ == '__main__':
    run_tests()
    print("Numpy tests passed")
