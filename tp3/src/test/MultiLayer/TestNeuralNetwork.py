import random
import sys
import numpy as np
import os as os
import pandas as pd
from src.classes.NeuralNetwork import NeuralNetwork


DIGITS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir,
                           "Data/TP3-ej3-digitos.txt")

def get_digits_dataframe():
    df = pd.read_csv(DIGITS_PATH, delimiter='\t')
    numbers = [[]]
    for i in range(0, 9):
        start = i*7
        numbers[i] = df[start: start + 7].to_numpy()

values = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
expected = [[1 , 0], [1 , 0], [0 , 1], [0 , 1]]
learning_rate = 0.1

def NeuralNetworkTest():
    inputs = values
    network = NeuralNetwork(2, 2, 3,2)
    i = 0
    min_error = sys.maxsize
    error = None
    limit = 10000
    epsilon = 0.01
    w_min = None
    while min_error > epsilon and i < limit:
        mu = random.randint(0, len(inputs) - 1 )
        network.forward_propagation(inputs[mu])
        error, w = network.back_propagation(expected[mu])
        if error < min_error:
            min_error = error
            w_min = w
        i += 1
    print(network.test([-1, -1]))
    print(network.test([-1, 1]))
    print(network.test([1, -1]))
    print(network.test([1, 1]))
    return w_min
NeuralNetworkTest()
