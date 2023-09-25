from src.classes.perceptron.PerceptronABC import PerceptronABC


class Linear(PerceptronABC):
    def __init__(self, weight_qty, learning_rate, weights=None) -> None:
        super().__init__(weight_qty, learning_rate, weights)

    def activation(self, excitement):
        return excitement

    def error(self, training_set, expected_set):
        error = 0
        for mu in range(0, len(expected_set)-1):
            error += (expected_set[mu] - self.activation(self.excitement(training_set[mu])))**2
        return error * 0.5

    def update_weights(self, activation_value, training_value, expected_value):
        diff = (self.learning_rate * (expected_value - activation_value)) * training_value
        self.weights = self.weights + diff
        return self.weights
