import random
import sys
from abc import ABC, abstractmethod

import numpy as np


class PerceptronABC(ABC):
    """
    **IMPORTANT!** In case of using an ``optimization method`` which takes more than one constant coefficient, it MUST
    be configured from the outside. Eg: MomentumO
    """

    def __init__(self, weight_qty: int, learning_rate: float, optimization_method, weights=None, **kwargs):
        if weights is None:
            self.weights = np.array(np.random.uniform(-1, 1, size=(1, weight_qty)))
        else:
            self.weights = np.array(weights)
        self.optimization_method = optimization_method
        self.optimization_method.configure(learning_rate)

    def excitement(self, training_value):
        return np.dot(self.weights, training_value)

    @abstractmethod
    def activation(self, excitement):
        pass

    @abstractmethod
    def error(self, training_set, expected_set):
        pass

    @abstractmethod
    def update_weights(self, activation_value, training_value, expected_value):
        pass

    def train(self, training_set, expected_set, epoch, epsilon):
        """ Trains the perceptron until error < epsilon or epoch amount is reached"""
        training_set = np.array(training_set)
        previous_weights = np.array(self.weights)
        previous_errors = []
        min_error = sys.maxsize
        w_min = None
        i = 0
        while min_error > epsilon and i < epoch:
            mu = random.randint(0, len(training_set) - 1)
            training_value = training_set[mu]
            excitement = self.excitement(training_value)
            activation = self.activation(excitement)
            w = self.update_weights(activation, training_value, expected_set[mu])
            error = self.error(training_set, expected_set)
            if error < min_error:
                min_error = error
                w_min = w
            i += 1
            previous_weights = np.append(previous_weights, w, axis=0)
            previous_errors.append(error)
        return w_min, i, previous_weights, previous_errors

    def test(self, test_set, weights):
        """ Calculates outputs from a test_set using custom weights parameter"""
        original_weights = self.weights.copy
        self.weights = weights
        activation_values = np.array([])

        for i in range(0, len(test_set)):
            excitement = self.excitement(test_set[i])
            activation_values = np.append(activation_values, self.activation(excitement))

        self.weights = original_weights
        return activation_values
