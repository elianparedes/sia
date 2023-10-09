import numpy as np

from src.classes.networks.NetworkABC import NetworkABC


class Kohonen(NetworkABC):
    def __init__(self):
        self.network = None

    def generate(self, input_qty, test_set=None):
        """Generates Kohonen Network
		:param input_qty: Array of input layer
		:param test_set: If you wish to generate weights with random examples from the test set,
		otherwise it will follow a random uniform distribution
		"""

