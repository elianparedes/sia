import numpy as np

from src.benchmarks.dataframe.letters_progression_df import letters_progression_df
from src.utils.LettersUtils import LettersUtils
import os
from plotly.subplots import make_subplots
import plotly.graph_objs as go

FILE_PATH = os.path.join(os.pardir, os.pardir, os.pardir, "data", "letters.csv")


def letter_progression_plot(letters, input_letter, epochs, grid_size):
    letters = LettersUtils.load_letters_map_from_file(FILE_PATH)
    fig = make_subplots(rows=1, cols=epochs, subplot_titles = [i for i in range(0, epochs)])
    fig.update_xaxes(scaleanchor="y", scaleratio=1)
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    patterns = []

    for letter in letters:
        patterns.append(np.array(letters[letter]).flatten().tolist())

    letters_arrays = letters_progression_df(epochs, patterns, np.array(letters[input_letter]).flatten().tolist(), grid_size)
    custom_colorscale = [
        [0, 'white'],
        [0.5, 'grey'],
        [1, 'black']
    ]

    for i in range(0, epochs):
        data = letters_arrays[i][::-1]
        heatmap = go.Heatmap(z=data, colorscale=custom_colorscale)
        fig.add_trace(heatmap, row=1, col=i + 1)
        fig.update_xaxes(scaleanchor="y", scaleratio=1)
        fig.update_yaxes(scaleanchor="x", scaleratio=1)

    fig.update_layout(title="Neuron states by epochs")
    fig.show()


letter_progression_plot(['a', 'b', 'c', 'd'], 'f', 10, 5)
