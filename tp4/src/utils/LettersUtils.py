import ast
from string import ascii_lowercase as alc
import numpy as np


class LettersUtils:
    @staticmethod
    def load_letters_map_from_file(file_path):
        letters = []

        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                matrix = ast.literal_eval(line)  # Convert string representation of list to actual list
                letters.append(matrix)

        alphabet = []
        for i in alc:
            alphabet.append(i)

        letters_map = {}
        for i, letter in enumerate(letters):
            letters_map[alphabet[i]] = letter

        return letters_map

    @staticmethod
    def add_noise_random(array, ratio):
        if ratio < 0 or ratio > 1:
            raise ValueError("ratio must be between [0, 1]")

        num_elements_to_change = int(ratio * len(array))

        random_indices = np.random.choice(len(array), num_elements_to_change, replace=False)

        for index in random_indices:
            array[index] = -array[index]

        return array
