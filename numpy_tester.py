import inspect
import linear_algebra_tests

# note in future needs to record and print number of failures and where
def run_tests():
    # get list of all test functions and their names in linear_algebra test
    members = inspect.getmembers(linear_algebra_tests)
    test_functions = list(filter(lambda x: x[0][:5] == "test_", members))
    
    # loop through and run each test 100 times
    print("Testing linear_algebra_tests.py\n")
    print("{0: <30}Status".format("Function"))
    for name, function in test_functions:
        print("{0: <30}".format(name), end="")
        try:
            for i in range(100):
                function()
        except AssertionError as e:
            print("Fail: {}".format(e))
        else:
            print("Pass")
    
if __name__ == "__main__":
    run_tests()
