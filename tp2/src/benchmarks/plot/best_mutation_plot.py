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

def best_mutation_for_character(agg_data, title):
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
                showlegend=(idx == 0)
            ), row=row, col=col)

    fig.update_layout(title_text=title, barmode='group')
    fig.show()
def best_mutation_avg(data, title):
    colors = ['blue', 'red', 'green', 'purple', 'yellow']
    fig = go.Figure()
    for idx, method in data.iterrows():
        fig.add_trace(go.Bar(
            x=[method['method']],
            y=[method['mean']],
            error_y=dict(type='data', array=[method['std']], visible=True),
            name=method['method'],
            marker=dict(color=colors[idx % len(colors)])
        ))
    fig.update_layout(title_text=title, barmode='group')
    fig.show()

def best_mutation_by_fitness_plot(df):
    agg_data = df.groupby(['character', 'method'])['fitness'].agg(['mean', 'std']).reset_index()
    title = 'Average Fitness by Method and Character'
    best_mutation_for_character(agg_data, title)


def best_mutation_by_generation_plot(df):
    agg_data = df.groupby(['character', 'method'])['generation'].agg(['mean', 'std']).reset_index()
    title = 'Average Generation Count by Character and Method'
    best_mutation_for_character(agg_data, title)

def best_mutation_avg_fitness_plot(df):
    agg_data = df.groupby(['method'])['fitness'].agg(['mean', 'std']).reset_index()
    title = 'Average Fitness by Method'
    best_mutation_avg(agg_data,title)

def best_mutation_avg_generation_plot(df):
    agg_data = df.groupby(['method'])['generation'].agg(['mean', 'std']).reset_index()
    title = 'Average Generation count by Method'
    best_mutation_avg(agg_data,title)
