import os as os
import random
import sys
import time
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.offline as pyo

from src.classes.Autoencoder import Autoencoder
from src.data.fonts import get_characters
from src.utils import Function


def autoencoder_test(training_set, training_expected, test_set, test_expected, architecture, latent_space_index):
    encoder = Autoencoder(latent_space_index, architecture, Function.SIGMOID, Function.SIGMOID_DERIVATIVE, Function.SIGMOID,
                            Function.SIGMOID_DERIVATIVE, 0.1, [-1, 1])
    i = 0
    min_error = sys.maxsize

    limit = 50000
    epsilon = 1
    w_min = None
    start = time.process_time()

    while min_error > epsilon and i < limit:
        mu = random.randint(0, len(training_set) - 1)
        encoder.forward_propagation(training_set[mu])
        encoder.back_propagation(training_expected[mu])
        w = encoder.set_delta_w()
        encoder.update_weights()
        error = encoder.compute_error(training_set, training_expected)
        if error < min_error:
            print("Global Error: ", error)
            min_error = error
            w_min = w
        i += 1

    end = time.process_time()
    for k in range(0, len(test_set)):
        print('expected: ', test_expected[k], '-> result: ', encoder.test_forward_propagation_custom(test_set[k], w_min)
               .round(0))
        #print(test_expected - encoder.test_forward_propagation_custom(test_set[k], w_min).round())

    print('min_error: ', min_error)
    print('time: ', end - start)
    print('iterations: ', i)
    print('w_min', w_min)
    return w_min, encoder


training_set = get_characters()
test_set = training_set.copy()
test_expected = test_set.copy()

architecture = [35, 20, 10, 5, 2, 5, 10, 20, 35]

w_min, encoder = autoencoder_test(training_set, training_set, test_set, test_expected, architecture, 2)

