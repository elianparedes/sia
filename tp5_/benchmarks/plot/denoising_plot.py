import numpy as np
import plotly.graph_objects as go
from pandas import DataFrame
import plotly.express as px

from classes.NeuralNetwork import NeuralNetwork
from classes.NoiseFunctions import gaussian_noise

MEAN = 0
STD_DEVIATION = 0.1


def denoising_plot(trained_nn: NeuralNetwork, characters):
    # noisy image
    data = [characters[1]]
    data = trained_nn.predict(gaussian_noise(data, MEAN, STD_DEVIATION))

    arr = np.array(data)
    data = arr.reshape((7, 5))

    fig = px.imshow(data)
    fig.show()

    # recovered data
    data = trained_nn.predict(trained_nn.predict(characters[1]))

    arr = np.array(data)
    data = arr.reshape((7, 5))

    fig = px.imshow(data)
    fig.show()

    # original image
    data = characters[1]

    arr = np.array(data)
    data = arr.reshape((7, 5))

    fig = px.imshow(data)
    fig.show()
