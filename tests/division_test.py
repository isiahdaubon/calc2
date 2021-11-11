"""Testing Divide"""
from calc.calculations.division import Division
def test_calculation_division():
    """test that calc has static method for divide"""
    #arrange
    mynumbers = (1.0,2.0)
    divide = division(mynumbers)
    #act
    #assert
    assert divide.get_result() == 0.50

    def test_calculator_division_error():
        """ tests dividing by 0 exception """
        # Arrange
        mynumbers = (1.0, 0.0, 1.0)
        divide = Division(mynumbers)
        # Act
        # Assert
        with pytest.raises(ZeroDivisionError):
            return result is True
