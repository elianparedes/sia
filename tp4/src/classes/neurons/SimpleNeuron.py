import numpy as np

from src.classes.neurons.NeuronABC import NeuronABC


class SimpleNeuron(NeuronABC):
    def __init__(self, input_qty: int, test_set=None):
        """
		:param input_qty: Number of input neurons in input layer
		:param test_set: If included it chooses weights from test_set, otherwise randomly assigned
		"""
        if test_set is None:
            self.weights = np.random.uniform(-1, 1, size=input_qty)
        else:
            self.weights = np.random.choice(test_set, size=input_qty, replace=True)

    @property
    def weights(self):
        return self.weights
