import numpy as np

"""File to encapsulate functions"""

BETA = 0.5

SIGMOID = (lambda x: 1 / (1 + np.exp(-2 * BETA * x)))
SIGMOID_DERIVATIVE = (lambda x: 2 * BETA * SIGMOID(x) * (1 - SIGMOID(x)))

TAN_H = (lambda x: np.tanh(BETA * x))
TAN_H_DERIVATIVE = (lambda x: BETA * (1 - np.tanh(BETA * x) ** 2))

RELU = (lambda x: np.log(np.exp(x) + 1))
RELU_DERIVATIVE = (lambda x: np.exp(x) / (np.exp(x) + 1))