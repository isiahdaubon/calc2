"""This is our calculation base class / Abstract Class"""
class Calculation: # pylint: disable=too-few-public-methods
    """class docstring""""""
    
       def __init__(self, value_a, value_b):
           """method""
           self.value_a = value_a
           self.value_b = value_b

       # Class Factory Method <- bound to the class and not the instance of the class
       @classmethod
       def create(cls,value_a,value_b):
           """docstring"""
           return cls(value_a,value_b)
