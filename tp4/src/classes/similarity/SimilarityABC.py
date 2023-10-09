from abc import ABC, abstractmethod


class SimilarityABC(ABC):

	@abstractmethod
	@classmethod
	def calculate(cls, expected, weights):
		pass
