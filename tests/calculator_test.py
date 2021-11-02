"""Testing the Calculator"""
import pytest

from calculator.main import Calculator

def test_calculator_result():
        """testing calculator result is 0"""
        calc = Calculator()
        assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    calc = Calculator
    assert calc.add_number(1,3)

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator
    assert calc.subtract_number(1,3)

def test_calculator_multiply():
    """ tests multiplication of two numbers"""
    calc = Calculator
    assert calc.multiply_numbers(3,1)


def test_calculator_divide():
    """tests division of two numbers"""
    calc = Calculator
    assert calc.divide_numbers(1,3)

def test_calculator_division_error():
    """ tests dividing by 0 exception """
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(3, 0)


