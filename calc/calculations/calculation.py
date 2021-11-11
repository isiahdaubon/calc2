"""Calculation Class"""
class Calculation:
    """Calculation abstract base class"""
    #pylint: disable=too-few-public-methods
    def __init__(self,values: tuple):
        """Constructor Method"""
        self.values = Calculation.convert_args_to_tuple_of_float(values)
    @staticmethod
    def convert_args_to_tuple_of_float(values):
        """standardize values to list floats"""
        list_values_float = []
        for item in values:
            list_floats_float.append(float(item))
        return tuple(list_values_float)
