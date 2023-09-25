from src.classes.perceptron.Step import Step


def and_step_test():
    training_set = [
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1],
    ]
    learning_rate = 0.1
    training_expected = [-1, -1, -1, 1]
    test_set = [
        [1, -1, 1],
        [1, 1, -1],
        [1, -1, -1],
        [1, 1, 1],
    ]
    perceptron = Step(3, learning_rate)
    w_min = perceptron.train(training_set, training_expected, 30000, 0)
    results = perceptron.test(test_set, w_min)

    print('expected: ', training_expected)
    print('results: ', results)


and_step_test()
