"""This is the addition operation object"""

from calc.calculation import Calculation


class Addition(Calculation):
    """This is the addition class"""
    def get_result(self):
        """This is the addition class"""
        return self.value_a + self.value_b
