from abc import ABC, abstractmethod
import numpy as np


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
