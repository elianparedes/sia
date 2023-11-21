import pandas as pd
from sklearn.decomposition import PCA

from src.classes.models.NeuralNetwork import NeuralNetwork
from src.classes.utils.Extractor import Extractor


def ae_latent_space_df(trained_nn: NeuralNetwork):
    """
    :param trained_nn: Trained neural network
    :return: pca_df with following format: {idx, pca1, pca2, character}
    """
    middle_layer = Extractor.extract_latent_space(trained_nn)

    # Map with fonts.py
    latent_space = middle_layer.layer_output
    characters = ['`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'DEL'
                  ]

    # Applying PCA for dimensionality reduction to 2D
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(latent_space)

    # Creating a DataFrame with the PCA results and corresponding characters
    pca_df = pd.DataFrame(pca_result, columns=['PCA 1', 'PCA 2'])
    pca_df['Character'] = characters

    return pca_df
