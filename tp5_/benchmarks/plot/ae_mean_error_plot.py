from pandas import DataFrame
import plotly.graph_objects as go


def ae_mean_error_plot(error_df: DataFrame):
    # Create a scatter plot with Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=error_df['epoch'],
        y=error_df['error'],
        mode='markers',
        marker=dict(color='blue'),
        name='Error vs. Epochs'
    ))

    # Customize layout
    fig.update_layout(
        title='Scatter Plot of Error vs. Epochs',
        xaxis=dict(title='Epoch'),
        yaxis=dict(title='Error'),
    )

    # Show the plot
    fig.show()
