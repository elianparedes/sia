from abc import ABC, abstractmethod


class NeuronABC(ABC):
	@abstractmethod
	def get_weights(self):
		pass


