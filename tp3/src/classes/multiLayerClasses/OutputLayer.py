import numpy as np

from src.classes.multiLayerClasses.LayerABC import LayerABC


class OutputLayer(LayerABC):

    def __init__(self, activation_func, activation_fderivate, input_qty, neuron_qty, learning_rate):
        super().__init__(activation_func, activation_fderivate, input_qty, neuron_qty, learning_rate)

    def set_deltas(self, expected):
        """Set ``delta`` for each neuron in a layer"""
        self.deltas = np.array([])
        for i in range(0, self.neuron_qty):
            self.deltas = np.append(self.deltas,
                                    np.subtract(expected[i], self.results[i]) * self.activation_fderivate(self.results[i]))

        super().set_delta_w()
        return np.sum(np.subtract(expected, self.results)** 2) / 2