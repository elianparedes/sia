import random

import numpy as np

from src.classes.models.NeuralNetwork import NeuralNetwork

class TrainingUtils:

    @staticmethod
    def encoder_train(encoder: NeuralNetwork, input_data, epochs):
        sampled_latent_points = []
        for epoch in range(epochs):
            result = encoder.feed_forward(input_data)

            mean = result[:, : result.shape[1] // 2]
            std = result[:, result.shape[1] // 2:]

            eps = np.random.standard_normal()
            z = eps * std + mean
            sampled_latent_points.append(z)

        return sampled_latent_points

    @staticmethod
    def generate_batches(characters, batch_size):
        batch_size = max(batch_size, 1)

        num_complete_batches, remainder = divmod(len(characters), batch_size)

        random.shuffle(characters)

        batches = [characters[i * batch_size:(i + 1) * batch_size] for i in range(num_complete_batches)]

        if remainder:
            last_batch = characters[num_complete_batches * batch_size:]
            random_fill = random.sample(characters, batch_size - remainder)
            last_batch.extend(random_fill)
            batches.append(last_batch)

        return batches


