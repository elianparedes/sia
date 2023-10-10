from src.classes.weights.WeightABC import WeightABC
import numpy as np


class SetBased(WeightABC):
    """
    Calculates initial weights with random examples from a given set
    """

    def __init__(self, my_set: list):
        super().__init__()
        self.set = my_set

    def calculate(self, weight_qty: int) -> list[float]:
        return np.random.choice(self.set, size=weight_qty, replace=True).tolist()
