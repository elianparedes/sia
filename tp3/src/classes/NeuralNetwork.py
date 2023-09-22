import numpy as np

from src.classes.multiLayerClasses.HiddenLayer import HiddenLayer
from src.classes.multiLayerClasses.OutputLayer import OutputLayer

LEARNING_RATE = 0.1


class NeuralNetwork:

    def __init__(self, num_layers, output_neurons, hidden_neurons, input_quantity):
        self.num_layers = num_layers
        self.hidden_layers = []

        self.output_layer = OutputLayer(lambda x: x, lambda x: 1, hidden_neurons, output_neurons, LEARNING_RATE)
        self.hidden_layers.append(HiddenLayer(lambda x: x, lambda x: 1, input_quantity, hidden_neurons, LEARNING_RATE))
        for i in range(1, num_layers - 1):
            self.hidden_layers.append(HiddenLayer(lambda x: x, lambda x: 1, hidden_neurons, hidden_neurons, LEARNING_RATE))
        self.hidden_layers.append(self.output_layer)

    def forward_propagation(self, input):
        new_input = input
        for i in range(0, len(self.hidden_layers)):
            new_input = self.hidden_layers[i].activate(new_input)
        return new_input
    def test(self, input):
        new_input = input
        for i in range(0, len(self.hidden_layers)):
            new_input = self.hidden_layers[i].test_activation(new_input)
        return new_input

    def back_propagation(self, expected):
        w = []
        error = self.output_layer.set_deltas(expected)
        w.append(self.output_layer.get_weights())
        for i in range(len(self.hidden_layers) - 2, -1, -1):
            self.hidden_layers[i].set_deltas(self.hidden_layers[i + 1].get_deltas(), self.hidden_layers[i + 1].get_weights())
            w.append(self.hidden_layers[i].get_weights())
        return error, w

