import os as os
import random
import sys
import time
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.subplots import make_subplots
import numpy as np


from src.classes.NeuralNetwork import NeuralNetwork
from src.utils import Function
from src.utils.DatasetUtils import DatasetUtils
from src.utils.ExerciseUtils import ExerciseUtils

DIGITS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej3-digitos.txt")


def neural_network_test(training_set, training_expected, test_set, test_expected, architecture):
    network = NeuralNetwork(architecture, Function.TAN_H, Function.TAN_H_DERIVATIVE, Function.TAN_H,
                            Function.TAN_H_DERIVATIVE, 0.1, [-1, 1])
    i = 0
    min_error = sys.maxsize
    limit = 500000
    epsilon = 0.01
    w_min = None
    start = time.process_time()

    while min_error > epsilon and i < limit:
        mu = random.randint(0, len(training_set) - 1)
        network.forward_propagation(training_set[mu])
        network.back_propagation(training_expected[mu])
        w = network.set_delta_w()
        network.update_weights()
        error = network.compute_error(training_set, training_expected)
        if error < min_error:
            min_error = error
            w_min = w
        i += 1

    end = time.process_time()
    for k in range(0, len(test_set)):
        print('expected: ', test_expected[k], '-> result: ', network.test_forward_propagation_custom(test_set[k], w_min)
              .round(3))

    print('min_error: ', min_error)
    print('time: ', end - start)
    print('iterations: ', i)
    # print('w_min: ', w_min)
    return w_min


def test_xor():
    dataset = [[0, 1], [1, 0], [0, 0], [1, 1]]
    expected = [[1], [1], [0], [0]]
    architecture = [2, 3, 1]
    neural_network_test(dataset, expected, dataset, expected, architecture)


def test_even():
    dataset = ExerciseUtils.load_ex3_file(DIGITS_PATH)
    expected = [[1], [0], [1], [0], [1], [0], [1], [0], [1], [0]]
    architecture = [35, 1]
    # does not work if we split the dataset. TODO: check different configurations
    # training_set, training_expected, test_set, test_expected = DatasetUtils.split_dataset(dataset, expected, 0.9)
    neural_network_test(dataset, expected, dataset, expected, architecture)


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
    dataset, expected = DatasetUtils.expand_dataset(dataset, expected, 2)
    dataset = DatasetUtils.add_noise(dataset, 0.2)
    training_set, training_expected, test_set, test_expected = DatasetUtils.split_dataset(dataset, expected, 0.8)
    return neural_network_test(training_set, training_expected, test_set, test_expected, architecture)

weights = test_digits()
df = pd.DataFrame(weights[0])
# df[0]

num_matrices = 10
rows = 7
cols = 5

matrix = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(num_matrices)]

for k in range(num_matrices):
    for i in range(rows-1, -1, -1):
        for j in range(cols):
            matrix[k][i][j] = df[k][i * cols + j]

print(matrix[3])

heatmap = go.Heatmap(z=matrix[3], colorscale='Viridis')


# Create a layout for the heatmap
layout = go.Layout(title='Heatmap Example')

# Create a figure and plot it
fig = go.Figure(data=[heatmap], layout=layout)

# Display the heatmap (you can also save it as an HTML file)
pyo.plot(fig, filename='heatmap.html')
