from typing import Any
from src.calculator import Calculator
def test_add():
    cal = Calculator()
    assert cal.add(3) == 3

def test_subtract():
    cal = Calculator()
    assert cal.subtract(1) == -1

def test_multiply():
    cal = Calculator()
    assert cal.multiply(15) == 0

def test_divide():
    cal = Calculator()
    assert cal.divide(0) == 0