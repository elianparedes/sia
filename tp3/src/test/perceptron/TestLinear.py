import numpy as np

from src.classes.perceptron.Linear import Linear


def linear_perceptron_test():
    """ Learns Y= 2X + 0"""
    training_set = [
        [1, 1.0],
        [1, 2.0],
        [1, 3.0],
        [1, 4.0],
        [1, 5.0]
    ]
    learning_rate = 0.01
    training_expected = [2.0, 4.0, 6.0, 8.0, 10.0]
    test_set = [
        [1, 1.5],
        [1, 3.0],
        [1, 6.0]
    ]
    test_expected = [
        3,
        6,
        12
    ]
    np.seterr(all='raise')
    perceptron = Linear(2, learning_rate)
    w_min, iterations, previous_weights, training_errors, test_errors = perceptron\
        .train(training_set, training_expected, [], [], 4, 30000, 0.01)
    results = perceptron.test(test_set, w_min)

    print('expected: ', test_expected)
    print('results: ', results)

def linear_perceptron_test_k():
    """ Learns Y= 2X + 0"""
    training_set = [
        [1, 1.0],
        [1, 2.0],
        [1, 3.0],
        [1, 4.0],
        [1, 5.0]
    ]
    learning_rate = 0.01
    training_expected = [2.0, 4.0, 6.0, 8.0, 10.0]
    test_set = [
        [1, 1.5],
        [1, 3.0],
        [1, 6.0]
    ]
    test_expected = [
        3,
        6,
        12
    ]
    np.seterr(all='raise')
    perceptron = Linear(2, learning_rate)
    w_min, iterations, previous_weights, training_errors, test_errors = perceptron\
        .k_cross_validation(training_set, training_expected, 3, 30000, 0.01)
    results = perceptron.test(test_set, w_min)

    print('expected: ', test_expected)
    print('results: ', results)


linear_perceptron_test_k()
