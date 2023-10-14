import csv
import json
import os


from src.classes.algorithms.PCAAlgorithm import PCAAlgorithm

import pandas as pd
import numpy as np
import scipy.stats as stats

CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "config.json")
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)["algorithms"]["pca"]

INPUT_PATH = config["input_path"]
project_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
input_path_parts = INPUT_PATH.strip("/").split("/")

INPUT_PATH = os.path.join(project_path, *input_path_parts)
INPUT = []
COUNTRIES = []

with open(INPUT_PATH, 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    for row in reader:
        #append all row except first position
        INPUT.append(row[1:])
        COUNTRIES.append(row[0])

pca_values = PCAAlgorithm.train(INPUT)

