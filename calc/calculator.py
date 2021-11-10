""" This is the increment function"""
from calc.History.calculations import Calculations
#methods to calculate
class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def get_last_result_value():
        """This gets the result of the calculation"""
        Calculations.get_last_calculation_value()
        return True
    @staticmethod
    def add_numbers(tuple_values: tuple):
        """adds list of number"""
        Calculations.add_addition_calculation(tuple_values)
        return True
    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """subtract list of numbers from the result"""
        Calculations.add_subtraction_calculation(tuple_values)
        return True
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """multiply number from result"""
        Calculations.add_multiplication_calculation(tuple_values)
        return True
    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """divide number from result"""
        Calculations.add_division_calculation(tuple_values)
        return True