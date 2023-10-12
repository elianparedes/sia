import plotly.graph_objects as go
import plotly.offline as pyo


class KohonenGraphs:

    @staticmethod
    def CompleteHeatmap(network, training_set, countries):
        winners = [network.neuron_qty * [0] for _ in range(network.neuron_qty)]
        country_matrix = [network.neuron_qty * [''] for _ in range(network.neuron_qty)]

        for i, register in enumerate(training_set):
            winner_neuron, _ = network.get_winner_neuron(register)
            winners[winner_neuron.x][winner_neuron.y] += 1
            country_matrix[winner_neuron.x][winner_neuron.y] += (' ' + countries[i] + '\n')

        heatmap = go.Heatmap(z=winners, colorscale='Viridis', text=country_matrix, texttemplate="%{text}", textfont={"size": 10})
        # Create a layout for the heatmap
        layout = go.Layout(title='Complete Heatmap')
        # Create a figure and plot it
        fig = go.Figure(data=[heatmap], layout=layout)
        # Display the heatmap (you can also save it as an HTML file)
        # pyo.plot(fig, filename='heatmap.html')
        fig.show()

    @staticmethod
    def SingleVariableHeatMap(network, variable_index):
        weights = [network.neuron_qty * [0] for _ in range(network.neuron_qty)]
        for i in range(network.neuron_qty):
            for j in range(network.neuron_qty):
                weights[i][j] = network.get_output_layer()[i][j].get_weights()[variable_index]

        heatmap = go.Heatmap(z=weights, colorscale='Viridis')
        # Create a layout for the heatmap
        layout = go.Layout(title='Variable: ' + str(variable_index))
        # Create a figure and plot it
        fig = go.Figure(data=[heatmap], layout=layout)
        # Display the heatmap (you can also save it as an HTML file)
        # pyo.plot(fig, filename='heatmap.html')
        fig.show()

