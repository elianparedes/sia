from src.classes.perceptron.PerceptronABC import PerceptronABC


class Step(PerceptronABC):

    def __init__(self, input, expected, weights, learning_rate) -> None:
        super().__init__(input, expected, weights, learning_rate)

    def activation(self, excitement):
        return 1 if excitement > 0 else -1

    def error(self):
        wrong = 0
        for i in range(0, len(self.input)):
            if self.activation(self.excitement(i)) != self.expected[i]:
                wrong += 1
        return wrong / len(self.input)

    def update_weights(self, activation, mu):
        diff = (self.learning_rate * (self.expected[mu] - activation)) * self.input[mu]
        self.weights = self.weights + diff
        return self.weights
