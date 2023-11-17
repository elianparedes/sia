import numpy as np

from data.fonts import get_characters
from classes.optimizers.Adam import Adam
from classes.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE
from classes.LossFunctions import mse_prime, mse
from classes.NeuralNetwork import NeuralNetwork
from classes.layer.Layer import Layer

# Assuming you have defined the get_characters function

def replace_zeros_with_minus_one(array):
    return np.where(array == 0, -1, array)

# optimizer
# adam = Adam()

# network
net = NeuralNetwork()
net.add(Layer(35, 20, SIGMOID, SIGMOID_DERIVATIVE, Adam()))
net.add(Layer(20, 10, SIGMOID, SIGMOID_DERIVATIVE, Adam()))
net.add(Layer(10, 5, SIGMOID, SIGMOID_DERIVATIVE, Adam()))
net.add(Layer(5, 2, SIGMOID, SIGMOID_DERIVATIVE, Adam()))
net.add(Layer(2, 5, SIGMOID, SIGMOID_DERIVATIVE, Adam()))
net.add(Layer(5, 10, SIGMOID, SIGMOID_DERIVATIVE, Adam()))
net.add(Layer(10, 20, SIGMOID, SIGMOID_DERIVATIVE, Adam()))
net.add(Layer(20, 35, SIGMOID, SIGMOID_DERIVATIVE, Adam()))

# bring fonts
training_set = np.array([get_characters()])

test_set = training_set.copy()

# train
net.use(mse, mse_prime)
net.fit(training_set, test_set, epochs=1000000000, learning_rate=0.01)

# test
out = net.predict(training_set)