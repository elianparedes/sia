import os.path

import numpy as np

from src.Config import Config
from src.benchmarks.dataframe.vae_latent_space_df import vae_latent_space_df
from src.benchmarks.plot.vae_latent_space_plot import vae_latent_space_plot
from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.models.VariationalAutoencoder import VariationalAutoencoder
from src.classes.optimizers.Adam import Adam
from src.data.fonts import get_characters
from src.classes.utils.TrainingUtils import TrainingUtils


def vae_latent_space_setup(config: Config):
    config_vae = config.vae
    config_enc = config_vae['encoder']
    config_dec = config_vae['decoder']

    encoder = NeuralNetwork(
        activation=config_enc['activation'],
        activation_prime=config_enc['activation_prime'],
        optimizer=Adam,
        biased=True,
        architecture=config_enc['layers'],
        learning_rate=config_vae['learning_rate']
    )
    decoder = NeuralNetwork(
        activation=config_dec['activation'],
        activation_prime=config_dec['activation_prime'],
        optimizer=Adam,
        biased=True,
        architecture=config_dec['layers'],
        learning_rate=config_vae['learning_rate']
    )

    vae = VariationalAutoencoder(encoder=encoder, decoder=decoder)
    characters = get_characters()
    test_set = np.array(characters.copy())

    vae.train(test_set, epochs=config_vae['epochs'])
    sampled_latent = TrainingUtils.encoder_train(encoder, test_set, 1000)
    latent_df = vae_latent_space_df(sampled_latent)
    vae_latent_space_plot(latent_df)
