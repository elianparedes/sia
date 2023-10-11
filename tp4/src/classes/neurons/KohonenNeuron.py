from src.classes.neurons.NeuronABC import NeuronABC


class KohonenNeuron:
    def __init__(self, neuron: NeuronABC, x: int, y: int):
        super().__init__()
        self.neuron = neuron
        self._x = x
        self._y = y
        self.associated_entries = []

    def get_weights(self) -> list[float]:
        return self.neuron.get_weights()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
