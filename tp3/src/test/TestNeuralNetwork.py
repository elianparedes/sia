import os as os
import random
import sys
import time

import numpy as np
from src.classes.NeuralNetwork import NeuralNetwork

DIGITS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej3-digitos.txt")

values = [[0, 1], [1, 0], [0, 0], [1, 1]]
expected = [[1], [1], [0], [0]]

BETA = 1
LOGISTIC = (lambda x: 1 / (1 + np.exp(-2 * BETA * x)))
LOGISTIC_DERIVATIVE = (lambda x: 2 * BETA * LOGISTIC(x) * (1 - LOGISTIC(x)))
TAN_H = (lambda x: np.tanh(x))
TAN_H_DERIVATIVE = (lambda x: 1 - np.tanh(x) ** 2)


def neural_network_test():
    inputs = values
    network = NeuralNetwork([2, 3, 1], TAN_H, TAN_H_DERIVATIVE, TAN_H, TAN_H_DERIVATIVE, 0.1, [-1, 1])
    i = 0
    min_error = sys.maxsize
    limit = 5000
    epsilon = 0.01
    w_min = None
    start = time.process_time()
    while min_error > epsilon and i < limit:
        mu = random.randint(0, len(inputs) - 1)
        network.forward_propagation(inputs[mu])
        network.back_propagation(expected[mu])
        w = network.set_delta_w()
        error = network.compute_error(inputs, expected)
        if error < min_error:
            min_error = error
            w_min = w
        i += 1
    end = time.process_time()
    print(network.test_forward_propagation_custom([0, 0], w_min))
    print(network.test_forward_propagation_custom([0, 1], w_min))
    print(network.test_forward_propagation_custom([1, 0], w_min))
    print(network.test_forward_propagation_custom([1, 1], w_min))
    print(min_error)
    print(end - start)
    print(i)
    return w_min


neural_network_test()
