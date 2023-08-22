import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def max_value_from_matrix(matrix):
    return np.amax(matrix)

def min_value_from_matrix(matrix):
    return np.amin(matrix)

def algorithms_heatmaps_plot(df):
    algorithms = df["algorithm"].unique()

    cols = 5
    rows = 2

    zmax = max(df["without_deadlocks"].apply(max_value_from_matrix))
    zmin = min(df["without_deadlocks"].apply(min_value_from_matrix))

    zmax_wdeadlocks = max(df["with_deadlocks"].apply(max_value_from_matrix))
    zmin_wdeadlocks = min(df["with_deadlocks"].apply(min_value_from_matrix))

    zmax_global = max(zmax, zmax_wdeadlocks)
    zmin_global = min(zmin, zmin_wdeadlocks)

    fig = make_subplots(rows=rows, cols=cols, subplot_titles=algorithms)

    for i, algorithm in enumerate(algorithms):
        heatmap = df[df['algorithm'] == algorithm]

        z = heatmap["without_deadlocks"].tolist()[0]
        z_wdeadlocks = heatmap["with_deadlocks"].tolist()[0]

        fig.add_trace(
            go.Heatmap(
                z=z,
                zmax=zmax_global,
                zmin=zmin_global,
                text=z,
                showscale=False if i > 0 else True
            ),
            row=1,
            col=i + 1
        )

        fig.add_trace(
            go.Heatmap(
                z=z_wdeadlocks,
                zmax=zmax_global,
                zmin=zmin_global,
                text=z_wdeadlocks,
                showscale=False
            ),
            row=2,
            col=i + 1
        )

    
    for i in range(1, cols + 1):
        fig.update_xaxes(title_text="X map point", scaleanchor='x', row=2, col=i)
        fig.update_xaxes(title_text="X map point", scaleanchor='x', row=1, col=i)
        fig.update_yaxes(title_text="Y map point", scaleanchor='x', row=1, col=i)
        fig.update_yaxes(title_text="Y map point", scaleanchor='x', row=2, col=i)
        
    fig.update_yaxes(autorange="reversed")
    
    fig.show()
