import numpy as np

from src.classes.neurons.NeuronABC import NeuronABC
from src.classes.weights.WeightInitializerABC import WeightInitializerABC


class SimpleNeuron(NeuronABC):
    def __init__(self, weight_qty: int, weights_calculator: WeightInitializerABC):
        self.weights = weights_calculator.calculate(weight_qty)

    def get_weights(self) -> list[float]:
        return self.weights

    def set_weights(self, weights: list[float]):
        self.weights = weights
