import numpy as np

from src.classes.networks.NetworkABC import NetworkABC
from src.classes.neurons.SimpleNeuron import SimpleNeuron


class Kohonen(NetworkABC):
    def __init__(self, weights_qty, neuron_qty, initial_environment, learning_rate, similarity_function,
                 weight_calculator):
        self.weights_qty = weights_qty
        self.neuron_qty = neuron_qty
        self.initial_environment = initial_environment
        self.learning_rate = learning_rate
        self.similarity_function = similarity_function
        self.output_layer = [[SimpleNeuron(weights_qty, weight_calculator) for _ in range(neuron_qty)] for _ in
                             range(neuron_qty)]

    def get_neighbours(self, x, y, r):
        result = []

        for i in range(int(x - r), int(x + r) + 1):
            if i < 0 or i >= len(self.output_layer):
                continue

            for j in range(int(y - r), int(y + r) + 1):
                if j < 0 or j >= len(self.output_layer[0]):
                    continue

                distance = ((x - i) ** 2 + (y - j) ** 2) ** 0.5

                if distance <= r:
                    result.append(self.output_layer[i][j])

        return result
