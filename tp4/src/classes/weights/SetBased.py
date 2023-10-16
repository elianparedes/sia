import random
from src.classes.weights.WeightInitializerABC import WeightInitializerABC
import numpy as np


class SetBased(WeightInitializerABC):
    """
    Calculates initial weights with random examples from a given set
    """

    def __init__(self, my_set: list):
        super().__init__()
        self.set = my_set
        #arange randomly the indexes of the set
        self.order = np.arange(len(self.set))
        random.shuffle(self.order)
        print(self.order)
        self.value = 0

    def calculate(self, weight_qty: int) -> list[float]:
        # return [random.choice([row[i] for row in self.set]) for i in range(len(self.set[0]))]
        #return a random row
        toReturn = self.set[self.order[self.value]]
        self.value += 1
        print(toReturn)
        return toReturn
