import math
import random

from src.classes.genes.GeneABC import GeneABC


class Intelligence(GeneABC):

    def __init__(self, value):
        super().__init__(value)

    def get_p(self):
        return 0.6 * math.tanh(self.value * 0.01)

    def __hash__(self):
        return hash((self.value, Intelligence))

    def __eq__(self, other):
        if other is None:
            return False
        if isinstance(other, Intelligence):
            return self.value == other.value
        else:
            return False

    def __str__(self):
        return self.value.__str__()

    def mutate(self):
        new_val = random.uniform(0, 150)
        return Intelligence(new_val)
