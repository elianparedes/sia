from abc import ABC


class GeneABC(ABC):

    def __init__(self, value: float):
        self.value = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.value + other
        elif isinstance(other, GeneABC):
            return self.value + other.value
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * other
        elif isinstance(other, GeneABC):
            return self.value * other.value
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")


