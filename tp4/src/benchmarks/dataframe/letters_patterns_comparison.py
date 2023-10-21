import ast
import os
import itertools
import numpy as np
import pandas as pd
from string import ascii_lowercase as alc

FILE_PATH = os.path.join(os.pardir, os.pardir, os.pardir, "data", "letters.csv")


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


def letters_patterns_comparison_df():

    avg_dot_product = []
    max_dot_product = []
    rows = []

    letters = load_letters_map_from_file(FILE_PATH)
    combinations = itertools.combinations(letters.keys(), 4)
    for i, combination in enumerate(combinations):
        letters_combination = []
        for letter in combination:
            letters_combination.append(np.array(letters[letter]).flatten())
        letters_combination = np.array(letters_combination)

        orto_matrix = letters_combination.dot(letters_combination.T)
        np.fill_diagonal(orto_matrix, 0)
        row, _ = orto_matrix.shape

        avg_dot_product.append((np.abs(orto_matrix).sum() / (orto_matrix.size - row), combination))
        max_v = np.abs(orto_matrix).max()
        max_dot_product.append(((max_v, np.count_nonzero(np.abs(orto_matrix) == max_v) / 2), combination))

    df = pd.DataFrame(sorted(avg_dot_product), columns=["|<,>| medio", "grupo"])
    df2 = pd.DataFrame(sorted(max_dot_product), columns=["|<,>| max", "grupo"])

letters_patterns_comparison_df()