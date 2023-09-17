import sys
from random import random

import numpy as np
import os as os
import pandas as pd
from src.classes.perceptron.Linear import Linear
from src.classes.perceptron.NoLinear import NoLinear

learning_rate = 0.1
ws = []


def initialize_weights():
    w = []
    for i in range(0, 2):
        w.append(random.uniform(-1, 1))
    return w


CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir,
                           "Data/TP3-ej2-conjunto.csv")


def create_dataframe():
    df = pd.read_csv(CONFIG_PATH)
    inputs = df[['x1', 'x2', 'x3']].to_numpy()
    expected = df['y'].to_numpy()

    return inputs, expected

def no_linear_perceptron():
    inputs, expected = create_dataframe()
    i = 0
    limit = 1000000
    w = initialize_weights()
    perceptron = NoLinear(inputs, expected, w, learning_rate, (lambda x, beta: 1 / (1 + np.exp(-2*beta * x))), (lambda x, beta: 0.5* beta * np.log(1+np.exp(-2*beta*x))), 1)
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
            min_error = error
            w_min = w
        i += 1
    return w_min

print(no_linear_perceptron())