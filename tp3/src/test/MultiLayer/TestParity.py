import random
import sys
import time

import numpy as np
import os as os
import pandas as pd
from src.classes.NeuralNetwork import NeuralNetwork



values = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
expected = [[1], [1], [0], [0]]
learning_rate = 0.01

def TestParity():
    inputs = values
    network = NeuralNetwork(3, 1, 5, 2)
    i = 0
    min_error = sys.maxsize
    limit = 1000000
    epsilon = 0.01
    w_min = None
    start = time.process_time()
    while min_error > epsilon and i < limit:
        mu = random.randint(0, len(inputs) - 1)
        network.forward_propagation(inputs[mu])
        network.back_propagation(expected[mu])
        w = network.set_delta_w()
        error = network.compute_error(expected, inputs)
        if error < min_error:
            min_error = error
            w_min = w
        i += 1
    end = time.process_time()
    print(network.testino([-1, -1], w_min))
    print(network.testino([-1, 1], w_min))
    print(network.testino([1, -1], w_min))
    print(network.testino([1, 1], w_min))
    print(min_error)
    print(end - start)
    return w_min


NeuralNetworkTest()
