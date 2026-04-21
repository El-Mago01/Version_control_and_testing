import pytest
from main import upper_lower

def test_1():
    assert upper_lower("aAaafaasdfA") == True

def test_2():
    assert upper_lower("aaadf") == False

def test_3():
    assert upper_lower("AAb") == True

def test_4():
    assert upper_lower("") == False

def test_5():
    assert upper_lower("#") == False

def test_6():
    assert upper_lower("A") == False

def test_7():
    assert upper_lower("xyZx") == True

def test_8():
    assert upper_lower("xy\\Z\\nx") == False
