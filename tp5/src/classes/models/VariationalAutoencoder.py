import numpy as np

from numpy import ndarray

from src.classes.models.NeuralNetwork import NeuralNetwork


class VariationalAutoencoder:
    def __init__(
        self,
        encoder: NeuralNetwork,
        decoder: NeuralNetwork,
        latent_space_size: int,
        last_delta: int = 0,
    ):
        self.encoder = encoder
        self.decoder = decoder
        self.latent_space_size = latent_space_size
        self.last_delta_size = decoder.layers[0].output_size
        pass

    def train(self, input_data, epochs):
        for epoch in range(epochs):
            result = self.encoder.feed_forward(input_data)

            mean = result[:, : result.shape[1] // 2]
            std = result[:, result.shape[1] // 2 :]

            z, eps = self.reparametrization_trick(mean, std)

            result = self.decoder.feed_forward(z)

            loss = self.loss_function(mean, std, input_data, result)
            print(loss)
            if loss <= 0.01:
                break
            if epoch >= 200000:
                break

            decoder_output_error = input_data - result

            decoder_gradients, last_delta = self.decoder.backpropagation(
                decoder_output_error
            )

            dz_dmean = np.ones([self.last_delta_size, self.latent_space_size])
            dz_dstd = eps * np.ones([self.last_delta_size, self.latent_space_size])

            mean_error = np.dot(last_delta, dz_dmean)
            std_error = np.dot(last_delta, dz_dstd)

            encoder_output_error = np.concatenate((mean_error, std_error), axis=1)
            encoder_reconstruction_gradients, _ = self.encoder.backpropagation(
                encoder_output_error
            )

            dL_dm = mean
            dL_dv = 0.5 * (np.exp(std) - 1)
            encoder_loss_error = np.concatenate((dL_dm, dL_dv), axis=1)
            encoder_loss_gradients, _ = self.encoder.backpropagation(encoder_loss_error)

            # NOTE: update weights with gradients
            encoder_gradients = []
            for g1, g2 in zip(encoder_loss_gradients, encoder_reconstruction_gradients):
                encoder_gradients.append(g1 + g2)

            self.encoder.update_weights(encoder_gradients, epoch)
            self.decoder.update_weights(decoder_gradients, epoch)

    def predict(self, input_data):
        result = self.decoder.feed_forward(input_data)
        return result

    def reparametrization_trick(
        self, mean: ndarray[float], std: ndarray[float]
    ) -> tuple[ndarray[float], float]:
        eps = np.random.standard_normal()
        return eps * std + mean, eps

    def loss_function(self, mean, std, data, result):
        rec = 0.5 * np.mean((data - result) ** 2)
        kl = -0.5 * np.sum(1 + std - mean**2 - np.exp(std))

        return rec + kl
