import numpy as np

from src.classes.neurons.SimpleNeuron import SimpleNeuron
from src.classes.weights.Random import Random


class Oja:

    def __init__(self, neuron_quantity):
        self.neuron_quantity = neuron_quantity
        self.neurons = SimpleNeuron(neuron_quantity, Random())

    def get_activation(self, input_vector):
        weights = self.neurons.get_weights()
        activation = np.dot(input_vector, weights)
        return activation.tolist()
    def update_weights(self, activation, learning_rate, input_vector):
        input_vector = np.array(input_vector)
        activation = np.array(activation)
        weights = np.array(self.neurons.get_weights())
        delta_weights = learning_rate * (input_vector * activation - (activation ** 2) * weights)
        self.neurons.set_weights(weights + delta_weights)
