import os

import pandas as pd
import plotly.express as px

from src.classes.perceptron.Step import Step

CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej2-conjunto.csv")

LEARNING_RATE = 0.1
EPOCHS = 500


def step_error_plot(training_set, training_expected, title):
    # AND function
    perceptron = Step(3, LEARNING_RATE)
    w_min, iterations, previous_weights, previous_errors = perceptron.train(training_set, training_expected, EPOCHS, 0)
    x = [i for i in range(iterations)]
    data = {'Epochs': x, 'Error': previous_errors}
    df = pd.DataFrame(data)
    fig = px.line(df, x="Epochs", y="Error", title=title)
    fig.show()


def and_error_plot():
    # AND function
    training_set = [
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1],
    ]
    training_expected = [-1, -1, -1, 1]
    step_error_plot(training_set, training_expected, 'Error value by Epochs (AND function)')


def xor_error_plot():
    # XOR function (cannot be solved with a simple perceptron)
    training_set = [
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1],
    ]
    training_expected = [1, 1, -1, -1]
    step_error_plot(training_set, training_expected, 'Error value by Epochs (XOR function)')


and_error_plot()
xor_error_plot()
