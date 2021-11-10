"""Testing Divide"""
from calc.calculations.division import Division
def test_calculation_division():
    """test that calc has static method for divide"""
    #arrange
    mynumbers = (1.0,2.0)
    divide = division(mynumbers)
    #act
    #assert
    assert divide.get_result() == 2.0