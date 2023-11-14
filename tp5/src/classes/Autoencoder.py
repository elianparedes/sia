import numpy as np

from src.classes.NeuralNetwork import NeuralNetwork


class Autoencoder(NeuralNetwork):

    def __init__(self, latent_space_idx, architecture, hidden_function, hidden_derivative, output_function, output_derivative,
                 learning_rate=0.01, weight_distribution=(-1, 1), weights=None):
        super().__init__(architecture,hidden_function, hidden_derivative, output_function, output_derivative, learning_rate,weight_distribution, weights)
        self.latent_space_index = latent_space_idx

    def get_latent_space_input(self, dataset):
        new_input = dataset
        for i in range(0, self.latent_space_index):
            new_input = self.layers[i].test_activation(new_input)
        return new_input

    def compute_error(self, dataset, expected):
        to_return = 0
        for i in range(0, len(dataset)):
            different_pixels = 0
            result = self.test_forward_propagation(dataset[i])
            for k in range(0, len(result)):
                if result[k] > 0.5:
                    result[k] = 1
                else:
                    result[k] = 0
            err = expected[i]-result
            different_pixels += np.sum(np.abs(err))
            # print(different_pixels)
            if different_pixels > to_return:
                to_return = different_pixels
        return to_return
