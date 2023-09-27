import random
import sys

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
                                   np.random.uniform(weight_distribution[0], weight_distribution[1],
                                                     size=(output_rows, output_cols)))
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

    def update_weights(self):
        w = []
        for i in range(self.num_layers):
            self.layers[i].update_weights()
            w.append(self.layers[i].weights)
        return w

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

    def get_weights(self):
        w = []
        for i in range(self.num_layers):
            w.append(self.layers[i].get_weights())
        return w

    def train(self, training_set, expected_set, test_set, test_expected, batch_amount, max_epoch, epsilon):

        np_training_set = np.array(training_set)
        np_training_expected = np.array(expected_set)
        min_error = sys.maxsize
        prev_weights = np.array(self.get_weights())
        prev_errors = []
        w_min = None
        curr_epoch = 0
        while min_error > epsilon and curr_epoch < max_epoch:
            np_training_copy = np.array(training_set.copy())

            for _ in range(0, batch_amount):
                mu = random.randint(0, len(np_training_copy)-1)

                np_training_copy = np.delete(np_training_copy, mu, 0)

                self.forward_propagation(np_training_set[mu])
                self.back_propagation(np_training_expected[mu])
                self.set_delta_w()

            w = self.update_weights()
            error = self.compute_error(training_set, expected_set)
            if error < min_error:
                min_error = error
                w_min = w

            curr_epoch += 1
            prev_weights = np.append(prev_weights, w, axis=0)
            prev_errors.append(error)

        # FIXME: delete, only for testing
        for k in range(0, len(test_set)):
            print('expected: ', test_expected[k], '-> result: ',
                  self.test_forward_propagation_custom(test_set[k], w_min)
                  .round(3))

        return w_min, curr_epoch, prev_weights, prev_errors
