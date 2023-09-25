from src.classes.perceptron.PerceptronABC import PerceptronABC


class NoLinear(PerceptronABC):

    def __init__(self, weights_qty, learning_rate, activation_f, activation_derivative, weights=None) -> None:
        super().__init__(weights_qty, learning_rate, weights)
        self.activation_f = activation_f
        self.activation_derivative = activation_derivative

    def activation(self, excitement):
        return self.activation_f(excitement)

    def error(self, training_set, expected_set):
        error = 0
        for mu in range(0, len(training_set) - 1):
            error += (expected_set[mu] - self.activation(self.excitement(training_set[mu]))) ** 2
        return error * 0.5

    def update_weights(self, activation_value, training_value, expected_value):
        diff = ((self.learning_rate * (expected_value - activation_value))
                * self.activation_derivative(self.excitement(training_value))) * training_value

        self.weights = self.weights + diff
        return self.weights
