import os
import pandas as pd
import plotly.express as px

from src.utils.DatasetUtils import DatasetUtils
from src.classes.perceptron.NonLinear import NonLinear
from src.utils.Function import *

def test_and_training_errors_plot(inputs, expected, bias, learning_rate, batch_amount, epsilon, max_epoch, activation_function, activation_function_derivative, normalize_range):
    test_errors = []
    training_errors = []

    inputs = inputs.tolist()

    for i in range(len(inputs)):
        inputs[i].insert(0, bias)

    normalized_data = DatasetUtils.normalize_to_range(expected, normalize_range[0], normalize_range[1])
    training_set, training_expected, test_set, test_expected = DatasetUtils.split_dataset(inputs, normalized_data.tolist(), 0.5)

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
        test_errors.append(test_mse)

        # training benchmark
        activation_values = perceptron.test(training_set, w_min)
        training_mse_sum = 0
        for i in range(0, len(activation_values)):
            training_mse_sum += (training_expected[i] - activation_values[i]) ** 2

        training_mse = training_mse_sum / len(activation_values)
        training_errors.append(training_mse)

    test_data = {'Epochs': [i for i in range(1, max_epoch)], 'test_errors': test_errors, 'training_errors': training_errors}
    test_df = pd.DataFrame(test_data)

    fig = px.line(test_df, x="Epochs", y=['test_errors', 'training_errors'], title="Testing and Training Mean Squared Error Comparison", labels={
        'value': "Mean Squared Error (MSE)",
        'test_errors': "Test Error",
        'training_errors': "Training Error"
    })
    fig.show()
