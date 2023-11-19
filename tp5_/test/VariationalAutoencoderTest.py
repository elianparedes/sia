import numpy as np
import random
import string

from data.fonts import get_characters
from classes.optimizers.Adam import Adam
from classes.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE
from classes.LossFunctions import mse_prime, mse
from classes.NeuralNetwork import NeuralNetwork
from classes.layer.Layer import Layer
from classes.VariationalAutoencoder import VariationalAutoencoder

# network
encoder = NeuralNetwork()
encoder.add(Layer(35, 28, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(28, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(20, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(10, 5, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(5, 4, TAN_H, TAN_H_DERIVATIVE, Adam()))

decoder = NeuralNetwork()
decoder.add(Layer(2, 5, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(5, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(10, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(20, 28, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(28, 35, TAN_H, TAN_H_DERIVATIVE, Adam()))

vae = VariationalAutoencoder(encoder=encoder, decoder=decoder,latent_space_size=2,last_delta=5)
characters = get_characters()
test_set = np.array(characters.copy())

vae.train(test_set,epochs=500000)