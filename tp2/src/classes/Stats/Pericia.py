import math


class Pericia:

    def __init__(self, value):
        self.value = value

    def get_p(self):
        return 0.6 * math.tanh(self.value * 0.01)

    def __hash__(self):
        return hash((self.value, Pericia))

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Pericia):
            return self.value == other.value
        else:
            return False
