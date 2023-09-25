from math import ceil
import random

import numpy as np


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

    @staticmethod
    def add_noise(dataset, ratio):
        """Adds noise given by ratio to a dataset (must be binary)"""
        amount = ceil(len(dataset[0]) * ratio)
        for i in range(0, len(dataset)):
            for j in range(0, amount):
                k = random.randint(0, len(dataset[j]) - 1)
                dataset[i][k] ^= 1

        return dataset

    @staticmethod
    def expand_dataset(dataset, expected, amount):
        """Expands a dataset amount times """
        dataset_copy = dataset.copy()
        expected_copy = expected.copy()
        for i in range(0, amount):
            dataset.extend(dataset_copy)
        for k in range(0, amount):
            expected.extend(expected_copy)

        return dataset, expected

    @staticmethod
    def normalize_to_range(data, new_min, new_max):
        """Normalizes array to a new range given by [new_min - new_max]"""
        min_val = min(data)
        max_val = max(data)
        normalized_data = np.interp(data, (min_val, max_val), (new_min, new_max))
        return normalized_data
