import numpy as np

from src.benchmarks.dataframe.hopfield_progression_df import hopfield_progression_df
from src.utils.LettersUtils import LettersUtils
import os
from plotly.subplots import make_subplots
import plotly.graph_objs as go

LETTERS_PATH = os.path.join(os.pardir, os.pardir, os.pardir, "data", "letters.csv")
BIG_LETTERS_PATH = os.path.join(os.pardir, os.pardir, os.pardir, "data", "letter_big.csv")


def hopfield_progression_plot(patterns, input_pattern, epochs, grid_size):
    fig = make_subplots(rows=1, cols=epochs, subplot_titles=[i for i in range(0, epochs)])
    fig.update_xaxes(scaleanchor="y", scaleratio=1)
    fig.update_yaxes(scaleanchor="x", scaleratio=1)

    heatmaps_by_epoch, heatmaps_pattern = hopfield_progression_df(epochs, patterns, input_pattern, grid_size)

    custom_colorscale = [
        [0, 'white'],
        [0.5, 'grey'],
        [1, 'black']
    ]

    for i in range(0, epochs):
        data = heatmaps_by_epoch[i][::-1]
        heatmap = go.Heatmap(z=data, colorscale=custom_colorscale)
        fig.add_trace(heatmap, row=1, col=i + 1)
        fig.update_xaxes(scaleanchor="y", scaleratio=1)
        fig.update_yaxes(scaleanchor="x", scaleratio=1)

    fig.update_layout(title="Neuron states by epochs")
    fig.show()

    # Patterns plot

    fig = make_subplots(rows=1, cols=len(patterns))

    custom_colorscale = [
        [0, 'white'],
        [0.5, 'blue'],
        [1, 'darkblue']
    ]

    for i in range(0, len(patterns)):
        data = heatmaps_pattern[i][::-1]
        heatmap = go.Heatmap(z=data, colorscale=custom_colorscale)
        fig.add_trace(heatmap, row=1, col=i + 1)
        fig.update_xaxes(scaleanchor="y", scaleratio=1)
        fig.update_yaxes(scaleanchor="x", scaleratio=1)

    fig.update_layout(title="Stored patterns in Hopfield network")
    fig.show()


def letter_progression_plot(selected_letters, input_letter, epochs):
    letters = LettersUtils.load_letters_map_from_file(LETTERS_PATH)
    patterns = []
    for letter in selected_letters:
        patterns.append(np.array(letters[letter]).flatten().tolist())

    input_pattern = np.array(letters[input_letter]).flatten().tolist()

    hopfield_progression_plot(patterns, input_pattern, epochs, 5)


def big_letter_progression_plot(selected_letters, input_letter, epochs):
    letters = LettersUtils.load_letters_map_from_file(BIG_LETTERS_PATH)
    patterns = []
    for letter in selected_letters:
        patterns.append(np.array(letters[letter]).flatten().tolist())

    input_pattern = np.array(letters[input_letter]).flatten().tolist()

    hopfield_progression_plot(patterns, input_pattern, epochs, 13)


letter_progression_plot(['a', 'b', 'c', 'd'], 'z', 5)
big_letter_progression_plot(['a', 'b', 'c', 'd'], 'a', 5)
