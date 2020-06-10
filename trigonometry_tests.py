import numpy as np
import random
from utilities import assert_delta


# assert sin(x)==sin(2pi+x)
def test_sin():
    x = random.random()
    assert_delta((np.sin(x*np.pi)),(np.sin((x*np.pi)+(2*np.pi))))

# assert cos(x)==cos(2pi+x)
def test_cos():
    x = random.random()
    assert_delta((np.cos(x * np.pi)),(np.cos(x*np.pi+(2*np.pi))))

# assert tan(x)==tan(2pi+x)
def test_tan():
    x = random.random()
    assert_delta((np.tan(x*np.pi)),(np.tan(x*np.pi+(2*np.pi))))

# assert sin(x)==-sin(2pi-x)
def test_metaSin():
    x = random.random()
    assert_delta((np.sin(x * np.pi)),-(np.sin((2*np.pi)-(x * np.pi))))

# assert cos(x)==cos(2pi-x)
def test_metaCos():
    x = random.random()
    assert_delta((np.cos(x * np.pi)),(np.cos((2*np.pi)-(x * np.pi))))

# assert tan(x)==-tan(2pi-x)
def test_metaTan():
    x = random.random()
    assert_delta((np.tan(x * np.pi)),-(np.tan((2*np.pi)-(x * np.pi))))

# assert arcsin sin(sin-1(x))==x
def test_arcsin():
    x = random.random()
    assert_delta((np.sin(np.arcsin(x))), x)

# assert arccos cos(cos-1(x))==x
def test_arccos():
    x = random.random()
    assert_delta((np.cos(np.arccos(x))), x)

# assert arctan tan(tan-1(x))==x
def test_arctan():
    x = random.random()
    assert_delta((np.tan(np.arctan(x))), x)
