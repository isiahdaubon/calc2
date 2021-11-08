""" This is the increment function"""
from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
class Calculator:
    """ This is the Calculator class"""

    history = []

    @staticmethod
    def add_calculation_to_history(calculation):
        """Add the results to the history"""
        Calculator.history.append(calculation)

    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """Add the first result to history"""
        return Calculator.history[0].getResult()

    @staticmethod
    def get_last_calculation_object():
        """Retrieves the latest result in history"""
        return Calculator.history[-1]

    @staticmethod
    def clear_history():
        """Clear the history"""
        Calculator.history.clear()
        return Calculator.count_history()

    @staticmethod
    def count_history():
        """Count the length of the history"""
        return len(Calculator.history)

    @staticmethod
    def add_number(value_a,value_b):
        """Adds two numbers are returns the sum"""
        Calculator.add_calculation_to_history(Addition.create(value_a, value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def subtract_number(value_a, value_b):
        """subtracts the two numbers and returns difference"""
        Calculator.add_calculation_to_history(Subtraction.create(value_a,value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """multiply the two numbers and return the product"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a, value_b))
        return Calculator.get_last_calculation_result()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """divide the two numbers and return the quotient"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_last_calculation_result()