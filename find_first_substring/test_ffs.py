import pytest
from ffs import first_substr

def test_first_substr():
    assert first_substr("hello", "o") == 4

def test_first_substr_found_twice():
    assert first_substr("hello", "l") == 2

def test_first_substr_not_found():
    assert first_substr("hello", "x") == -1

def test_first_substr_empty_string():
    assert first_substr("", "a") == -1

def test_first_substr_first_char():
    assert first_substr("abc", "a") == 0

def test_first_substr_last_char():
    assert first_substr("abc", "c") == 2

def test_first_substr_case_sensitive():
    assert first_substr("Hello", "h") == -1

def test_first_substr_special_char():
    assert first_substr("hello!", "!") == 5