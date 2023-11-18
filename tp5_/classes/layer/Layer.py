import numpy as np

class Layer:
    # input_size = number of input neurons
    # output_size = number of output neurons
    def __init__(self, input_size, output_size, activation, activation_prime, optimizer):
        self.layer_input = None
        self.excitement_states = None
        self.layer_output = None
        self.weights = np.random.uniform(0, 1, size=(input_size, output_size))
        self.activation = activation
        self.activation_prime = activation_prime
        self.optimizer = optimizer

    # Calculates new neuron values (output) from a given input
    def forward_propagation(self, input_data):
        self.layer_input = input_data
        self.excitement_states = np.dot(self.layer_input, self.weights)
        self.layer_output = self.activation(self.excitement_states)
        return self.layer_output

    # output_error: error array from previous layer
    def backward_propagation(self, output_error, learning_rate, epoch):
        output_error = np.multiply(self.activation_prime(self.excitement_states), output_error)  # deltas
        input_error = np.dot(output_error, self.weights.T)  # sum error for next iterations

        weights_error = np.dot(self.layer_input.T, output_error)  # delta w

        # update parameters
        self.weights -= self.optimizer.calculate_delta_w(weights_error, self.layer_input, epoch)

        return input_error