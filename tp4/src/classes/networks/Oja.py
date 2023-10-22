import numpy as np

from src.classes.networks.NetworkABC import NetworkABC
from src.classes.neurons.SimpleNeuron import SimpleNeuron


class Oja(NetworkABC):

    def __init__(self, neuron_quantity, weight_calculator):
        self.neuron_quantity = neuron_quantity
        self.neurons = SimpleNeuron(neuron_quantity, weight_calculator)

    def get_activation(self, input_vector):
        weights = self.neurons.get_weights()
        return np.dot(input_vector, weights)

    def update_weights(self, activation, learning_rate, input_vector):
        weights = self.neurons.get_weights()
        delta_weights = learning_rate * (input_vector * activation - (activation ** 2) * weights)
        self.neurons.set_weights(weights + delta_weights)
