import numpy as np

from src.classes.neurons.KohonenNeuron import KohonenNeuron
from src.classes.neurons.SimpleNeuron import SimpleNeuron
from src.classes.weights.Random import Random


def kohonen_rule(neighbour: KohonenNeuron, expected: list[float]) -> list[float]:
    """
    :return :neighbour's updated weights
    """
    np_expected = np.array(expected)
    np_weights = np.array(neighbour.get_weights())
    np_difference = np_expected - np_weights

    np_result = np_weights + 0.5 * np_difference

    return np_result.tolist()


weight_calc = Random()
neighbour = KohonenNeuron(SimpleNeuron(5, weight_calc), 1, 1)

expected = [10, 20, 30, 40, 50]

result = kohonen_rule(neighbour, expected)
print(type(result))
