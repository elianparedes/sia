import pandas as pd
import plotly.graph_objects as go


def precision_metrics_plot(df: pd.DataFrame):
    # Extract data for training and test metrics
    epoch = df["epoch"]
    training_metrics = df["training"]
    test_metrics = df["test"]

    # Create the figure
    fig = go.Figure()

    # Add traces for training and test metrics
    fig.add_trace(
        go.Scatter(x=epoch, y=training_metrics, mode='lines+markers', name='Training Metrics', line=dict(color='blue')))
    fig.add_trace(
        go.Scatter(x=epoch, y=test_metrics, mode='lines+markers', name='Test Metrics', line=dict(color='green')))

    # Customize the layout
    fig.update_layout(
        title='Training and Test Metrics Over Epochs (Precision)',
        xaxis=dict(title='Epoch'),
        yaxis=dict(title='Metrics'),
        legend=dict(x=0, y=1),
    )

    # Show the plot
    fig.show()