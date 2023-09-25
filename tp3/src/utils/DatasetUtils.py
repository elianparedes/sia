from math import ceil
import random


class DatasetUtils:
    """Loads exercise files"""

    def __init__(self):
        raise NotImplementedError("Cannot instantiate class")

    @staticmethod
    def split_dataset(dataset, expected, ratio):
        amount = ceil(len(dataset) * ratio)
        training_set = []
        training_expected = []
        test_set = []
        test_expected = []
        while amount > 0:
            i = random.randint(0, len(dataset) - 1)
            training_set.append(dataset.pop(i))
            training_expected.append(expected.pop(i))
            amount -= 1

        test_set.extend(dataset)
        test_expected.extend(expected)
        return training_set, training_expected, test_set, test_expected
