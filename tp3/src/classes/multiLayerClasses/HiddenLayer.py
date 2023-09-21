import numpy as np

from src.classes.multiLayerClasses.LayerABC import LayerABC


class HiddenLayer(LayerABC):

    def __init__(self, activation_func, activation_fderivate, input_qty, neuron_qty, learning_rate):
        super().__init__(activation_func, activation_fderivate, input_qty, neuron_qty, learning_rate)

    def output(self):
        return self.results

    def set_deltas(self, upper_deltas, upper_weights):
        """Set ``delta`` for each neuron in a layer"""
        self.deltas = np.array([])
        for i in range(0, self.neuron_qty):
            self.deltas = np.append(self.deltas, self.activation_fderivate(self.results[i]) * np.dot(upper_deltas, upper_weights[i]))
        self.set_delta_w()
