import plotly.express as px

from src.benchmarks.dataframe.hopfield_energy_df import hopfield_energy_df


def hopfield_energy_plot(epochs, patterns, input_state):
    df = hopfield_energy_df(epochs, patterns, input_state)
    fig = px.line(df, x='Epoch', y='Energy', title='Energy through epochs')

    fig.update_layout(
        xaxis_title='Epoch',
        yaxis_title='Energy'
    )

    fig.show()
