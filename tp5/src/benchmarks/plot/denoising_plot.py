import numpy as np
import plotly.express as px

from src.classes.models.NeuralNetwork import NeuralNetwork

MEAN = 0
STD_DEVIATION = 0.09


def denoising_plot(trained_nn: NeuralNetwork, characters, noisy_characters):

    # noisy image
    data = noisy_characters[1]

    arr = np.array(data)
    data = arr.reshape((7, 5))

    fig = px.imshow(data, title="noisy", color_continuous_scale='gray')
    fig.show()

    # recovered data
    data = trained_nn.predict([noisy_characters])

    arr = np.array(data[0][0][1].round().astype(int))
    data = arr.reshape((7, 5))

    fig = px.imshow(data, title="recovered", color_continuous_scale='gray')
    fig.show()

    # original image
    data = characters[1]

    arr = np.array(data)
    data = arr.reshape((7, 5))

    fig = px.imshow(data, title="original", color_continuous_scale='gray')
    fig.show()
