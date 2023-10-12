import numpy as np

from src.classes.networks.NetworkABC import NetworkABC
from src.classes.neurons.SimpleNeuron import SimpleNeuron
from src.classes.neurons.KohonenNeuron import KohonenNeuron
from src.classes.similarity.SimilarityABC import SimilarityABC
from src.classes.weights.WeightsInitializerABC import WeightInitializerABC


class Kohonen(NetworkABC):
    def __init__(self, weights_qty: int, neuron_qty: int,
                 similarity_type: SimilarityABC, weight_calculator: WeightInitializerABC):
        self.weights_qty = weights_qty
        self.neuron_qty = neuron_qty
        self.similarity_type = similarity_type
        self.output_layer = [
            [KohonenNeuron(SimpleNeuron(weights_qty, weight_calculator), i, j) for i in range(neuron_qty)]
            for j in range(neuron_qty)]

    def get_neighbours(self, x: int, y: int, r: float) -> list[KohonenNeuron]:
        """
        Gets the neighbours of the neuron in `(x,y)` within a radius `r`
        """
        result = []

        for i in range(int(x - r), int(x + r) + 1):
            if i < 0 or i >= len(self.output_layer):
                continue

            for j in range(int(y - r), int(y + r) + 1):
                if j < 0 or j >= len(self.output_layer[0]):
                    continue

                distance = ((x - i) ** 2 + (y - j) ** 2) ** 0.5

                if distance <= r:
                    result.append(self.output_layer[i][j])

        return result

    def get_winner_neuron(self, expected: list[float]) -> tuple[KohonenNeuron, float]:
        min_neuron = self.output_layer[0][0]
        min_value = self.similarity_type.calculate(expected, min_neuron.get_weights())

        for i in range(self.neuron_qty):
            for j in range(self.neuron_qty):
                candidate = self.output_layer[i][j]
                candidate_value = self.similarity_type.calculate(expected, candidate.get_weights())
                if candidate_value < min_value:
                    min_neuron = candidate
                    min_value = candidate_value

        return min_neuron, min_value

    def kohonen_rule(self, neighbour: KohonenNeuron, expected: list[float], learning_rate: float) -> list[float]:
        """
        :return :neighbour's updated weights
        """
        np_expected = np.array(expected)
        np_weights = np.array(neighbour.get_weights())
        np_difference = np_expected - np_weights

        np_result = np_weights + learning_rate * np_difference

        return np_result.tolist()

    def get_output_layer(self):
        return self.output_layer

