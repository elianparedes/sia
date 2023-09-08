import math

from src.classes.genes.GeneABC import GeneABC


class Agility(GeneABC):

    def __init__(self, value):
        super().__init__(value)

    def get_p(self):
        return math.tanh(self.value * 0.01)

    def __hash__(self):
        return hash((self.value, Agility))

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Agility):
            return math.isclose(other.value, self.value, rel_tol=1e-03)
        else:
            return False

    def __str__(self):
        return self.value.__str__()

