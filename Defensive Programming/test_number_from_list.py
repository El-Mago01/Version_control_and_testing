import pytest
from number_from_list import number_from_list

def test_normal_inputs():
    assert number_from_list([1]) == 1
    assert number_from_list([2]) == 2
    assert number_from_list([1,0]) == 10
    assert number_from_list([1,2,3,4,5,6,7,8,9]) == 123456789
    assert number_from_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 123456789


def test_ValueError_cases1():
    with pytest.raises(ValueError):
        number_from_list([1,2,3,4,5,6,7,8,9,10])

def test_ValueError_cases2():
    with pytest.raises(ValueError):
        number_from_list([10,12,13,14,15,16,17,18,19,20])

def test_ValueError_cases3():
    with pytest.raises(ValueError):
        number_from_list([])

def test_TypeError_cases1():
    with pytest.raises(TypeError):
        number_from_list(['a', 1, 2, 3, 4, 5, 6, 7, 8, 9])

def test_TypeError_cases2():
    with pytest.raises(TypeError):
        number_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 1.1])

def test_TypeError_cases3():
    with pytest.raises(TypeError):
        number_from_list(['-', 2, 3, 4, 5, 6, 7, 8, 9])

def test_TypeError_cases4():
    with pytest.raises(TypeError):
        number_from_list([2, 3, 4, 5, 6, 7, '.', 8, 9])



pytest.main()
