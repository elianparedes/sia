import os
import itertools
import numpy as np
import pandas as pd

from src.utils.IconsUtils import IconsUtils
from src.utils.LettersUtils import LettersUtils

FILE_PATH = os.path.join(os.pardir, os.pardir, os.pardir, "data", "icons.csv")


def icons_patterns_comparison_df():

    avg_dot_product = []
    max_dot_product = []

    icons = IconsUtils.load_icons_map_from_file(FILE_PATH)
    combinations = itertools.combinations(icons.keys(), 3)
    for i, combination in enumerate(combinations):
        icons_combination = []
        for icon in combination:
            icons_combination.append(np.array(icons[icon]).flatten())
        icons_combination = np.array(icons_combination)

        orto_matrix = icons_combination.dot(icons_combination.T)
        np.fill_diagonal(orto_matrix, 0)
        row, _ = orto_matrix.shape

        avg_dot_product.append((np.abs(orto_matrix).sum() / (orto_matrix.size - row), combination))
        max_v = np.abs(orto_matrix).max()
        max_dot_product.append(((max_v, np.count_nonzero(np.abs(orto_matrix) == max_v) / 2), combination))

    df = pd.DataFrame(sorted(avg_dot_product), columns=["|<,>| medio", "grupo"])
    df2 = pd.DataFrame(sorted(max_dot_product), columns=["|<,>| max", "grupo"])

    return df, df2

df, df2 = icons_patterns_comparison_df()
print(df)
print(df2)