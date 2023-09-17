import random
import sys
import numpy as np

from src.classes.perceptron.Linear import Linear

inputs = [
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
]
learning_rate = 0.1
ws = []

expected = [2.0, 3.8, 5.9, 8.1, 10.2]

def normalized_input(input):
    return [[1] + row for row in input]

def initialize_weights():
    w = []
    for i in range(0, 2):
        w.append(random.uniform(-1, 1))
    return w

def linear_perceptor():
    i = 0
    limit = 1000000
    w = initialize_weights()
    perceptron = Linear(normalized_input(inputs), expected, w, learning_rate)
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

#Learns Y = 2X + 0
print(linear_perceptor())