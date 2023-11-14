from abc import ABC

import numpy as np

from src.algorithms.ADAM import ADAM


class LayerABC(ABC):

    def __init__(self, input_qty, neuron_qty, activation_func, activation_derivative, learning_rate, weights=None):
        self.neuron_qty = neuron_qty
        self.input_qty = input_qty
        if weights is None:
            self.weights = np.random.uniform(-1, 1, size=(input_qty, neuron_qty))
        else:
            rows, cols = weights.shape
            if rows != input_qty or cols != neuron_qty:
                print("Weights matrix should have input_qty x neuron_qty size")
                return
            self.weights = weights

        # Activation function values
        self.activation_values = np.array([])
        self.activation_func = activation_func
        self.activation_derivative = activation_derivative
        self.deltas = np.array([])
        self.delta_w = np.zeros((input_qty, neuron_qty))
        self.learning_rate = learning_rate
        self.input = None
        self.h = None
        self.adam = ADAM(0.9, 0.999, 1e-8, 0.001, input_qty, neuron_qty)

    def activate(self, layer_input):
        """Calculates the activation function ``theta``"""
        # Excitement values
        h = np.dot(layer_input, self.weights)
        self.h = h
        # V vector from the previous layer
        self.input = layer_input
        self.activation_values = np.array([])
        for i in range(0, self.neuron_qty):
            self.activation_values = np.append(self.activation_values, self.activation_func(h[i]))
        return self.activation_values

    def test_activation(self, layer_input):
        # Excitement values
        h = np.dot(layer_input, self.weights)

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
        myArray = np.zeros((self.input_qty, self.neuron_qty))
        for i in range(self.input_qty):
            for j in range(self.neuron_qty):
                myArray[i][j] = self.delta_w[i][j] + self.deltas[j] * self.input[i]

        self.delta_w = self.adam.optimize(myArray)

    def update_weights(self):
        self.weights = np.subtract(self.weights, self.delta_w)
        self.delta_w = np.zeros((self.input_qty, self.neuron_qty))
