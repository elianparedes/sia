import plotly.graph_objects as go
import numpy as np
from pandas import DataFrame

characters_strings = [
    '`',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
    '{',
    '|',
    '}',
    '~',
    'DEL'
]


def vae_latent_space_plot(latent_df: DataFrame):
    fig = go.Figure()
    colorscale = [
        f'rgba({np.random.randint(0, 256)}, {np.random.randint(0, 256)}, {np.random.randint(0, 256)}, 1)' for _ in range(32)]

    for i in range(32):
        group_data = latent_df[latent_df['Group'] == i + 1]
        x_values = group_data['Dimension_1']
        y_values = group_data['Dimension_2']

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            marker=dict(size=5, color=colorscale[i]),
            name=f'Character "{characters_strings[i]}"'
        ))

    # Customize layout
    fig.update_layout(
        title='Scatter Plots of Latent Space Grouped by 32 Values',
        xaxis=dict(title='Dimension 1'),
        yaxis=dict(title='Dimension 2'),
    )

    # Show the plot
    fig.show()


def vae_latent_space_plot_old(latent_df: DataFrame):
    fig = go.Figure()

    for i in range(32):
        x_values = [latent_df[j][i, 0] for j in range(len(latent_df))]
        y_values = [latent_df[j][i, 1] for j in range(len(latent_df))]

        fig.add_trace(go.Scatter(
            x=x_values,
            y=y_values,
            mode='markers',
            marker=dict(size=5),
            name=f'Value {i + 1}'
        ))

    # Customize layout
    fig.update_layout(
        title='Scatter Plots of Latent Space Grouped by 32 Values',
        xaxis=dict(title='Dimension 1'),
        yaxis=dict(title='Dimension 2'),
    )

    # Show the plot
    fig.show()
