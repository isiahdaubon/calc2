""" This is the increment function"""
class Calculator:
    """ This is the Calculator class"""
    History = []
    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        return value_a + value_b

    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        return value_a - value_b

    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        return value_a * value_b

    @staticmethod
    def divide_numbers(value_a, value_b):
        """divide two numbers and store the result"""
        return  value_a / value_b
