from matplotlib import pyplot as plt
import os
import numpy as np
from src.classes.functions.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE
from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.models.VariationalAutoencoder import VariationalAutoencoder
from src.classes.layers.BiasedDenseLayer import BiasedDenseLayer
from src.classes.optimizers.Adam import Adam
from src.data.fonts import get_characters

from src.utils.IconsUtils import IconsUtils

FILE_PATH = os.path.join(os.pardir, "data", "small_icons.csv")

# network
encoder = NeuralNetwork(
    activation=TAN_H,
    activation_prime=TAN_H_DERIVATIVE,
    optimizer=Adam,
    biased=True,
    architecture=[400, 50, 140, 4],
    learning_rate=0.01
)
decoder = NeuralNetwork(
    activation=TAN_H,
    activation_prime=TAN_H_DERIVATIVE,
    optimizer=Adam,
    biased=True,
    architecture=[2, 50, 140, 400],
    learning_rate=0.01
)

vae = VariationalAutoencoder(encoder=encoder, decoder=decoder)
characters = IconsUtils.load_icons_map_from_file(FILE_PATH)
characters = np.array(list(characters))
test_set = np.array(characters.copy())

vae.train(test_set, epochs=10000)


def plot_latent(vae, n=15, fig_size=15, digit_size=20):
    figure = np.zeros((digit_size * n, digit_size * n))
    grid_x = np.linspace(-1, 1, n)
    grid_y = np.linspace(-1, 1, n)[::-1]
    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z = np.array([[xi, yi]])
            output = vae.predict(z)
            digit = output[0].reshape(digit_size, digit_size)
            figure[
                i * digit_size: (i + 1) * digit_size,
                j * digit_size: (j + 1) * digit_size,
            ] = digit
    plt.figure(figsize=(fig_size, fig_size))
    start_range = digit_size // 2
    end_range = n * digit_size + start_range
    pixel_range = np.arange(start_range, end_range, digit_size)
    sample_range_x = np.round(grid_x, 1)
    sample_range_y = np.round(grid_y, 1)
    plt.xticks(pixel_range, sample_range_x)
    plt.yticks(pixel_range, sample_range_y)
    plt.imshow(figure, cmap="Greys_r")
    plt.show()


plot_latent(vae)
