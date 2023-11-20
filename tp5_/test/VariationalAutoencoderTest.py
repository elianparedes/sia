import numpy as np
import random
import string

from matplotlib import pyplot as plt

from data.fonts import get_characters
from classes.optimizers.Adam import Adam
from classes.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE, RELU, RELU_DERIVATIVE
from classes.LossFunctions import mse_prime, mse
from classes.NeuralNetwork import NeuralNetwork
from classes.layer.Layer import Layer
from classes.VariationalAutoencoder import VariationalAutoencoder

# network
encoder = NeuralNetwork()
encoder.add(Layer(49+1, 25, TAN_H, TAN_H_DERIVATIVE, Adam()))
# encoder.add(Layer(28, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
# encoder.add(Layer(20, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(25+1, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(10+1, 4, TAN_H, TAN_H_DERIVATIVE, Adam()))

decoder = NeuralNetwork()
decoder.add(Layer(2+1, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(10+1, 25, TAN_H, TAN_H_DERIVATIVE, Adam()))
# decoder.add(Layer(10, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
# decoder.add(Layer(20, 28, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(25+1, 49, TAN_H, TAN_H_DERIVATIVE, Adam()))

vae = VariationalAutoencoder(encoder=encoder, decoder=decoder,latent_space_size=2,last_delta=10)
characters = get_characters()
test_set = np.array(characters.copy())

vae.train(test_set, epochs=10000)

def plot_latent(vae, n=20, fig_size=15, digit_size=7):
    figure = np.zeros((digit_size * n, digit_size * n))
    grid_x = np.linspace(-1.0, 1.0, n)
    grid_y = np.linspace(-1.0, 1.0, n)[::-1]
    for i, yi in enumerate(grid_y):
        for j, xi in enumerate(grid_x):
            z = np.array([[xi, yi]])
            output = vae.predict(z)
            digit = output[0].reshape(digit_size, digit_size)
            figure[i * digit_size: (i + 1) * digit_size, j * digit_size: (j + 1) * digit_size] = digit
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

# def plot_latent(vae, n=20, fig_size=15, digit_size=7):
#     figure = np.zeros((digit_size * n, 5 * n))
#     grid_x = np.linspace(-1, 1.0, n)
#     grid_y = np.linspace(-1, 1.0, n)[::-1]
#     for i, yi in enumerate(grid_y):
#         for j, xi in enumerate(grid_x):
#             z = np.array([[xi, yi]])
#             output = vae.predict(z)
#             digit = output[0].reshape(digit_size, 5)
#             figure[i * digit_size: (i + 1) * digit_size, j * 5: (j + 1) * 5] = digit
#     plt.figure(figsize=(fig_size, fig_size))
#     start_range = digit_size // 2
#     end_range = n * digit_size + start_range
#     pixel_range = np.arange(start_range, end_range, digit_size)
#     sample_range_x = np.round(grid_x, 1)
#     sample_range_y = np.round(grid_y, 1)
#     plt.xticks(pixel_range, sample_range_x)
#     plt.yticks(pixel_range, sample_range_y)
#     plt.imshow(figure, cmap="Greys_r")
#     plt.show()

plot_latent(vae)



