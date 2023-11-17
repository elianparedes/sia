import numpy as np

from tp5_.classes.ActivationFunctions import SIGMOID, SIGMOID_DERIVATIVE
from tp5_.classes.LossFunctions import mse_prime, mse
from tp5_.classes.NeuralNetwork import NeuralNetwork
from tp5_.classes.layer.Layer import Layer
from tp5_.classes.optimizers.GradientDescent import GradientDescent

# training data
x_train = np.array([[[0,0]], [[0,1]], [[1,0]], [[1,1]]])
y_train = np.array([[[0]], [[1]], [[1]], [[0]]])

# optimizer
gradient_descent = GradientDescent()

# network
net = NeuralNetwork()
net.add(Layer(2, 3, SIGMOID, SIGMOID_DERIVATIVE, gradient_descent))
net.add(Layer(3, 1, SIGMOID, SIGMOID_DERIVATIVE, gradient_descent))

# train
net.use(mse, mse_prime)
net.fit(x_train, y_train, epochs=1000, learning_rate=0.1)

# test
out = net.predict(x_train)
print(out)