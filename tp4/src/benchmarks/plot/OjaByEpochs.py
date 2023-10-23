import pandas as pd

from src.classes.algorithms.OjaAlgorithm import OjaAlgorithm
import plotly.express as px


class OjaEpochsGraph:
    @staticmethod
    def plot(neural_network, input, initial_learning_rate, epochs,pc1_real):

        epochs_graph = []
        error_graph = []
        for i in range(1,epochs,10):
            epochs_graph.append(i)
            OjaAlgorithm.train(neural_network,input,initial_learning_rate,10)
            error_graph.append(OjaAlgorithm.error(neural_network, input, pc1_real))
        df = pd.DataFrame(dict(
            epochs=epochs_graph,
            error=error_graph
        ))
        fig = px.line(df,x="epochs", y="error", title='Error by epochs')
        fig.show()
