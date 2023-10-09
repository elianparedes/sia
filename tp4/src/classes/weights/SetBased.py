from src.classes.weights.WeightABC import WeightABC
import numpy as np


class SetBased(WeightABC):

    def __init__(self, my_set: set) -> None:
        super().__init__()
        self.set = my_set

    def calculate(self, weight_qty):
        np.random.choice(self.set, size=weight_qty, replace=True)
