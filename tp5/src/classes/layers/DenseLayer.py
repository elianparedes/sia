import numpy as np
from src.classes.layers.LayerABC import LayerABC

class DenseLayer(LayerABC):
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, input_size, output_size, optimizer, init_weights_range: tuple[int, int] = [-1, 1]):
        self.layer_input = None
        self.excitement_states = None
        self.layer_output = None
        self.activation = None
        self.activation_prime = None

        self.optimizer = optimizer
        self.output_size = output_size
        self.input_size = input_size

        self.weights = np.random.uniform(low=init_weights_range[0], high=init_weights_range[1], size=(input_size, output_size))

    # Calculates new neuron values (output) from a given input
    def forward_propagation(self, input_data):
        self.layer_input = input_data
        self.excitement_states = np.dot(self.layer_input, self.weights)
        self.layer_output = self.activation(self.excitement_states)
        return self.layer_output

    # output_error: error array from previous layer
    def backward_propagation(self, output_error, epoch):
        output_error = np.multiply(self.activation_prime(self.excitement_states), output_error)  # deltas
        input_error = np.dot(output_error,self.weights.T)  # sum error for next iterations

        weights_error = np.dot(self.layer_input.T, output_error)  # delta w

        # update parameters
        self.weights += self.optimizer.calculate_delta_w(weights_error, self.layer_input, epoch)

        return input_error
    
    # wip auxiliar function that does not store calculated weights in the layer
    def _backward_propagation(self, output_error):
        output_error = np.multiply(self.activation_prime(self.excitement_states), output_error)  # deltas
        input_error = np.dot(output_error,  np.delete(self.weights, 0, axis=0).T)  # sum error for next iterations

        weights_error = -np.dot(self.layer_input.T, output_error)  # delta w

        return input_error, weights_error, output_error
    
    def set_weights(self, weights_error, epoch):
        self.weights += self.optimizer.calculate_delta_w(weights_error, self.layer_input, epoch)
    