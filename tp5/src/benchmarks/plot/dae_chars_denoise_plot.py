import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.classes.models.NeuralNetwork import NeuralNetwork

MEAN = 0
STD_DEVIATION = 0.5

def denoising_plot(trained_nn: NeuralNetwork, characters, noisy_characters):
    # recovered data
    results = trained_nn.predict([noisy_characters])[0][0]

    recovered_characters = []
    for recovered_character in results:
        recovered_character.round().astype(int)
        recovered_characters.append(np.reshape(recovered_character, (7, 5)))

    # noisy characters reshape
    noisy_characters = [noisy_character.reshape(
        7, 5) for noisy_character in noisy_characters]

    print(np.shape(noisy_characters))

    # Create 8x8 grid with recovered character and it's noisy version
    fig = make_subplots(rows=8, cols=8)
    for i, (noisy_character, recovered_character) in enumerate(zip(noisy_characters, recovered_characters)):
        fig.add_trace(go.Heatmap(z=np.flipud(noisy_character), colorscale="Greys_r", showscale=False),
                      row=1 + i // 4, col=1 + 2 * (i % 4))

        fig.update_xaxes(
            scaleanchor='x', row=1 + i // 4, col=1 + 2 * (i % 4), showgrid=False, showticklabels=False, zerolinecolor='rgba(0,0,0,0)')
        fig.update_xaxes(
            scaleanchor='x', row=1 + i // 4, col=2 + 2 * (i % 4), showgrid=False, showticklabels=False, zerolinecolor='rgba(0,0,0,0)')

        fig.add_trace(go.Heatmap(z=np.flipud(recovered_character), colorscale="Greys_r", showscale=False),
                      row=1 + i // 4, col=2 + 2 * (i % 4))

        fig.update_yaxes(
            scaleanchor='x', row=1 + i // 4, col=1 + 2 * (i % 4), showgrid=False, showticklabels=False, zerolinecolor='rgba(0,0,0,0)')
        fig.update_yaxes(
            scaleanchor='x', row=1 + i // 4, col=2 + 2 * (i % 4), showgrid=False, showticklabels=False, zerolinecolor='rgba(0,0,0,0)')

    fig.update_layout(
        plot_bgcolor='black',
        paper_bgcolor='white',
    )

    fig.show()
