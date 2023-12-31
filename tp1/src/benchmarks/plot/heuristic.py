import os
import math
import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots

CSV_PATH = os.path.join(os.path.dirname(__file__), os.pardir, "output", "heuristic.csv")

def heuristics_benchmarks_plot(df):

    maps = df["map"].unique()
    algorithms = df["algorithm"].unique()

    cols = 3
    rows = math.ceil(len(maps) / cols)

    fig = make_subplots(rows=rows, cols=cols, subplot_titles=maps)

    for i, map in enumerate(maps):

        row = (i // cols) + 1
        col = (i % cols) + 1

        map_timestamps = df[df['map'] == map]

        x = algorithms
        data = map_timestamps[map_timestamps.heuristic.str.contains('manhattan_distance')]
        y = data['expanded_nodes'].unique()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Manhattan distance",
                marker_color="#F7BE15",
                textposition="outside",
                showlegend=False if i > 0 else True
            ).update(textfont=dict(size=8)),
            row=row,
            col=col
        )

        x = algorithms
        data = map_timestamps[map_timestamps.heuristic.str.contains('min_distance')]
        y = data['expanded_nodes'].unique()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Min distance",
                marker_color="#1C818A",
                textposition="outside",
                showlegend=False if i > 0 else True
            ).update(textfont=dict(size=8)),
            row=row,
            col=col,
        )

        x = algorithms
        data = map_timestamps[map_timestamps.heuristic.str.contains('bipartite')]
        y = data['expanded_nodes'].unique()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Bipartite",
                marker_color="#293462",
                textposition="outside",
                showlegend=False if i > 0 else True,
            ).update(textfont=dict(size=8)),
            row=row,
            col=col,
        )


        x = algorithms
        data = map_timestamps[map_timestamps.heuristic.str.contains('heuristic_combination')]
        y = data['expanded_nodes'].unique()

        fig.add_trace(
            go.Bar(
                x=x,
                y=y,
                text=y,
                name="Heuristic combination",
                marker_color="#F0B26E",
                textposition="outside",
                showlegend=False if i > 0 else True
            ).update(textfont=dict(size=8)),
            row=row,
            col=col,
        )

        fig.update_xaxes(title_text="Algorithms used", row=row, col=col)
        fig.update_yaxes(title_text="Expanded nodes", row=row, col=col)

        fig.update_traces(cliponaxis=False)

    fig.show()
