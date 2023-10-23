import numpy as np
import plotly.graph_objects as go

from src.classes.similarity.Euclidean import Euclidean


class KohonenGraphs:

    @staticmethod
    def CompleteHeatmap(network, training_set, countries):
        winners = [network.neuron_qty * [0] for _ in range(network.neuron_qty)]
        country_matrix = [network.neuron_qty * [''] for _ in range(network.neuron_qty)]

        for i, register in enumerate(training_set):
            winner_neuron, _ = network.get_winner_neuron(register)
            winners[winner_neuron.x][winner_neuron.y] += 1
            country_matrix[winner_neuron.x][winner_neuron.y] += (countries[i] + '<br>')

        bold_country_matrix = [[f'<b>{text.strip()}</b>' for text in row] for row in country_matrix]

        heatmap = go.Heatmap(z=winners, colorscale='Viridis', text=bold_country_matrix, texttemplate="%{text}",
                             textfont={"size": 16, "color": 'rgb(255,255,255)'},
                             )
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

    @staticmethod
    def UMatrix(network):
        som = network.get_output_layer()  # Trained network
        row_qty = len(network.get_output_layer())
        col_qty = len(network.get_output_layer()[0])
        u_matrix = np.zeros((row_qty, col_qty))  # Initialize U-Matrix grid

        for i in range(row_qty):
            for j in range(col_qty):
                current_neuron = som[i][j]
                neighbor_distances = []

                # Calculate distances to neighbors
                for ni in [-1, 0, 1]:
                    for nj in [-1, 0, 1]:
                        if 0 <= i + ni < row_qty and 0 <= j + nj < col_qty:
                            neighbor = som[i + ni][j + nj]
                            distance = Euclidean.calculate(current_neuron.get_weights(), neighbor.get_weights())
                            neighbor_distances.append(distance)

                # Calculate mean distance and assign to U-Matrix
                u_matrix[i][j] = np.mean(neighbor_distances)

        return u_matrix

    @staticmethod
    def PlotUMatrix(network):
        umatrix_values = KohonenGraphs.UMatrix(network)
        # Create a Plotly figure for the heatmap
        fig = go.Figure(data=go.Heatmap(z=umatrix_values, colorscale='Greys'))

        # Add text annotations for z-values
        for i in range(len(umatrix_values)):
            for j in range(len(umatrix_values[0])):
                z_value = umatrix_values[i][j]
                fig.add_annotation(
                    text=f'<b>{z_value:.2f}</b>', x=j, y=i,
                    xref='x1', yref='y1',
                    showarrow=False,
                    font=dict(size=18, color='rgb(0, 255, 0)')
                )
        # Add z-values as text annotations on top of the heatmap cells

        # Customize the heatmap appearance
        fig.update_layout(
            title='Unified Distance Matrix (U-Matrix)',
            xaxis_title='Neuron X',
            yaxis_title='Neuron Y',
        )

        # Show the plot
        fig.show()

    @staticmethod
    def PlotUMatrixByVariable(network, input_names):
        for index, name in enumerate(input_names):
            umatrix_values = KohonenGraphs.UMatrixByVariable(network, index)
            # Create a Plotly figure for the heatmap
            fig = go.Figure(data=go.Heatmap(z=umatrix_values, colorscale='Greys'))

            # Add text annotations for z-values
            for i in range(len(umatrix_values)):
                for j in range(len(umatrix_values[0])):
                    z_value = umatrix_values[i][j]
                    fig.add_annotation(
                        text=f'<b>{z_value:.2f}</b>', x=j, y=i,
                        xref='x1', yref='y1',
                        showarrow=False,
                        font=dict(size=18, color='rgb(0, 255, 0)')
                    )
            # Add z-values as text annotations on top of the heatmap cells

            # Customize the heatmap appearance
            fig.update_layout(
                title='Unified Distance Matrix (U-Matrix) for ' + name,
                xaxis_title='Neuron X',
                yaxis_title='Neuron Y',
            )

            # Show the plot
            fig.show()

    @staticmethod
    def UMatrixByVariable(network, variable_index):
        som = network.get_output_layer()  # Trained network
        row_qty = len(network.get_output_layer())
        col_qty = len(network.get_output_layer()[0])
        u_matrix = np.zeros((row_qty, col_qty))  # Initialize U-Matrix grid

        for i in range(row_qty):
            for j in range(col_qty):
                current_neuron = som[i][j]
                neighbor_distances = []

                # Calculate distances to neighbors
                for ni in [-1, 0, 1]:
                    for nj in [-1, 0, 1]:
                        if 0 <= i + ni < row_qty and 0 <= j + nj < col_qty:
                            neighbor = som[i + ni][j + nj]
                            distance = abs(
                                current_neuron.get_weights()[variable_index] - neighbor.get_weights()[variable_index])
                            neighbor_distances.append(distance)

                # Calculate mean distance and assign to U-Matrix
                u_matrix[i][j] = np.mean(neighbor_distances)

        return u_matrix
