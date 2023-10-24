import os

import numpy as np
import pandas as pd
from pandas import DataFrame

from src.classes.networks.Hopfield import Hopfield
from src.utils.LettersUtils import LettersUtils

LETTERS_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data", "letters.csv")

def hopfield_energy_df(epochs, patterns, input_state, ratio) -> DataFrame:
    letters_map = LettersUtils.load_letters_map_from_file(LETTERS_PATH)
    selected_letters = []
    for letter in patterns:
        selected_letters.append(np.array(letters_map[letter]).flatten().tolist())

    input_pattern = np.array(letters_map[input_state]).flatten().tolist()
    input_pattern = LettersUtils.add_noise_random(input_pattern, ratio)

    network = Hopfield(selected_letters, input_pattern)
    energies = [network.calculate_energy(network.get_states(), network.get_weights_matrix())]

    for _ in range(epochs):
        network.train_epoch()
        energies.append(network.calculate_energy(network.get_states(), network.get_weights_matrix()))

    return pd.DataFrame({'Epoch': list(range(epochs + 1)), 'Energy': energies})
