"""This is our calculation base class / Abstract Class"""
class Calculation:
    """Initializing Objects"""
    def __init__(self,value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)

    @property
    def value_a(self):
        """Get For Value A"""
        return self._value_a

    @property
    def value_b(self):
        """Get For Value B"""
        return self._value_b