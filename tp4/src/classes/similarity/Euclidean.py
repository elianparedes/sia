import numpy as np

from src.classes.similarity.SimilarityABC import SimilarityABC


class Euclidean(SimilarityABC):
    @classmethod
    def calculate(cls, expected, weights):
        return np.linalg.norm(np.array(expected)-np.array(weights), 2)
