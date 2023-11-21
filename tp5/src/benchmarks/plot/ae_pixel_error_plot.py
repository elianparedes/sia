from pandas import DataFrame
import plotly.graph_objects as go


def ae_pixel_error_plot(error_df: DataFrame):
    # Create a line graph with Plotly
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=error_df['epoch'],
        y=error_df['pixel_error'],
        mode='lines',  # Use 'lines' mode for a line graph
        line=dict(color='blue'),  # Set the line color
        name='Pixel Error vs. Epochs'
    ))

    # Customize layout
    fig.update_layout(
        title='Line Graph of Pixel Error vs. Epochs',
        xaxis=dict(title='Epoch (hundreds)'),
        yaxis=dict(title='Pixel Error'),
    )

    # Show the plot
    fig.show()
    