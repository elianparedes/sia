import numpy as np

from src.classes.layer.LayerABC import LayerABC


class Hidden(LayerABC):

    def __init__(self, input_qty, neuron_qty, activation_func, activation_derivative, learning_rate, weights=None):
        super().__init__(input_qty, neuron_qty, activation_func, activation_derivative, learning_rate, weights)

    def get_activation_values(self):
        return self.activation_values

    def set_deltas(self, upper_deltas, upper_weights):
        """Set ``delta`` for each neuron in a layer"""

        self.deltas = np.array([])
        for i in range(0, self.neuron_qty):
            #TODO check if this is correct
            self.deltas = np.append(self.deltas, self.activation_derivative(self.h[i]) * np.dot(upper_deltas, upper_weights[i]))
