import math
import random

from src.classes.genes.GeneABC import GeneABC


class Strength(GeneABC):

    def __init__(self, value):
        super().__init__(value)

    def get_p(self):
        return 100 * math.tanh(self.value * 0.01)

    def __hash__(self):
        return hash((self.value, Strength))

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Strength):
            return math.isclose(other.value, self.value, rel_tol=1e-03)
        else:
            return False

    def __str__(self):
        return self.value.__str__()


