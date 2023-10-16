import csv
import json
import os


from src.classes.algorithms.PCAAlgorithm import PCAAlgorithm

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
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

with open(INPUT_PATH, 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    for row in reader:
        #append all row except first position
        INPUT.append(row[1:])
        COUNTRIES.append(row[0])

scaler = StandardScaler()
scaled_data = scaler.fit_transform(INPUT)


# Implementacion casera
pc1, pc2 = PCAAlgorithm.train(scaled_data)

pca_df = pd.DataFrame({"PC1": pc1, "PC2": pc2, "Country": COUNTRIES})
plt.figure(figsize=(10, 8))
plt.scatter(pca_df["PC1"], pca_df["PC2"])
plt.xlabel("Principal Component 1 (PC1)")
plt.ylabel("Principal Component 2 (PC2)")
plt.title("PCA Analysis")
plt.grid()
for i, country in enumerate(pca_df["Country"]):
    plt.annotate(country, (pca_df["PC1"][i], pca_df["PC2"][i]))
plt.show()


# Implementacion de scikit
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(data=pca_result, columns=["PC1", "PC2"])
pca_df["Country"] = COUNTRIES
plt.figure(figsize=(10, 8))
plt.scatter(pca_df["PC1"], pca_df["PC2"])
plt.xlabel("Principal Component 1 (PC1)")
plt.ylabel("Principal Component 2 (PC2)")
plt.title("PCA Analysis")
plt.grid()
for i, country in enumerate(pca_df["Country"]):
    plt.annotate(country, (pca_df["PC1"][i], pca_df["PC2"][i]))
plt.show()









