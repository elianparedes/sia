import os

from src.classes.NeuralNetwork import NeuralNetwork
from src.utils import Function
from src.utils.DatasetUtils import DatasetUtils
from src.utils.ExerciseUtils import ExerciseUtils
from src.benchmarks.dataframes.metrics.accuracy_metrics import accuracy_metrics
from src.benchmarks.plot.metrics.accuracy_metrics_plot import acurracy_metrics_plot
from src.benchmarks.dataframes.metrics.f1_metrics import f1_metrics
from src.benchmarks.plot.metrics.f1_metrics import f1_metrics_plot
from src.benchmarks.dataframes.metrics.recall_metrics import recall_metrics
from src.benchmarks.plot.metrics.recall_metrics import recall_metrics_plot
from src.benchmarks.dataframes.metrics.precision_metrics import precision_metrics
from src.benchmarks.plot.metrics.precision_metrics import precision_metrics_plot

DIGITS_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej3-digitos.txt")

STEP = 10
CLASSES = 10


def number_metrics(epsilon, learning_rate, max_epoch, batch_amount, noise):
    dataset = ExerciseUtils.load_ex3_file(DIGITS_PATH)
    expected = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

    architecture = [35, 10, 10]
    dataset, expected = DatasetUtils.expand_dataset(dataset, expected, 2)
    dataset = DatasetUtils.add_noise(dataset, noise)
    training_set, training_expected, test_set, test_expected = DatasetUtils.split_dataset(dataset, expected, 0.8)

    network = NeuralNetwork(architecture, Function.TAN_H, Function.TAN_H_DERIVATIVE, Function.TAN_H,
                            Function.TAN_H_DERIVATIVE, learning_rate, [-1, 1])

    df = accuracy_metrics(max_epoch, network, 10, training_set, training_expected, test_set, test_expected,
                          batch_amount, epsilon, network.classifier, CLASSES)
    acurracy_metrics_plot(df)

    df = f1_metrics(max_epoch, network, 10, training_set, training_expected, test_set, test_expected,
                    batch_amount, epsilon, network.classifier, CLASSES)
    f1_metrics_plot(df)

    df = precision_metrics(max_epoch, network, 10, training_set, training_expected, test_set, test_expected,
                           batch_amount, epsilon, network.classifier, CLASSES)
    precision_metrics_plot(df)

    df = recall_metrics(max_epoch, network, 10, training_set, training_expected, test_set, test_expected,
                        batch_amount, epsilon, network.classifier, CLASSES)
    recall_metrics_plot(df)
