from src.classes.perceptron.PerceptronABC import PerceptronABC


class Linear(PerceptronABC):
    def __init__(self, input, expected, weights, learning_rate) -> None:
        super().__init__(input, expected, weights, learning_rate)

    def activation(self, excitement):
        return excitement

    def error(self):
        error = 0
        for mu in range(0,len(self.input)-1):
            error += (self.expected[mu] - self.activation(self.excitement(mu)))**2
        return error * 0.5

    def update_weights(self, activation, mu):
        diff = (self.learning_rate * (self.expected[mu] - activation)) * self.input[mu]
        self.weights = self.weights + diff
        return self.weights
