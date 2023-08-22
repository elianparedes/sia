import os
import math
import statistics

import numpy as np
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots

CSV_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "output", "algorithms_df.csv")

def standard_deviation(times):
    mean = statistics.mean(times)
    sum = 0
    for time in times:
        sum += (time-mean) ** 2
    return (sum/len(times))**0.5

def algorithms_benchmarks_plot():
    df = pd.read_csv(CSV_PATH)

    maps = df["map"].unique()
    algorithms = df["algorithm"].unique()

    cols = 3
    rows = math.ceil(len(maps) / cols)

    fig = make_subplots(rows=rows, cols=cols, subplot_titles=maps)

    for i, map in enumerate(maps):

        row = (i // cols) + 1
        col = (i % cols) + 1
        print(row, col)

        map_timestamps = df[df['map'] == map]

        x = algorithms
        filtered_data = map_timestamps.groupby(['algorithm'], sort=False)['without_deadlocks']
        deviations = []
        for name, group in filtered_data:
            deviations.append(standard_deviation(group))
        y = filtered_data.mean()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=[f"{i}" for i, val in enumerate(y.values)],
                name="Without deadlocks",
                marker_color="#F7BE15",
                textposition="outside",
                showlegend=False if i > 0 else True,
                error_y=dict(type='data', array=deviations)
            ),
            row=row,
            col=col
        )

        x = algorithms
        filtered_data = map_timestamps.groupby(['algorithm'], sort=False)['with_deadlocks']
        deviations = []
        for name, group in filtered_data:
            deviations.append(standard_deviation(group))
        y = filtered_data.mean()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="With deadlocks",
                marker_color="#1C818A",
                textposition="outside",
                showlegend=False if i > 0 else True,
                error_y=dict(type='data', array=deviations)
            ),
            row=row,
            col=col
        )

        fig.update_xaxes(title_text="Algorithms used", row=row, col=col)
        fig.update_yaxes(title_text="Execution time [seconds]", row=row, col=col)    

    fig.show()
