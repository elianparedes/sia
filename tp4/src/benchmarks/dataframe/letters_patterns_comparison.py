import os
import itertools
import numpy as np
import pandas as pd

from src.utils.LettersUtils import LettersUtils

FILE_PATH = os.path.join(os.pardir, os.pardir, os.pardir, "data", "letters.csv")


def letters_patterns_comparison_df():

    avg_dot_product = []
    max_dot_product = []

    letters = LettersUtils.load_letters_map_from_file(FILE_PATH)
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

    return df, df2