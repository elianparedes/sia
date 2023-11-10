import os
import pandas as pd
import plotly.express as px

from src.classes.NeuralNetwork import NeuralNetwork
from src.utils import Function
from src.utils.DatasetUtils import DatasetUtils
from src.classes.perceptron.NonLinear import NonLinear
from src.utils.Function import *
dataset = [[0, 1], [1, 0], [0, 0], [1, 1]]
expected = [[1], [1], [0], [0]]
learning_rate = 0.1
def test_and_training_errors_plot_xor(inputs, expected, bias, learning_rate, batch_amount, epsilon, max_epoch, activation_function, activation_function_derivative, normalize_range):
    test_errors = []
    training_errors = []
    network = NeuralNetwork([2,2,2,1], Function.TAN_H, Function.TAN_H_DERIVATIVE, Function.TAN_H,
                            Function.TAN_H_DERIVATIVE, learning_rate, [-1, 1])
    previous_train_weights = None

    w_min, curr_epoch, prev_weights, prev_errors = network.train(dataset, expected, test_expected=dataset, test_set=expected, batch_amount=batch_amount , epsilon=epsilon,max_epoch=500)

    test_data = {'Epochs': [i for i in range(0, curr_epoch)], 'test_errors': prev_errors}
    test_df = pd.DataFrame(test_data)

    fig = px.line(test_df, x="Epochs", y=['test_errors'], title="Testing and Training Mean Squared Error Comparison", labels={
        'value': "Mean Squared Error (MSE)",
        'test_errors': "Test Error",
        'training_errors': "Training Error"
    })
    fig.show()
test_and_training_errors_plot_xor(dataset, expected, 1, learning_rate, 1, 0.01, 500, Function.TAN_H, Function.TAN_H_DERIVATIVE, [-1, 1])