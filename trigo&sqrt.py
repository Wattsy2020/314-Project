import numpy as np
from random import randrange
import random


#can remove this duplicate function after combining, just for testing code now
# asserts that two values are equal within a delta

def assert_delta(x, y, delta=0.0001):

    assert abs(x - y) < delta, "x and y not equal"



#assert square root
def assert_squareRoot(x):

    assert  np.sqrt(x-1)<np.sqrt(x)<np.sqrt(x+1), "the square root of x is invalid, FAILED"
    print("the square root of x is valid, PASSED")
    
assert_squareRoot(random.uniform(-20.0,100.0))


#inverse square root
def assert_inversesquareRoot(x):

    assert_delta(x,(np.sqrt(x)**2))
    print("the square root of x is valid, PASSED")
    
assert_inversesquareRoot(random.uniform(-20.0,100.0))


#assert trigonometry
#assert sin(x)==sin(2pi+x)
def assert_sin(x):
    assert_delta((np.sin(x*np.pi)),(np.sin((x*np.pi)+(2*np.pi))))
    print("sin(x) and sin(360+x) are equal, PASSED")

assert_sin(random.random())



#assert cos(x)==cos(2pi+x)
def assert_cos(x):
    assert_delta((np.cos(x * np.pi)),(np.cos(x*np.pi+(2*np.pi))))
    print("cos(x) and cos(360+x) are equal, PASSED")

assert_cos(random.random())



#assert tan(x)==tan(2pi+x)
def assert_tan(x):
    assert_delta((np.tan(x*np.pi)),(np.tan(x*np.pi+(2*np.pi))))
    print("tan(x) and tan(360+x) are equal, PASSED")

assert_tan(random.random())



#assert metamorphic trigonometry
#assert sin(x)==-sin(2pi-x)
def assert_metaSin(x):
    assert_delta((np.sin(x * np.pi)),-(np.sin((2*np.pi)-(x * np.pi))))
    print("sin(x) and -sin(2pi-x) value are equal, PASSED")

assert_metaSin(random.random())


#assert cos(x)==cos(2pi-x)
def assert_metaCos(x):
    assert_delta((np.cos(x * np.pi)),(np.cos((2*np.pi)-(x * np.pi))))
    print("cos(x) and cos(2pi-x) value are equal, PASSED")

assert_metaCos(random.random())


#assert tan(x)==-tan(2pi-x)
def assert_metaTan(x):
    assert_delta((np.tan(x * np.pi)),-(np.tan((2*np.pi)-(x * np.pi))))
    print("tan(x) and -tan(2pi-x) value are equal, PASSED")

assert_metaTan(random.random())



#assert arcsin sin(sin-1(x))==x
def assert_arcsin(x):
    assert_delta((np.sin(np.arcsin(x))), x)
    print("sin(x) and arcsin(x) are inverse relation, PASSED")

assert_arcsin(random.random())


#assert arccos cos(cos-1(x))==x
def assert_arccos(x):
    assert_delta((np.cos(np.arccos(x))), x)
    print("cos(x) and arccos(x) are inverse relation, PASSED")

assert_arccos(random.random())


#assert arctan tan(tan-1(x))==x
def assert_arctan(x):
    assert_delta((np.tan(np.arctan(x))), x)
    print("tan(x) and arctan(x) are inverse relation, PASSED")

assert_arctan(random.random())



