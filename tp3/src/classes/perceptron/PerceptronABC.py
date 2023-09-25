import sys
from abc import ABC, abstractmethod
import numpy as np
import random


class PerceptronABC(ABC):

    def __init__(self, input, expected, weights, learning_rate) -> None:
        self.input = np.array(input)
        self.expected = expected
        self.weights = np.array(weights)
        self.learning_rate = learning_rate

    def excitement(self, mu):
        return np.dot(self.weights, self.input[mu])

    @abstractmethod
    def activation(self, excitement):
        pass

    @abstractmethod
    def error(self):
        pass

    @abstractmethod
    def update_weights(self, activation, mu):
        pass

    def train(self, limit, epsilon):
        i = 0
        ws = [self.weights]
        min_error = sys.maxsize
        w_min = None
        while min_error > epsilon and i < limit:
            mu = random.randint(0, len(self.input) - 1)
            excitement = self.excitement(mu)
            activation = self.activation(excitement)
            w = self.update_weights(activation, mu)
            ws.append(w)
            error = self.error()
            if error < min_error:
                min_error = error
                w_min = w
            i += 1
        return w_min
