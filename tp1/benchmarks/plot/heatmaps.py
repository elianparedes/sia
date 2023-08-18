import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from benchmarks.df.heatmaps import algorithms_heatmap_df

def algorithms_benchmarks_plot():
    df = algorithms_heatmap_df("example3.txt")

    algorithms = df["algorithm"].unique()

    cols = 5
    rows = 2

    fig = make_subplots(rows=rows, cols=cols, subplot_titles=algorithms)

    for i, algorithm in enumerate(algorithms):

        heatmap = df[df['algorithm'] == algorithm]

        z = heatmap["without_deadlocks"].tolist()[0]
        z_wdeadlocks = heatmap["with_deadlocks"].tolist()[0]

        fig.add_trace(
            go.Heatmap(
                z=z,
                showscale=False if i > 0 else True
            ),
            row=1,
            col=i + 1
        )   

        fig.add_trace(
            go.Heatmap(
                z=z_wdeadlocks,
                showscale=False if i > 0 else True
            ),
            row=2,
            col=i + 1
        )   

    fig.update_layout(yaxis = dict(scaleanchor = 'x'))
    fig.update_yaxes(autorange="reversed")
    fig.show()

algorithms_benchmarks_plot()