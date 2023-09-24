import numpy as np

from src.classes.layer.LayerABC import LayerABC


class Output(LayerABC):

    def __init__(self, input_qty, neuron_qty, activation_func, activation_derivative, learning_rate, weights=None):
        super().__init__(input_qty, neuron_qty, activation_func, activation_derivative, learning_rate, weights)

    def set_deltas(self, expected):
        """Set ``delta`` for each neuron in a layer"""
        self.deltas = np.array([])
        for i in range(0, self.neuron_qty):
            self.deltas = np.append(self.deltas,
                                    np.subtract(expected[i], self.activation_values[i]) * self.activation_derivative(self.h[i]))

