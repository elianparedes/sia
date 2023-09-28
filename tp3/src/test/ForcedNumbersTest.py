import os as os
import csv
import numpy as np
import random
import sys
import time
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

from src.classes.NeuralNetwork import NeuralNetwork
from src.utils import Function
from src.utils.DatasetUtils import DatasetUtils
from src.utils.ExerciseUtils import ExerciseUtils

DIGITS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej3-digitos.txt")

DIGITS_TEST_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir,
                                "Data", "TP3-ej3-digitos-prueba.txt")

def neural_network_test(test_set, test_expected, network):

    for k in range(0, len(test_set)):
        print('expected: ', test_expected[k], '-> result: ', network.test_forward_propagation_custom(test_set[k], network.get_weights()).round(3))


# Initialize an empty matrix its gonna be a 35x10 matrix
matrix = []

# Specify the path to your CSV file
csv_file_path = 'weights.csv'

# Read the CSV file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Iterate through each row in the CSV
    for row in csv_reader:
        # Ensure each row has exactly 10 values
        if len(row) == 10:
            row = [float(value) for value in row]
            matrix.append(row)

matrix = np.array(matrix)

# print(matrix)

#Create a neural network with the weights from the csv
network = NeuralNetwork([35, 10], Function.TAN_H, Function.TAN_H_DERIVATIVE, Function.TAN_H,
                        Function.TAN_H_DERIVATIVE, 0.1, [-1, 1], matrix)


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

neural_network_test(dataset, expected, network)
# network.test_forward_propagation(dataset)
