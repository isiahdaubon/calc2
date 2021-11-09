"""This is the multiplication operation object"""

from calc.calculation import Calculation

class Multiplication(Calculation):
    """The is the multiplication class"""
    def get_result(self):
        """This is the multiplication class"""
        return self.value_a * self.value_b
