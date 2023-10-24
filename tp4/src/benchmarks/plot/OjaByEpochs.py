from typing import Any

import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from src.classes.algorithms.OjaAlgorithm import OjaAlgorithm
from src.utils.FileUtils import FileUtils


class OjaEpochsGraph:
    @staticmethod
    def plot(neural_network, input, initial_learning_rate, epochs, pc1_real):
        epochs_graph = []
        error_graph = []
        for i in range(1, epochs, 10):
            epochs_graph.append(i)
            OjaAlgorithm.train(neural_network, input, initial_learning_rate, 10)
            error_graph.append(OjaAlgorithm.error(neural_network, input, pc1_real))
        df = pd.DataFrame(dict(
            epochs=epochs_graph,
            error=error_graph
        ))
        fig = px.line(df, x="epochs", y="error", title='Error by epochs')
        fig.show()
        return

    @staticmethod
    def setup() -> tuple[list[str], Any, PCA]:
        """
        :return: list[entries, scaled_data, pca]
        """
        entries, countries, variables = FileUtils.load_europe_csv()
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(entries)

        pca = PCA(n_components=len(variables))
        pca = pca.fit_transform(scaled_data)
        return entries[0], scaled_data, pca
