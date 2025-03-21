import pytest
from bank import value

def test_hello():
    assert value("Hello, Newman") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("Hi") == 20
    assert value("Hey there") == 20
    assert value("h") == 20

def test_other():
    assert value("Goodbye") == 100
    assert value("What's up?") == 100
    assert value("Welcome") == 100

if __name__ == "__main__":
    pytest.main()
