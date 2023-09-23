from abc import ABC, abstractmethod

import numpy as np


class LayerABC(ABC):

    def __init__(self, activation_func, activation_fderivate, input_qty, neuron_qty, learning_rate):
        self.activation_func = activation_func
        self.neuron_qty = neuron_qty
        self.input_qty = input_qty
        self.weights = np.random.rand(input_qty, neuron_qty)
        # Activation function values
        self.activation = np.array([])
        self.activation_fderivate = activation_fderivate
        self.deltas = np.array([])
        self.learning_rate = learning_rate
        self.input = None
        self.h = None

    def activate(self, input):
        """Calculates the activation function ``theta``"""
        # Excitement values
        h = np.dot(input, self.weights)
        self.h = h
        # V vector from the previous layer
        self.input = input
        self.activation = np.array([])
        for i in range(0, self.neuron_qty):
            self.activation = np.append(self.activation, self.activation_func(h[i]))
        return self.activation

    def test_activation(self, test):
        input = test

        # Excitement values
        h = np.dot(input, self.weights)

        # V vector from the previous layer
        results = np.array([])
        for i in range(0, self.neuron_qty):
            results = np.append(results, self.activation_func(h[i]))
        return results

    def get_deltas(self):
        return self.deltas

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

    def set_delta_w(self):
        for i in range(self.input_qty):
            for j in range(self.neuron_qty):
                self.weights[i][j] = self.weights[i][j] + self.learning_rate * self.deltas[j] * self.input[i]

