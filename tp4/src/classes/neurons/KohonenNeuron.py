from src.classes.neurons.NeuronABC import NeuronABC


class KohonenNeuron:
    def __init__(self, neuron: NeuronABC, x: int, y: int):
        super().__init__()
        self.neuron = neuron
        self._x = x
        self._y = y

    def get_weights(self) -> list[float]:
        return self.neuron.get_weights()

    def set_weights(self, weights: list[float]):
        self.neuron.set_weights(weights)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
