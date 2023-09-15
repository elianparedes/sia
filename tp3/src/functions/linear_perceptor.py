import random
import sys
import numpy as np

values = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
expected = [-1, -1, -1, 1]
learning_rate = 0.1
ws = []


def linear_perceptor():
    i = 0
    limit = 1000000
    w = initialize_weights()
    ws.append(w)
    min_error = sys.maxsize
    w_min = None
    while min_error > 0 and i < limit:
        mu = random.randint(0, len(values) - 1)
        excitement = compute_excitement(w, values[mu])
        activation = compute_activation(excitement)
        deltas = np.dot([1] + values[mu], learning_rate * (expected[mu] - activation))
        w = np.add(w, deltas)
        ws.append(w)
        error = compute_error(w)
        if error < min_error:
            min_error = error
            w_min = w
        i += 1
    return w_min


# Scalar product
def compute_excitement(w, x):
    return w[0] + w[1] * x[0] + w[2] * x[1]


# Activation function
def compute_activation(excitement):
    return 1 if excitement > 0 else -1


# Simulation
def compute_error(w):
    wrong = 0
    for i in range(0, len(values)):
        if compute_activation(compute_excitement(w, values[i])) != expected[i]:
            wrong += 1
    return wrong / len(values)


# Random weights
def initialize_weights():
    w = []
    for i in range(0, 3):
        w.append(random.uniform(-1, 1))
    return w


print(linear_perceptor())





