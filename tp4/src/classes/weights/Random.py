import numpy as np

from src.classes.weights.WeightInitializerABC import WeightInitializerABC


class Random(WeightInitializerABC):
    """
    Calculates weights with random values
    """

    def calculate(self, weights_qty: int) -> list[float]:
        return np.random.uniform(0, 1, size=weights_qty).tolist()
