import numpy as np

from src.benchmarks.dataframe.hopfield_progression_df import hopfield_progression_df
from src.utils.IconsUtils import IconsUtils
from src.utils.LettersUtils import LettersUtils
import os
from plotly.subplots import make_subplots
import plotly.graph_objs as go

LETTERS_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data", "letters.csv")
BIG_LETTERS_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data", "letter_big.csv")
ICONS_PATH = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, "data", "icons.csv")


def hopfield_progression_plot(patterns, input_pattern, epochs, grid_size, ratio):
    input_pattern = LettersUtils.add_noise_random(input_pattern, ratio)

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
        __create_subplot(fig, custom_colorscale, heatmaps_by_epoch[i], 1, i + 1)

    title = "Neuron states by epochs (noise ratio = " + ratio.__str__() + ")"
    fig.update_layout(title=title)
    fig.show()

    # Patterns plot

    fig = make_subplots(rows=1, cols=len(patterns))

    custom_colorscale = [
        [0, 'white'],
        [0.5, 'blue'],
        [1, 'darkblue']
    ]

    for i in range(0, len(patterns)):
        __create_subplot(fig, custom_colorscale, heatmaps_pattern[i], 1, i + 1)

    fig.update_layout(title="Stored patterns in Hopfield network")
    fig.show()
    return


def __create_subplot(fig, custom_colorscale, heatmap, row, col):
    data = heatmap[::-1]
    heatmap = go.Heatmap(z=data, colorscale=custom_colorscale)
    fig.add_trace(heatmap, row=row, col=col)
    fig.update_xaxes(scaleanchor="y", scaleratio=1, showgrid=False,
                     zeroline=False,
                     showticklabels=False,
                     ticks='')
    fig.update_yaxes(scaleanchor="x", scaleratio=1, showgrid=False,
                     zeroline=False,
                     showticklabels=False,
                     ticks='')
    return


def letter_progression_plot(selected_letters, input_letter, epochs, ratio):
    letters = LettersUtils.load_letters_map_from_file(LETTERS_PATH)
    patterns = []
    for letter in selected_letters:
        patterns.append(np.array(letters[letter]).flatten().tolist())

    input_pattern = np.array(letters[input_letter]).flatten().tolist()

    hopfield_progression_plot(patterns, input_pattern, epochs, 5, ratio)
    return


def big_letter_progression_plot(selected_letters, input_letter, epochs, ratio):
    letters = LettersUtils.load_letters_map_from_file(BIG_LETTERS_PATH)
    patterns = []
    for letter in selected_letters:
        patterns.append(np.array(letters[letter]).flatten().tolist())

    input_pattern = np.array(letters[input_letter]).flatten().tolist()

    hopfield_progression_plot(patterns, input_pattern, epochs, 13, ratio)
    return


def icons_progression_plot(selected_icons, input_icon, epochs, ratio):
    icons = IconsUtils.load_icons_map_from_file(ICONS_PATH)
    patterns = []
    for icon in selected_icons:
        patterns.append(np.array(icons[icon]).flatten().tolist())

    input_pattern = np.array(icons[input_icon]).flatten().tolist()

    hopfield_progression_plot(patterns, input_pattern, epochs, 24, ratio)
    return


# letter_progression_plot(['a', 'b', 'c', 'd'], 'z', 5, 0)
# big_letter_progression_plot(['a', 'b', 'c', 'd', 'e'], 'z', 10, 0.05)
icons_progression_plot(["close", "share", "arrow", "arrow_back", "arrow_right"], "close", 5, 0.0000001)
