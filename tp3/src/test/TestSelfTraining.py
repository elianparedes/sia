import time

from src.classes.NeuralNetwork import NeuralNetwork
from src.utils import Function
from src.utils.DatasetUtils import DatasetUtils
from src.utils.ExerciseUtils import ExerciseUtils

LEARNING_RATE = 0.2
NOISE_RATIO = 0.2

BATCH_AMOUNT = 2
MAX_EPOCH = 10000
EPSILON = 0.1

def test_digits(neural_network: NeuralNetwork):
    dataset = ExerciseUtils.load_ex3_file()
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
    dataset, expected = DatasetUtils.expand_dataset(dataset, expected, 2)
    dataset = DatasetUtils.add_noise(dataset, NOISE_RATIO)
    training_set, training_expected, test_set, test_expected = DatasetUtils.split_dataset(dataset, expected, 0.8)

    return neural_network.train(training_set, training_expected, test_set, test_expected, BATCH_AMOUNT,
                                MAX_EPOCH, EPSILON)


architecture = [35, 10]
network = NeuralNetwork(architecture, Function.TAN_H, Function.TAN_H_DERIVATIVE, Function.TAN_H,
                        Function.TAN_H_DERIVATIVE, LEARNING_RATE, [-1, 1])

start = time.process_time()
w_min, curr_epoch, prev_weights, prev_errors = test_digits(network)
end = time.process_time()

print('time: ', end - start)
print('iterations: ', curr_epoch)
print('errors', prev_errors)
