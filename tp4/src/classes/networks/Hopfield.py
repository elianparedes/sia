from src.classes.networks.NetworkABC import NetworkABC
from src.classes.neurons.HopfieldNeuron import HopfieldNeuron
from src.classes.neurons.SimpleNeuron import SimpleNeuron
import math
import numpy as np

class Hopfield(NetworkABC):

    # weights_calculator = calculator

    def __init__(self, patterns: list[list[int]], input_state: list[int]) -> None:
        super().__init__()
        self.patterns = patterns
        self.neurons = self.__initialize_neurons(input_state)

    def __calculate_weights(self, index: int) -> list[float]:
        n = len(self.patterns[0])
        p = len(self.patterns)
        weights = [0] * n

        for j in range(n):
            if j == index:
                weights[j] = 0
                continue

            for mu in range(p):
                weights[j] += self.patterns[mu][index] * self.patterns[mu][j]
            weights[j] = (1 / n) * weights[j]

        return weights
    
    def calculate_energy(self, states, weights) -> float:
        energy = 0
        for i in enumerate(weights[0]):
            for j in enumerate(weights[0]):
                if j > i:
                    energy = energy + weights[i][j]*states[i]*states[j]

        energy = -1 * energy
        return energy

    def __initialize_neurons(self, input_state):
        neurons = []
        for i, state in enumerate(input_state):
            neurons.append(HopfieldNeuron(state, self.__calculate_weights(i)))
        return neurons

    def train_epoch(self) -> None:
        for i, neuron in enumerate(self.neurons):
            neuron_weights = neuron.get_weights()
            state = 0
            for j in range(len(self.neurons)):
                if i != j:
                    state += neuron_weights[j] * self.neurons[j].state
            state = (state >= 0) - (state < 0)
            if state == 0:
                raise Exception("State value is 0")
            neuron.set_state(state)

    def get_weights_matrix(self) -> list[list[float]]:
        weights = []
        for neuron in self.neurons:
            weights.append(neuron.get_weights())

        return weights

    def get_states(self) -> list[int]:
        states = []
        for neuron in self.neurons:
            states.append(neuron.state)

        return states
