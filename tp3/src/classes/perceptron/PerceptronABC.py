import sys
from abc import ABC, abstractmethod
import numpy as np
import random


class PerceptronABC(ABC):

    def __init__(self, weight_qty, learning_rate, weights=None) -> None:
        if weights is None:
            self.weights = np.array(np.random.uniform(-1, 1, size=(1, weight_qty)))
        else:
            self.weights = np.array(weights)
        self.learning_rate = learning_rate

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
        i = 0
        ws = [self.weights]
        min_error = sys.maxsize
        w_min = None
        while min_error > epsilon and i < epoch:
            mu = random.randint(0, len(training_set) - 1)
            training_value = training_set[mu]
            excitement = self.excitement(training_value)
            activation = self.activation(excitement)
            w = self.update_weights(activation, training_value, expected_set[mu])
            ws.append(w)
            error = self.error(training_set, expected_set)
            if error < min_error:
                min_error = error
                w_min = w
            i += 1
        return w_min

    def test(self, test_set, weights):
        """ Calculates outputs from a test_set using custom weights parameter"""
        original_weights = self.weights.copy
        self.weights = weights
        activation_values = []

        for i in range(0, len(test_set)):
            excitement = self.excitement(test_set[i])
            activation_values.append(self.activation(excitement))

        self.weights = original_weights
        return activation_values
