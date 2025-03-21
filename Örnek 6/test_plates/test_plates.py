import plates
from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("AB1234") == True

def test_start_with_letters():
    assert is_valid("123ABC") == False
    assert is_valid("A1B2C3") == False
    assert is_valid("AB123") == True

def test_no_leading_zero():
    assert is_valid("AB012") == False
    assert is_valid("AB123") == True

def test_alnum_only():
    assert is_valid("AB@12") == False
    assert is_valid("AB12") == True

def test_numbers_after_letters():
    assert is_valid("AB12C") == False
    assert is_valid("ABC123") == True

def test_1():
    assert is_valid("12") == False
