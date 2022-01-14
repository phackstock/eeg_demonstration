from audioop import mul
from demo import add, subtract, multiply


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 2) == 1
    assert add(-1, -2) == -3


def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(1, -2) == 3
    assert subtract(-1, -2) == 1


def test_multiply():
    assert multiply(1, 2) == 2
    assert multiply(1, -2) == -2
    assert multiply(-1, -2) == 2
