import random
from src.classes.weights.WeightsInitializerABC import WeightInitializerABC
import numpy as np


class SetBased(WeightInitializerABC):
    """
    Calculates initial weights with random examples from a given set
    """

    def __init__(self, my_set: list):
        super().__init__()
        self.set = my_set

    def calculate(self, weight_qty: int) -> list[float]:
        return [random.choice([row[i] for row in self.set]) for i in range(len(self.set[0]))]
