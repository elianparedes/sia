import numpy as np

from src.classes.functions.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE
from src.classes.functions.LossFunctions import mse_prime, mse
from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.layers.DenseLayer import DenseLayer
from src.classes.optimizers.GradientDescent import GradientDescent

# training data
x_train = np.array([[[[0, 0]], [[0, 1]], [[1, 0]], [[1, 1]]]])
y_train = np.array([[[[0]], [[1]], [[1]], [[0]]]])

# network
net = NeuralNetwork()
net.add(DenseLayer(2, 3, SIGMOID, SIGMOID_DERIVATIVE, GradientDescent()))
net.add(DenseLayer(3, 3, SIGMOID, SIGMOID_DERIVATIVE, GradientDescent()))
net.add(DenseLayer(3, 1, SIGMOID, SIGMOID_DERIVATIVE, GradientDescent()))

# train
net.use(mse, mse_prime)
net.fit(x_train, y_train, 1000, x_train, y_train)

# test
out = net.predict(x_train)
print(out)
