from abc import ABC, abstractmethod


class StatABC(ABC):

    def __init__(self, value: float):
        self.value = value

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.value + other
        elif isinstance(other, StatABC):
            return self.value + other.value
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.value * other
        elif isinstance(other, StatABC):
            return self.value * other.value
        else:
            raise TypeError(f"Unsupported operand type: {type(other)}")

    @abstractmethod
    def mutate(self):
        pass
