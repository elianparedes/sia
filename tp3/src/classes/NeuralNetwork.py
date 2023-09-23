import numpy as np

from src.classes.multiLayerClasses.HiddenLayer import HiddenLayer
from src.classes.multiLayerClasses.OutputLayer import OutputLayer

LEARNING_RATE = 0.01
BETA = 1
LOGISTIC = (lambda x: 1 / (1 + np.exp(-2 * BETA * x)))
LOGISTIC_DERIVATE = (lambda x: 2*BETA * LOGISTIC(x)*(1 - LOGISTIC(x)))
class NeuralNetwork:

    def __init__(self, num_layers, output_neurons, hidden_neurons, input_quantity):
        self.num_layers = num_layers
        self.hidden_layers = []

        self.output_layer = OutputLayer(LOGISTIC, LOGISTIC_DERIVATE, hidden_neurons, output_neurons, LEARNING_RATE)
        self.hidden_layers.append(HiddenLayer(LOGISTIC, LOGISTIC_DERIVATE, input_quantity, hidden_neurons, LEARNING_RATE))
        for i in range(0, num_layers - 1):
            self.hidden_layers.append(HiddenLayer(LOGISTIC, LOGISTIC_DERIVATE, hidden_neurons, hidden_neurons, LEARNING_RATE))
        self.hidden_layers.append(self.output_layer)

    def forward_propagation(self, input):
        new_input = input
        for i in range(0, len(self.hidden_layers)):
            new_input = self.hidden_layers[i].activate(new_input)

        # Returning the results of the output layer
        return new_input

    def test(self, input):
        new_input = input
        for i in range(0, len(self.hidden_layers)):
            new_input = self.hidden_layers[i].test_activation(new_input)
        return new_input

    def testino(self, input, w):
        for i in range(len(self.hidden_layers)):
            self.hidden_layers[i].set_weights(w[i])
        new_input = input
        for i in range(0, len(self.hidden_layers)):
            new_input = self.hidden_layers[i].test_activation(new_input)
        return new_input

    def back_propagation(self, expected):
        self.output_layer.set_deltas(expected)
        for i in range(len(self.hidden_layers) - 2, -1, -1):
            self.hidden_layers[i].set_deltas(self.hidden_layers[i + 1].get_deltas(), self.hidden_layers[i + 1].get_weights())


    def compute_error(self, expected, input):
        error = 0
        for i in range(len(input)):
            output = self.test(input[i])
            for j in range(len(output)):
                error += ((expected[i][j] - output[j]) ** 2) / 2
        return error


    def set_delta_w(self):
        w = []
        for i in range(len(self.hidden_layers)):
            self.hidden_layers[i].set_delta_w()
            w.append(self.hidden_layers[i].get_weights())
        return w

