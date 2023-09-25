from src.classes.perceptron.PerceptronABC import PerceptronABC


class Step(PerceptronABC):

    def __init__(self, weight_qty, learning_rate, weights=None) -> None:
        super().__init__(weight_qty, learning_rate, weights)

    def activation(self, excitement):
        return 1 if excitement > 0 else -1

    def error(self, training_set, expected_set):
        wrong = 0
        for i in range(0, len(training_set)):
            if self.activation(self.excitement(training_set[i])) != expected_set[i]:
                wrong += 1
        return wrong / len(training_set)

    def update_weights(self, activation_value, training_value, expected_value):
        diff = (self.learning_rate * (expected_value - activation_value)) * training_value
        self.weights = self.weights + diff
        return self.weights

    def train(self, training_set, expected_set, limit, epsilon):
        return super().train(training_set, expected_set, limit, 0)
