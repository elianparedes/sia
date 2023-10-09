import math

from src.classes.similarity.SimilarityABC import SimilarityABC
from src.classes.similarity.Euclidean import Euclidean


class Exponential(SimilarityABC):

    @classmethod
    def calculate(cls, expected, weights):
        euclidean = Euclidean.calculate(expected, weights)
        return math.exp(-1 * (euclidean ** 2))
