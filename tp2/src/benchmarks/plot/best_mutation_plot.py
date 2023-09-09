import pandas as pd
import os
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def best_mutation_plot(df):
    agg_data = df.groupby(['character', 'method'])['generation'].agg(['mean', 'std']).reset_index()

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

            diff = data['mean'] - data['std']
            is_positive = diff >= 0

            array = data['std'] if is_positive.all() else data['std'] + (-diff)
            arrayminus = data['std'] if is_positive.all() else data['std'] - (-diff)

            fig.add_trace(go.Bar(
                x=[method],
                y=data['mean'],
                error_y=dict(type='data', array=array, arrayminus=arrayminus, visible=True, symmetric=False),
                name=method,
                marker=dict(color=color),
                showlegend=(idx == 0), 
                base=0,
            ), row=row, col=col)

    fig.update_layout(title_text='Average Generations to Max Fitness by Method and Character', barmode='group')
    fig.show()
