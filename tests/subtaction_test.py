"""Testing Subtraction"""
from calc.calculations.subtraction import Subtraction
def test_calculation_subtraction():
    """test that calc has static method for subtraction"""
    #arrange
    mynumbers = (1.0,2.0)
    subtraction = Subtraction(mynumbers)
    #act
    #assert
    assert subtraction.get_result() == -3
