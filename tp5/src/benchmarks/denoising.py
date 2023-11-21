import os

import numpy as np
import pandas as pd

from src.Config import Config
from src.benchmarks.plot.dae_chars_denoise_plot import denoising_plot
from src.classes.functions.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE
from src.classes.functions.LossFunctions import mse, mse_prime
from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.functions.NoiseFunctions import gaussian_noise
from src.classes.layers.DenseLayer import DenseLayer
from src.classes.optimizers.Adam import Adam
from src.data import get_characters
from src.classes.functions.NoiseFunctions import gaussian_noise, salt_and_pepper
def denoising(config:Config):

    config_denoising = config.denoising

    epochs = config_denoising['epochs']
    learning_rate = config_denoising['learning_rate']
    noise_function = config_denoising['noise_function']
    noise_function_params = config_denoising['noise_function_params']

    # Setup nn
    net = NeuralNetwork(activation=config_denoising['activation'], activation_prime=config_denoising['activation_prime'], optimizer=Adam,
                        architecture=config_denoising['layers'], learning_rate=learning_rate)

    characters = get_characters()

    if noise_function == gaussian_noise:
        mean = noise_function_params['mean']
        std_deviation = noise_function_params['std_deviation']
        noisy_characters = gaussian_noise(characters,mean,std_deviation)
    elif noise_function == salt_and_pepper:
        radio = noise_function_params['radio']
        noisy_characters = salt_and_pepper(characters,radio)
    else:
        raise Exception(f'Unknown noise function {noise_function}')


    noisy_training_set = []
    for character in noisy_characters:
        noisy_training_set.append(character)

    training_expected = []
    for character in characters:
        training_expected.append(character)

    noisy_training_set = np.array([noisy_training_set])

    if noise_function == gaussian_noise:
        mean = noise_function_params['mean']
        std_deviation = noise_function_params['std_deviation']
        test_set = np.array(gaussian_noise(characters.copy(), mean, std_deviation))
    elif noise_function == salt_and_pepper:
        radio = noise_function_params['radio']
        test_set = np.array(salt_and_pepper(characters.copy(),radio))
    else:
        raise Exception(f'Unknown noise function {noise_function}')

    test_expected = np.array(characters.copy())


    print(np.shape(noisy_training_set))
    print(np.shape(training_expected))
    print('--------------')
    print(np.shape(test_set))
    print(np.shape(test_expected))


    # Train nn
    net.use(mse, mse_prime)
    net.fit(training_set=noisy_training_set, test_set=test_set,
            epochs=epochs, training_expected=[training_expected], test_expected=test_expected)

    # Plot
    denoising_plot(net, characters, noisy_characters)