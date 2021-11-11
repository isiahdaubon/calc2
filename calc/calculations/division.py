"""Division Class"""
from calc.calculations.calculation import Calculation
import pytest


class Division(Calculation):
    """Division Calculation Object"""
    def get_result(self):
        """get the division results"""
        result = 1.0
        for value in self.values:
            result = result / value
        return result


