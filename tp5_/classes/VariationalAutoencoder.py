
import numpy as np

from numbers import Number
from classes.NeuralNetwork import NeuralNetwork
from classes.LossFunctions import mse_prime

class VariationalAutoencoder:
    def __init__(self, encoder: NeuralNetwork, decoder: NeuralNetwork):
        self.encoder = encoder
        self.decoder = decoder
        pass

    def train(self, input_data, epochs):
        for epoch in range(epochs):
            result = self.encoder.feed_forward(input_data)

            mean = result[:, :result.shape[1] // 2]
            std = result[:, result.shape[1] // 2:]

            z, eps = self.reparametrization_trick(mean, std)

            result = self.decoder.feed_forward(z)

            loss = self.loss_function(mean, std, input_data, result)

            decoder_output_error = mse_prime(input_data, result)
            input_errors, weights_errors = self.decoder.backward_propagation(decoder_output_error)

            # TODO: Propagate the error backwards from the decoder's input

    def reparametrization_trick(self, mean, std) -> tuple[Number, Number]:
        epsilon = np.random.standard_normal()
        return epsilon * std + mean, epsilon
    
    def loss_function(self, mean, std, input_data, result):
        return 0.5 * np.mean((input_data - result) ** 2) -0.5 * np.sum(1 + std - mean ** 2 - np.exp(std))

    








        