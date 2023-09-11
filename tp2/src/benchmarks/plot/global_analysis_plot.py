import pandas as pd
import os
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

from src.utils.ConfigUtils import ConfigUtils


def global_analysis_avg(df, title):
    fig = make_subplots(rows=2, cols=2)
    row = 1
    col = 1
    grid_size = 4
    for idx,char in enumerate(ConfigUtils.CHARACTERS.keys()):
        subset = df[df['character'] == char]
        rslt = subset[subset['type'] == 'strength']
        fig.append_trace(go.Scatter(x=rslt['iteration'],y=rslt['value'],  name='strength'), row=row, col=col)
        rslt = subset[subset['type'] == 'health']
        fig.append_trace(go.Scatter(x=rslt['iteration'],y=rslt['value'],  name='health'), row=row, col=col)
        rslt = subset[subset['type'] == 'intelligence']
        fig.append_trace(go.Scatter(x=rslt['iteration'],y=rslt['value'],  name='intelligence'), row=row, col=col)
        rslt = subset[subset['type'] == 'agility']
        fig.append_trace(go.Scatter(x=rslt['iteration'],y=rslt['value'],  name='agility'), row=row, col=col)
        rslt = subset[subset['type'] == 'endurance']
        fig.append_trace(go.Scatter(x=rslt['iteration'],y=rslt['value'],  name='endurance'), row=row, col=col)
        fig.update_yaxes(title_text=char, row=row, col=col)

        if col == 2:
            row += 1
            col = 1
        else:
            col += 1

    fig.update_layout(height=600, width=800, title_text="Converge stats")
    fig.show()
