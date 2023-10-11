from abc import ABC, abstractmethod


class SimilarityABC(ABC):
	"""
	Calculates the similarity between a given weight array and an expected value
	"""

	@classmethod
	def calculate(cls, expected: float, weights: list[float]) -> float:
		pass
