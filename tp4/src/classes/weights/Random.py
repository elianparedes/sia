import numpy as np

from src.classes.weights.WeightABC import WeightABC


class Random(WeightABC):

    def calculate(self, weights_qty):
        np.random.uniform(-1, 1, size=weights_qty)
