import math

class Fuerza:

    def __init__(self, value):
        self.value = value

    def get_p(self):
        return 100 * math.tanh(self.value * 0.01)

    def __hash__(self):
        return hash((self.value, Fuerza))

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Fuerza):
            return self.value == other.value
        else:
            return False
