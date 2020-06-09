import numpy as np
from random import randrange
import random


#assert square root
def assert_squareRoot(x):
    assert  np.sqrt(x-1)<np.sqrt(x)<np.sqrt(x+1), "the square root of x is invalid, FAILED"
    
try:
    assert_squareRoot(random.uniform(-20.0,100.0))
except:
    pass
else:
    raise AssertionError("x is negative, FAILED")


#inverse square root
def assert_squareRoot(x):
    assert  round(x,8)==round(np.sqrt(x)**2,8), "the square root of x is invalid, FAILED"
    #round() is applied for the testing to be valid up to 8 decimal places, otherwise all will result in failure
try:
    assert_squareRoot(random.uniform(-20.0,100.0))
except:
    pass
else:
    raise AssertionError("x is negative, FAILED")




#assert trigonometry
#assert sin(x)==sin(2pi+x)
def assert_sin(x):
    assert round(np.sin(x*np.pi),8)==round(np.sin((x*np.pi)+(2*np.pi)),8), "sin(x) and sin(360+x) are not equal, FAILED"
    print("sin(x) and sin(360+x) are equal, PASSED")

assert_sin(random.random())



#assert cos(x)==cos(2pi+x)
def assert_cos(x):
    assert round(np.cos(x * np.pi),8)==round(np.cos(x*np.pi+(2*np.pi)),8), "cos(x) and cos(360+x) are not equal, FAILED"
    print("cos(x) and cos(360+x) are equal, PASSED")

assert_cos(random.random())



#assert tan(x)==tan(2pi+x)
def assert_tan(x):
    assert round(np.tan(x*np.pi),8)==round(np.tan(x*np.pi+(2*np.pi)),8), "tan(x) and tan(360+x) are not equal, FAILED"
    print("tan(x) and tan(360+x) are equal, PASSED")

assert_tan(random.random())



#assert metamorphic trigonometry
#assert sin(x)==-sin(2pi-x)
def assert_metaSin(x):
    assert round(np.sin(x * np.pi),8)==-(round(np.sin((2*np.pi)-(x * np.pi)),8)), "sin(x) and -sin(2pi-x) value are not equal, FAILED"
    print("sin(x) and -sin(2pi-x) value are equal, PASSED")

assert_metaSin(random.random())


#assert cos(x)==cos(2pi-x)
def assert_metaCos(x):
    assert round(np.cos(x * np.pi),8)==round(np.cos((2*np.pi)-(x * np.pi)),8) , "cos(x) and cos(2pi-x) value are not equal, FAILED"
    print("cos(x) and cos(2pi-x) value are equal, PASSED")

assert_metaCos(random.random())


#assert tan(x)==-tan(2pi-x)
def assert_metaTan(x):
    assert round(np.tan(x * np.pi),8)==-(round(np.tan((2*np.pi)-(x * np.pi)),8)), "tan(x) and -tan(2pi-x) value are not equal, FAILED"
    print("tan(x) and -tan(2pi-x) value are equal, PASSED")

assert_metaTan(random.random())



#assert arcsin sin(sin-1(x))==x
def assert_arcsin(x):
    assert round(np.sin(np.arcsin(x)),8)==round(x,8), "sin(x) and arcsin(x) are not inverse relation, FAILED"
    print("sin(x) and arcsin(x) are inverse relation, PASSED")

assert_arcsin(random.random())


#assert arccos cos(cos-1(x))==x
def assert_arccos(x):
    assert round(np.cos(np.arccos(x)),8)==round(x,8), "cos(x) and arccos(x) are not inverse relation, FAILED"
    print("cos(x) and arccos(x) are inverse relation, PASSED")

assert_arccos(random.random())


#assert arctan tan(tan-1(x))==x
def assert_arctan(x):
    assert round(np.tan(np.arctan(x)),8)==round(x,8), "tan(x) and arctan(x) are not inverse relation, FAILED"
    print("tan(x) and arctan(x) are inverse relation, PASSED")

assert_arctan(random.random())



