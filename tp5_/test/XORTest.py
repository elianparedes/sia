import numpy as np

from classes.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE
from classes.LossFunctions import mse_prime, mse
from classes.NeuralNetwork import NeuralNetwork
from classes.layer.Layer import Layer
from classes.optimizers.GradientDescent import GradientDescent

# training data
x_train = np.array([[[[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]]]])
y_train = np.array([[[[0]], [[1]], [[1]], [[0]]]])

# network
net = NeuralNetwork()
net.add(Layer(2, 3, SIGMOID, SIGMOID_DERIVATIVE, GradientDescent()))
net.add(Layer(3, 3, SIGMOID, SIGMOID_DERIVATIVE, GradientDescent()))
net.add(Layer(3, 1, SIGMOID, SIGMOID_DERIVATIVE, GradientDescent()))

# train
net.use(mse, mse_prime)
net.fit(x_train, y_train, 1000, 0.1, x_train, y_train)

# test
out = net.predict(x_train)
print(out)
