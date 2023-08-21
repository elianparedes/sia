import os
import math
import pandas as pd
import statistics

import plotly.graph_objects as go
from plotly.subplots import make_subplots

CSV_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "output", "heuristic.csv")

def standard_deviation(times):
    mean = statistics.mean(times)
    sum = 0
    for time in times:
        sum += (time-mean) ** 2
    return (sum/len(times))**0.5

def heuristics_time_benchmarks_plot():
    df = pd.read_csv(CSV_PATH)

    maps = df["map"].unique()
    algorithms = df["algorithm"].unique()

    cols = 3
    rows = math.ceil(len(maps) / cols)

    fig = make_subplots(rows=rows, cols=cols, subplot_titles=maps)

    for i, map in enumerate(maps):

        row = (i % rows) + 1
        col = (i % cols) + 1

        map_timestamps = df[df['map'] == map]

        x = algorithms
        filtered_data = map_timestamps[map_timestamps['heuristic'] == 'manhattan_distance']
        filtered_times = filtered_data.groupby(['algorithm'])['time']
        y = filtered_times.mean()
        deviations = []
        for filter_time in filtered_times:
            deviations.append(standard_deviation(filter_time))

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Manhattan distance",
                texttemplate='%{text:.3f}',
                marker_color="#F7BE15",
                textposition="outside",
                showlegend=False if i > 0 else True,
                error_y = dict(type='data', array=deviations)
            ),
            row=row,
            col=col
        )

        x = algorithms
        filtered_data = map_timestamps[map_timestamps['heuristic'] == 'min_distance']
        y = filtered_data.groupby(['algorithm'])['time'].mean()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Min distance",
                texttemplate='%{text:.3f}',
                marker_color="#1C818A",
                textposition="outside",
                showlegend=False if i > 0 else True
            ),
            row=row,
            col=col,
        )

        x = algorithms
        filtered_data = map_timestamps[map_timestamps['heuristic'] == 'bipartite']
        y = filtered_data.groupby(['algorithm'])['time'].mean()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Bipartite",
                texttemplate='%{text:.3f}',
                marker_color="#293462",
                textposition="outside",
                showlegend=False if i > 0 else True
            ),
            row=row,
            col=col,
        )

        x = algorithms
        filtered_data = map_timestamps[map_timestamps['heuristic'] == 'heuristic_combination']
        y = filtered_data.groupby(['algorithm'])['time'].mean()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Heuristic combination",
                texttemplate='%{text:.3f}',
                marker_color="#F0B26E",
                textposition="outside",
                showlegend=False if i > 0 else True
            ),
            row=row,
            col=col,
        )

        fig.update_xaxes(title_text="Algorithms used", row=row, col=col)
        fig.update_yaxes(title_text="Execution time [seconds]", row=row, col=col)

    fig.show()