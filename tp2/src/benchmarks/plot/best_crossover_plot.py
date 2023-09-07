import pandas as pd
import os
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots

CSV_PATH = os.path.join(os.path.dirname(__file__), os.path.pardir, "best_crossover")

def best_crossover_plot(df=None):

    if df is None:
        df = pd.read_csv(CSV_PATH)
    agg_data = df.groupby(['character', 'method'])['fitness'].agg(['mean', 'std']).reset_index()

    characters = agg_data['character'].unique()
    methods = agg_data['method'].unique()
    colors = ['blue', 'red', 'green', 'purple', 'yellow']

    grid_size = math.ceil(math.sqrt(len(characters)))

    fig = make_subplots(rows=grid_size, cols=grid_size, subplot_titles=characters)

    for idx, character in enumerate(characters):
        row, col = divmod(idx, grid_size)
        row += 1
        col += 1

        subset = agg_data[agg_data['character'] == character]

        for method, color in zip(methods, colors):
            data = subset[subset['method'] == method]
            fig.add_trace(go.Bar(
                x=[method],
                y=data['mean'],
                error_y=dict(type='data', array=data['std'], visible=True),
                name=method,
                marker=dict(color=color),
                showlegend=(idx == 0)  # Show legend only in the first subplot
            ), row=row, col=col)

    fig.update_layout(title_text='Average Fitness by Method and Character', barmode='group')
    fig.show()
