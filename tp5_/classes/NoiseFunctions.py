import numpy as np


def salt_and_pepper(array, ratio):
    if ratio < 0 or ratio > 1:
        raise ValueError("ratio must be between [0, 1]")

    num_elements_to_change = int(ratio * len(array))

    random_indices = np.random.choice(len(array), num_elements_to_change, replace=False)

    for index in random_indices:
        array[index] = -array[index]

    return array


def gaussian_noise(dataset, mean, std_deviation):
    gaussian_dataset = []

    for sample in dataset:
        shape = np.shape(sample)
        noise = np.random.normal(mean, std_deviation, shape)
        gaussian_dataset.append(sample + noise)

    return gaussian_dataset
