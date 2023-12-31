import math


class Height:

    def __init__(self, value):
        self.value = value

    def get_ATM(self):
        return 0.5 - (3 * self.value - 5) ** 4 + (3 * self.value - 5) ** 2 + self.value / 2

    def get_DEM(self):
        return 2 + (3 * self.value - 5) ** 4 - (3 * self.value - 5) ** 2 - self.value / 2

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Height):
            return math.isclose(other.value, self.value, rel_tol=1e-03)
        else:
            return False

    def __str__(self):
        return self.value.__str__()
