import os as os


from src.classes.perceptron.NonLinear import NonLinear
from src.utils import Function
from src.utils.DatasetUtils import DatasetUtils
from src.utils.ExerciseUtils import ExerciseUtils

CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir, os.path.pardir,
                           "Data", "TP3-ej2-conjunto.csv")


def non_linear_perceptron_test():
    training_set, expected_set = ExerciseUtils.load_ex2_file(CONFIG_PATH)
    expected = DatasetUtils.normalize_to_range(expected_set, -1, 1)
    perceptron = NonLinear(3, 0.1, Function.TAN_H, Function.TAN_H_DERIVATIVE)
    w_min = perceptron.train(training_set, expected, 30000, 2.0)
    results = perceptron.test(training_set, w_min)

    print('expected: ', expected)
    print('results: ', results)


non_linear_perceptron_test()
