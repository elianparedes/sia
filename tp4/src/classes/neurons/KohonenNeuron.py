from src.classes.neurons.NeuronABC import NeuronABC


class KohonenNeuron:
    def __init__(self, neuron: NeuronABC):
        super().__init__()
        self.neuron = neuron

    def get_weights(self) -> list[float]:
        return self.neuron.get_weights()
