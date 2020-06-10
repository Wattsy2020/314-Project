import inspect
import linear_algebra_tests
import sqrt_tests
import trigonometry_tests

# note in future needs to record and print number of failures and where
def run_tests(module, show_examples=False):
    # get list of all test functions and their names in a module
    members = inspect.getmembers(module)
    test_functions = list(filter(lambda x: x[0][:5] == "test_", members))
    module_name = list(filter(lambda x: x[0][:8] == "__name__", members))[0][1]
    
    # loop through and run each test 100 times
    print("Testing {}.py\n".format(module_name))
    print("{0: <30}Status".format("Test Name"))
    for name, function in test_functions:
        print("{0: <30}".format(name), end="")
        try:
            for i in range(100):
                function()
        except AssertionError as e:
            print("Fail: {}".format(e))
        else:
            print("Pass")       
    if not show_examples: return
    
    # Loop through all functions and print the results of those with output
    print("\n\nTest case examples")
    for name, function in test_functions:
        result = function()
        if result is not None:
            print("Example for {}".format(name))
            print(result)
            print()
    
if __name__ == "__main__":
    run_tests(linear_algebra_tests, show_examples=True)
    print()
    run_tests(sqrt_tests)
    print()
    run_tests(trigonometry_tests)
