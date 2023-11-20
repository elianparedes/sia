import os
import string

from pandas import DataFrame

FILE_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "benchmarks", "df_files")

class FileUtils:
    def __init__(self):
        raise NotImplementedError("Cannot instantiate class")

    @staticmethod
    def save_df_in_file(filename: string, dataframe: DataFrame):
        """
        File is saved inside "tp5/benchmarks/df_files"
        """
        path = os.path.join(FILE_PATH, filename + ".csv")
        dataframe.to_csv(path)
