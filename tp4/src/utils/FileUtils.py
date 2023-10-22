import csv
import os

import pandas as pd
from scipy.stats import stats

EUROPE_PATH = os.path.join(os.path.dirname(__file__),
                           os.pardir, os.pardir,
                           'data', 'europe.csv')


class FileUtils:
    def __init__(self):
        raise NotImplementedError("Cannot instantiate class")

    @staticmethod
    def load_europe_csv(path=None) -> tuple[list[list[str]], list[str], list[str]]:
        """
        :return: tuple[entries, list of countries, list of variables]
        """
        if path is None:
            path = EUROPE_PATH

        entries = []
        countries = []

        with open(path, 'r') as file:
            reader = csv.reader(file)

            # Skip the header row
            var_names = next(reader)
            var_names.pop(0)  # Eliminate 'Countries'

            for row in reader:
                # append all row except first position
                entry_names = row
                entries.append(row[1:])
                countries.append(row[0])

        entries = pd.DataFrame(entries).astype(float)
        entries = entries.apply(stats.zscore)
        entries = entries.values.tolist()

        return entries, countries, var_names
