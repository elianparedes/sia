import os as os
import random
import sys
import time

from src.classes.NeuralNetwork import NeuralNetwork
from src.utils import Function
from src.utils.ExerciseUtils import ExerciseUtils

DIGITS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej3-digitos.txt")


def neural_network_test(dataset, expected, architecture):
    network = NeuralNetwork(architecture, Function.TAN_H, Function.TAN_H_DERIVATIVE, Function.TAN_H,
                            Function.TAN_H_DERIVATIVE, 0.1, [-1, 1])
    i = 0
    min_error = sys.maxsize
    limit = 5000
    epsilon = 0.001
    w_min = None
    start = time.process_time()

    while min_error > epsilon and i < limit:
        mu = random.randint(0, len(dataset) - 1)
        network.forward_propagation(dataset[mu])
        network.back_propagation(expected[mu])
        w = network.set_delta_w()
        error = network.compute_error(dataset, expected)
        if error < min_error:
            min_error = error
            w_min = w
        i += 1

    end = time.process_time()
    for k in range(0, len(dataset)):
        print('expected: ', expected[k], '-> result: ', network.test_forward_propagation_custom(dataset[k], w_min)
              .round(3))

    print('min_error: ', min_error)
    print('time: ', end - start)
    print('iterations: ', i)
    return w_min


def test_xor():
    dataset = [[0, 1], [1, 0], [0, 0], [1, 1]]
    expected = [[1], [1], [0], [0]]
    architecture = [2, 3, 1]
    neural_network_test(dataset, expected, architecture)


def test_even():
    dataset = ExerciseUtils.load_ex3_file(DIGITS_PATH)
    expected = [[1], [0], [1], [0], [1], [0], [1], [0], [1], [0]]
    architecture = [35, 1]
    neural_network_test(dataset, expected, architecture)


def test_digits():
    dataset = ExerciseUtils.load_ex3_file(DIGITS_PATH)
    expected = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]
    architecture = [35, 10]
    neural_network_test(dataset, expected, architecture)


test_digits()
