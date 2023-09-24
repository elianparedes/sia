import numpy as np

from src.classes.layer.Hidden import Hidden
from src.classes.layer.Output import Output


class NeuralNetwork:

    def __init__(self, architecture, hidden_function, hidden_derivative, output_function, output_derivative,
                 learning_rate=0.1, weight_distribution=(-1, 1)):
        # hidden layers + output layer
        self.num_layers = len(architecture) - 1
        self.layers = []

        for i in range(0, len(architecture) - 2):
            rows = architecture[i]
            cols = architecture[i + 1]
            self.layers.append(
                Hidden(rows, cols, hidden_function, hidden_derivative, learning_rate,
                       np.random.uniform(weight_distribution[0], weight_distribution[1], size=(rows, cols))))

        output_rows = architecture[len(architecture) - 2]
        output_cols = architecture[len(architecture) - 1]
        self.output_layer = Output(output_rows,
                                   output_cols, output_function, output_derivative, learning_rate,
                                   np.random.uniform(weight_distribution[0], weight_distribution[1], size=(output_rows, output_cols)))
        self.layers.append(self.output_layer)

    def forward_propagation(self, dataset):
        new_input = dataset
        for i in range(0, self.num_layers):
            new_input = self.layers[i].activate(new_input)

        # Returning the results of the output layer
        return new_input

    def test_forward_propagation(self, dataset):
        new_input = dataset
        for i in range(0, self.num_layers):
            new_input = self.layers[i].test_activation(new_input)
        return new_input

    def test_forward_propagation_custom(self, dataset, w):
        for i in range(len(self.layers)):
            self.layers[i].set_weights(w[i])
        new_input = dataset
        for i in range(0, len(self.layers)):
            new_input = self.layers[i].test_activation(new_input)
        return new_input

    def back_propagation(self, expected):
        self.output_layer.set_deltas(expected)
        for i in range(self.num_layers - 2, -1, -1):
            self.layers[i].set_deltas(self.layers[i + 1].get_deltas(),
                                      self.layers[i + 1].get_weights())

    def compute_error(self, dataset, expected):
        error = 0
        for i in range(len(dataset)):
            output = self.test_forward_propagation(dataset[i])
            for j in range(len(output)):
                error += ((expected[i][j] - output[j]) ** 2) / 2
        return error

    def set_delta_w(self):
        w = []
        for i in range(self.num_layers):
            self.layers[i].set_delta_w()
            w.append(self.layers[i].get_weights())
        return w
