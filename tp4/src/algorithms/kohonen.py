import csv
import json
import os

from src.classes.networks.Kohonen import Kohonen
from src.classes.similarity.Euclidean import Euclidean
from src.classes.similarity.Exponential import Exponential
from src.classes.weights.Random import Random
from src.classes.weights.SetBased import SetBased

CONFIG_MAP = {
    "similarity": {
        "euclidean": Euclidean,
        "exponential": Exponential
    },
    "weights_initializer": {
        "random": Random,
        "set_based": SetBased
    }
}
CONFIG_PATH = os.path.join(os.pardir, os.pardir, "config.json")
with open(CONFIG_PATH, 'r') as f:
    config = json.load(f)["algorithms"]["kohonen"]

INPUT_PATH = config["input_path"]
project_path = os.path.join(os.pardir, os.pardir)
input_path_parts = INPUT_PATH.strip("/").split("/")

INPUT_PATH = os.path.join(project_path, *input_path_parts)
INPUT = []

with open(INPUT_PATH, 'r') as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    for row in reader:
        INPUT.append(row)

WEIGHTS_QTY = len(INPUT[0])
NEURON_QTY = config["neuron_qty"]
SIMILARITY_TYPE = CONFIG_MAP["similarity"][config["similarity"]]
INIT_RADIUS = config["radius"]
INIT_LEARNING_RATE = config["learning_rate"]

WEIGHT_INITIALIZER = CONFIG_MAP["weights_initializer"][config["weights_initializer"]]
if config["weights_initializer"] == "set_based":
    WEIGHT_INITIALIZER = WEIGHT_INITIALIZER(INPUT)
else:
    WEIGHT_INITIALIZER = WEIGHT_INITIALIZER()

kohonen_network = Kohonen(WEIGHTS_QTY, NEURON_QTY, SIMILARITY_TYPE, WEIGHT_INITIALIZER)
