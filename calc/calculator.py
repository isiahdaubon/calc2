""" This is the increment function"""
from calc.History.calculations import Calculations
from calc.calculations.subtraction import Subtraction
from calc.calculations.division import Division
from calc.calculations.addition import Addition
from calc.calculations.multiplication import Multiplication

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def add_numbers(*args):
        """adds list of numbers"""
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def subtract_numbers(*args):
        """subtract list of numbers from the result"""
        calculation = Subtraction(args)
        return calculation.get_result()
    @staticmethod
    def multiply_numbers(*args):
        """multiply number by result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def divide_numbers(*args):
        """divide number from result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()