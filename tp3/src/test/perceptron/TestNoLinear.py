import os as os
import random
import sys

import numpy as np

from src.classes.perceptron.NoLinear import NoLinear
from src.utils.ExerciseUtils import ExerciseUtils

learning_rate = 0.1
ws = []


def initialize_weights():
    w = []
    for i in range(0, 3):
        w.append(random.uniform(-1, 1))
    return w


CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej2-conjunto.csv")


def normalized_input(input):
    numpy_array = np.array(input)
    max = np.max(numpy_array)
    min = np.min(numpy_array)
    for i in range(0, len(input)):
        input[i] = (input[i] - min) / (max - min)
    return input


def no_linear_perceptron():
    inputs, expected = ExerciseUtils.load_ex2_file(CONFIG_PATH)
    expected = normalized_input(expected)
    i = 0
    limit = 100000
    w = initialize_weights()
    perceptron = NoLinear(inputs, expected, w, learning_rate, (lambda x, beta: 1 / (1 + np.exp(-2 * beta * x))),
                          (lambda x, beta: 0.5 * beta * np.log(1 + np.exp(-2 * beta * x))), 0.000001)
    ws.append(w)
    min_error = sys.maxsize
    w_min = None
    while min_error > 0 and i < limit:
        mu = random.randint(0, len(inputs) - 1)
        excitement = perceptron.excitement(mu)
        activation = perceptron.activation(excitement)
        w = perceptron.update_weights(activation, mu)
        ws.append(w)
        error = perceptron.error()
        if error < min_error:
            print(min_error)
            min_error = error
            w_min = w
        i += 1
    return w_min


print(no_linear_perceptron())
