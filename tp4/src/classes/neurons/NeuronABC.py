from abc import ABC, abstractmethod


class NeuronABC(ABC):
	@abstractmethod
	def get_weights(self) -> list[float]:
		pass

	@abstractmethod
	def set_weights(self, weights: list[float]):
		pass
