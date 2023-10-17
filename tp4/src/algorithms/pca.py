import csv
import json
import os

from src.benchmarks.plot.PCAScatterGraph import  PCAGraphs
from src.classes.algorithms.PCAAlgorithm import PCAAlgorithm

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

CONFIG_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, "config.json")
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)["algorithms"]["pca"]

INPUT_PATH = config["input_path"]
project_path = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
input_path_parts = INPUT_PATH.strip("/").split("/")

INPUT_PATH = os.path.join(project_path, *input_path_parts)
INPUT = []
COUNTRIES = []
ITEMS = []

file_path = INPUT_PATH
df = pd.read_csv(file_path)

# # Sort the DataFrame by the column of your choice (e.g., "GDP")
# sorted_df = df.sort_values(by="GDP")
#
# # Save the sorted DataFrame back to a CSV file
# output_file_path = INPUT_PATH
# sorted_df.to_csv(output_file_path, index=False)

with open(INPUT_PATH, 'r') as file:
    reader = csv.reader(file)
    first = False
    # Skip the header row
    for row in reader:
        if first == False:
            first = True
            ITEMS = row[1:]
            continue
        #append all row except first position
        INPUT.append(row[1:])
        COUNTRIES.append(row[0])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(INPUT)

# Implementacion casera
pc1, pc2, loadings = PCAAlgorithm.train(scaled_data)
PCAGraphs.scatter_plot_with_PBI(pc1, pc2, COUNTRIES, loadings, ITEMS)

# Implementacion de scikit
pca = PCA(n_components=4)
pca_result = pca.fit_transform(scaled_data)
loadings = pca.components_
loadings = loadings / np.linalg.norm(loadings, axis=1)[:, np.newaxis]
PCAGraphs.scatter_plot(pca_result, COUNTRIES, loadings, ITEMS)

# Boxplot
df = pd.DataFrame(INPUT).astype(float)
df = df.apply(stats.zscore)
PCAGraphs.blox_plot(df.values.tolist(), ITEMS)

# Scree plot
pca = PCA(n_components=7)
pca = pca.fit(scaled_data)
PCAGraphs.scree_plot(pca)
