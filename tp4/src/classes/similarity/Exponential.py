import math

from src.classes.similarity.SimilarityABC import SimilarityABC
from src.classes.similarity.Euclidean import Euclidean


class Exponential(SimilarityABC):
    """
    Calculates similirity using the follwoing formula: e^(-||Xp - Wj||)^2
    """

    @classmethod
    def calculate(cls, expected: float, weights: list[float]) -> float:
        euclidean = Euclidean.calculate(expected, weights)
        return math.exp(-1 * (euclidean ** 2))
