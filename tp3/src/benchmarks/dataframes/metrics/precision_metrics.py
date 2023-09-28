from pandas import DataFrame

from src.classes.NeuralNetwork import NeuralNetwork
from src.classes.metrics.Precision import Precision


def precision_metrics(max_epoch, network: NeuralNetwork, step, training_set, expected_set, test_set, test_expected,
                     batch_amount, epsilon, classifier, classes):
    rows = []
    for epoch in range(step, max_epoch, step):
        w_min, _, _, _ = network.train(training_set, expected_set, test_set, test_expected, batch_amount, epoch,
                                       epsilon)
        training_metrics = network.compute_metric(w_min, training_set, expected_set, Precision.calculate, classifier,
                                                  classes)
        test_metrics = network.compute_metric(w_min, test_set, test_expected, Precision.calculate, classifier, classes)
        rows.append({"epoch": epoch, "training": training_metrics, "test": test_metrics})

    return DataFrame(rows)
