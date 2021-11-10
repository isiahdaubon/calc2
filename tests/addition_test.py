"""Testing Addition"""
from calc.calculations.addition import Addition
def test_calculations_addition():
    """test that calc has static method for addition"""
    #arrange
    mynumbers = (1.0,2.0)
    addition = Addition(mynumbers)
    #act
    #assert
    assert addition.get_result() == 3.0
