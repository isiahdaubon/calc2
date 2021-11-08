"""This is the addition calculation that is being inherits the value A and value B from the calculation class"""

from calc.calculation import Calculation


class Addition(Calculation):
    """This is the addition class"""
    def getResult(self):
        """This is the addition class"""
        return self.value_a + self.value_b
