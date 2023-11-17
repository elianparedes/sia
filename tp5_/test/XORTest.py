import numpy as np

from classes.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE
from classes.LossFunctions import mse_prime, mse
from classes.NeuralNetwork import NeuralNetwork
from classes.layer.Layer import Layer
from classes.optimizers.GradientDescent import GradientDescent

# training data
x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
y_train = np.array([[[0]], [[1]], [[1]], [[0]]])

# optimizer
gradient_descent = GradientDescent()

# network
net = NeuralNetwork()
net.add(Layer(2, 3, SIGMOID, SIGMOID_DERIVATIVE, gradient_descent))
net.add(Layer(3, 1, SIGMOID, SIGMOID_DERIVATIVE, gradient_descent))

# net = NeuralNetwork()
# net.add(Layer(35, 20, SIGMOID, SIGMOID_DERIVATIVE, adam_l1))
# net.add(Layer(20, 10, SIGMOID, SIGMOID_DERIVATIVE, adam_l2))
# net.add(Layer(10, 5, SIGMOID, SIGMOID_DERIVATIVE, adam_l3))
# net.add(Layer(5, 2, SIGMOID, SIGMOID_DERIVATIVE, adam_l4))
# net.add(Layer(2, 5, SIGMOID, SIGMOID_DERIVATIVE, adam_l5))
# net.add(Layer(5, 10, SIGMOID, SIGMOID_DERIVATIVE, adam_l6))
# net.add(Layer(10, 20, SIGMOID, SIGMOID_DERIVATIVE, adam_l7))
# net.add(Layer(20, 35, SIGMOID, SIGMOID_DERIVATIVE, adam_l8))

# train
net.use(mse, mse_prime)
net.fit(x_train, y_train, epochs=1000, learning_rate=0.1)

# test
out = net.predict(x_train)
print(out)