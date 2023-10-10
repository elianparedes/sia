import numpy as np

from src.classes.neurons.NeuronABC import NeuronABC
from src.classes.weights.WeightABC import WeightABC


class SimpleNeuron(NeuronABC):
    def __init__(self, weight_qty: int, weights_calculator: WeightABC):
        self.weights = weights_calculator.calculate(weight_qty)

    def get_weights(self) -> list[float]:
        return self.weights
