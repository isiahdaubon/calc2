"""Calculation History Class"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
class Calculations:
    """Calculations class manages history of calculations"""
    history = []
    #pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clear history of calculations"""
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        """get the number of items in history"""
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation_object():
        """Get the last calculation"""
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_value():
        """get the last calculation"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        """get the first calculation"""
        return Calculations.history[0]
    @staticmethod
    def get_calculation(values):
        """get a specific calculation from history"""
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        """get a generic calculation from history"""
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        """Create an addition object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        """Create an subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_division_calculation(values):
        """Create an division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        """Create an multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return True


