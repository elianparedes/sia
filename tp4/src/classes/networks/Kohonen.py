import numpy as np

from src.classes.networks.NetworkABC import NetworkABC
from src.classes.neurons.SimpleNeuron import SimpleNeuron


class Kohonen(NetworkABC):
    def __init__(self, weights_qty, neuron_qty, initial_environment, learning_rate, similarity_function, test_set=None):
        """Generates Kohonen Network
              :param weights_qty: Array of input layer
              :param test_set: If you wish to generate weights with random examples from the test set,
              otherwise it will follow a random uniform distribution
              """
        self.weights_qty = weights_qty
        self.neuron_qty = neuron_qty
        self.initial_environment = initial_environment
        self.learning_rate = learning_rate
        self.similarity_function = similarity_function
        self.output_layer = [[SimpleNeuron(weights_qty, test_set) for _ in range(neuron_qty)] for _ in range(neuron_qty)]


    def get_neighbours(self, x, y):
        pass