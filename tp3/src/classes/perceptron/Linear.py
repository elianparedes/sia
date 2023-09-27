from src.classes.optimization.LinearO import LinearO
from src.classes.perceptron.PerceptronABC import PerceptronABC


class Linear(PerceptronABC):
    def __init__(self, weight_qty, learning_rate, weights=None):
        super().__init__(weight_qty, learning_rate, LinearO, weights)

    def activation(self, excitement):
        return excitement

    def error(self, training_set, expected_set):
        error = 0
        for mu in range(0, len(expected_set)-1):
            error += (expected_set[mu] - self.activation(self.excitement(training_set[mu])))**2
        return error * 0.5

    def update_weights(self, diff):
        self.weights = self.weights + diff
        return self.weights

    def compute_deltaw(self, activation_value, training_value, expected_value):
        return self.optimization_method.calculate(expected_value, activation_value, training_value)
