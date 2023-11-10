from src.classes.optimization.LinearO import LinearO
from src.classes.perceptron.PerceptronABC import PerceptronABC


class Step(PerceptronABC):

    def __init__(self, weight_qty, learning_rate, weights=None) -> None:
        super().__init__(weight_qty, learning_rate, LinearO, weights)

    def activation(self, excitement):
        return 1 if excitement > 0 else -1

    def error(self, training_set, expected_set):
        wrong = 0
        for i in range(0, len(training_set)):
            if self.activation(self.excitement(training_set[i])) != expected_set[i]:
                wrong += 1
        return wrong / len(training_set)

    def update_weights(self, diff):
        self.weights = self.weights + diff
        return self.weights

    def compute_deltaw(self, activation_value, training_value, expected_value):
        return self.optimization_method.calculate(expected_value, activation_value, training_value)

    def train(self, training_set, expected_set, test_set, test_expected, batch_amount, epoch, epsilon):
        return super().train(training_set, expected_set, test_set, test_expected, batch_amount, epoch, 0)
