import os
import numpy as np
import pandas as pd
import plotly.express as px

from src.utils.DatasetUtils import DatasetUtils
from src.classes.perceptron.NonLinear import NonLinear
from src.utils.Function import *

def split_ratio_errors_plot(inputs, expected, bias, learning_rate, batch_amount, epsilon, max_epoch, activation_function, activation_function_derivative, normalize_range):

    inputs = inputs.tolist()

    for i in range(len(inputs)):
        inputs[i].insert(0, bias)

    data = {}
    lines = []
    normalized_data = DatasetUtils.normalize_to_range(expected, normalize_range[0], normalize_range[1])

    for ratio in range(1, 9):
        errors = []
        training_set, training_expected, test_set, test_expected = DatasetUtils.split_dataset(inputs.copy(), normalized_data.tolist(), ratio / 10)

        previous_train_weights = None
        for _ in range(1, max_epoch):
            perceptron = NonLinear(4, learning_rate, activation_function, activation_function_derivative, weights=previous_train_weights)
            w_min, i, _, _, _ = perceptron.train(training_set, training_expected, test_expected=test_expected, test_set=test_set, batch_amount=batch_amount , epoch=1, epsilon=epsilon)

            # test benchmark
            activation_values = perceptron.test(test_set, w_min)
            previous_train_weights = w_min

            test_mse_sum = 0
            for i in range(0, len(activation_values)):
                test_mse_sum += (test_expected[i] - activation_values[i]) ** 2

            test_mse = test_mse_sum / len(activation_values)
            errors.append(test_mse)

        line_label = f'{ratio / 10} Split Ratio'
        lines.append(line_label)
        data[line_label] = errors

    data['Epochs'] = [i for i in range(1, max_epoch)]
    df = pd.DataFrame(data)

    fig = px.line(df, x="Epochs", y=lines, title="Testing Mean Squared Error with Different Split Ratio Comparison", labels={
        'value': 'Mean Squared Error (MSE)'
    } )
    fig.show()
