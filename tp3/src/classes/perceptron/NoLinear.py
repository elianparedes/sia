from src.classes.perceptron.PerceptronABC import PerceptronABC


class NoLinear(PerceptronABC):

    def __init__(self, input, expected, weights, learning_rate, activation_f, activation_fderivate, beta) -> None:
        super().__init__(input, expected, weights, learning_rate)
        self.activation_f = activation_f
        self.activation_fderivate = activation_fderivate
        self.beta = beta

    def activation(self, excitement):
        return self.activation_f(excitement, self.beta)

    def error(self):
        error = 0
        for mu in range(0, len(self.input) - 1):
            error += (self.expected[mu] - self.activation(self.excitement(mu))) ** 2
        return error * 0.5

    def update_weights(self, activation, mu):
        diff = ((self.learning_rate * (self.expected[mu] - activation)) * self.activation_fderivate(
            self.excitement(mu), self.beta)) * self.input[mu]

        self.weights = self.weights + diff
        return self.weights
