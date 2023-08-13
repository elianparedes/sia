import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import pandas as pd
import numpy as np
import os
import json

CSV_PATH = os.path.join(os.path.dirname(__file__),
                        os.pardir, 'output', 'dataset_2e.csv')
CONFIG_FILE_PATH = os.path.join(os.path.dirname(
    __file__), os.pardir, 'config', 'dataset_2e.json')

# Load config
with open(CONFIG_FILE_PATH) as f:
    config = json.load(f)
    POKEMON_NAME = config["pokemon"]["name"]
    POKEMON_HP = config["pokemon"]["hp"]
    WIDTH = config["plot"]["width"]
    HEIGHT = config["plot"]["height"]
    Y_MAX = config["plot"]["y_max"]
    COLORSCHEME = config["plot"]["colorscheme"]

def plot_capture_rate_by_level(df):

    # Prepare data
    levels = df["level"].unique()
    status_effects = df["status_effect"].unique()

    # Config plot
    fig, ax = plt.subplots()
    fig.set_figwidth(WIDTH)
    fig.set_figheight(HEIGHT)

    # Calculate lines
    lines = []
    
    for status_effect in status_effects:
        x = []
        y = []

        for level in levels:
            total_attempts = len(df[(df['level'] == level) & (df['status_effect'] == status_effect)])
            successful_attempts = len(df[(df['level'] == level) & (df['status_effect'] == status_effect) & (df['catch_result'] == True)])
            capture_rate = successful_attempts / total_attempts
            x.append(level)
            y.append(capture_rate)

        lines.append({"legend": status_effect, "points": y})

    # Sort the list of tuples based on the average for display clarity
    sorted_lines = sorted(lines, key=lambda line: np.average(line['points']), reverse=True)

    # Select a colorscheme
    colormap = plt.colormaps['viridis_r'](np.linspace(0, 1, len(lines)))

    for i, line in enumerate(sorted_lines):
        # Adding a label for the legend
        ax.fill_between(x, line["points"], color=colormap[i], label=f"{line['legend']}")

    # Flatten the lines array
    np_array = []
    for line in sorted_lines:
        np_array.append(line['points'])

    # Calculate plot viewport
    ax.set_ylim([np.min(np_array), Y_MAX])
    ax.set_xlim([np.min(levels), np.max(levels)])
    plt.xticks(list(plt.xticks()[0]) + [levels.min(), levels.max()])

    # Set titles
    ax.set_ylabel('Catch Ratio')
    ax.set_xlabel('Pokemon Level')
    ax.set_title(f"{POKEMON_NAME.capitalize()} ({POKEMON_HP * 100:.0f} HP) Catch Ratio Level Impact Under Different Conditions")
    ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title="Status Effects", ncol=1)
    plt.grid(axis='x')

    plt.show()


# Generate plot
df = pd.read_csv(CSV_PATH)
plot_capture_rate_by_level(df)