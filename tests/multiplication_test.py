"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication
def test_calculation_multiplication():
    """test that calc has static method for multiplication"""
    #arrange
    mynumbers = (1.0,2.0)
    multiplication = Multiplication(mynumbers)
    #act
    #assert
    assert multiplication.get_result() == 2.0
