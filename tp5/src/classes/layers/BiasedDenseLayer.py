import numpy as np
from src.classes.layers.DenseLayer import DenseLayer

class BiasedDenseLayer(DenseLayer):
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, input_size, output_size, optimizer, init_weights_range = [-1, 1]):
        super().__init__(input_size + 1, output_size, optimizer, init_weights_range)

    def forward_propagation_bias(self, input_data):
        input_data = np.insert(input_data, 0, 1, axis=1)
        self.layer_input = input_data
        self.excitement_states = np.dot(self.layer_input, self.weights)
        self.layer_output = self.activation(self.excitement_states)
        return self.layer_output
