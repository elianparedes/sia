import numpy as np

from classes.ActivationFunctions import TAN_H, TAN_H_DERIVATIVE
from classes.NeuralNetwork import NeuralNetwork
from classes.VariationalAutoencoder import VariationalAutoencoder
from classes.layer.Layer import Layer
from classes.optimizers.Adam import Adam
from data.fonts import get_characters

# network
encoder = NeuralNetwork()
encoder.add(Layer(35, 25, TAN_H, TAN_H_DERIVATIVE, Adam()))
# encoder.add(Layer(28, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
# encoder.add(Layer(20, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(25, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
encoder.add(Layer(10, 4, TAN_H, TAN_H_DERIVATIVE, Adam()))

decoder = NeuralNetwork()
decoder.add(Layer(2, 10, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(10, 25, TAN_H, TAN_H_DERIVATIVE, Adam()))
# decoder.add(Layer(10, 20, TAN_H, TAN_H_DERIVATIVE, Adam()))
# decoder.add(Layer(20, 28, TAN_H, TAN_H_DERIVATIVE, Adam()))
decoder.add(Layer(25, 35, TAN_H, TAN_H_DERIVATIVE, Adam()))

vae = VariationalAutoencoder(encoder=encoder, decoder=decoder,latent_space_size=2,last_delta=5)
characters = get_characters()
test_set = np.array(characters.copy())

vae.train(test_set, epochs=500000)
# print("---------------------")
# print(test_set[1].reshape(7, 5))
# print("---------------------")
# print(vae.predict(test_set)[1].round().astype(int).reshape(7, 5))



