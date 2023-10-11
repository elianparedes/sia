import numpy as np

from src.classes.weights.WeightsInitializerABC import WeightInitializerABC


class Random(WeightInitializerABC):
    """
    Calculates weights with random values
    """

    def calculate(self, weights_qty: int) -> list[float]:
        return np.random.uniform(-1, 1, size=weights_qty).tolist()
