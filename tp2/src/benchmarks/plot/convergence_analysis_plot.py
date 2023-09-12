import pandas as pd
import os
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

from src.utils.ConfigUtils import ConfigUtils


def convergence_analysis_plot(df):
    fig = make_subplots(rows=2, cols=2, subplot_titles=list(ConfigUtils.CHARACTERS.keys()))
    added_method_names = set()

    method_colors = {
        'single': '#636EFA',
        'limited': '#EF553B',
        'complete': '#32CC96',
        'uniform': '#AB63FA',
    }

    for idx, char in enumerate(ConfigUtils.CHARACTERS.keys()):
        subset = df[df['character'] == char]
        methods = df['method'].unique()

        row = (idx // 2) + 1
        col = (idx % 2) + 1

        for method in methods:
            rslt = subset[subset['method'] == method]

            if method not in added_method_names:
            
                traza = go.Scatter(
                    x=rslt['generation'],
                    y=rslt['fitness'],
                    name=method,  
                    line=dict(color=method_colors[method]),
                    showlegend=True
                )
               
                added_method_names.add(method)
            else:
                traza = go.Scatter(
                    x=rslt['generation'],
                    y=rslt['fitness'],
                    name=method,
                    line=dict(color=method_colors[method]),
                    showlegend=False
                )
            fig.add_trace(traza, row=row, col=col)

    fig.update_layout(title_text=f'Fitness Behaviour across Generations with Different Mutation Methods')
    fig.update_xaxes(title_text='Generations')
    fig.update_yaxes(title_text='Max Character Fitness')
    fig.show()
