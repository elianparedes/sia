from src.classes.neurons.NeuronABC import NeuronABC


class KohonenNeuron:
    def __init__(self, neuron: NeuronABC) -> None:
        super().__init__()
        self.neuron = neuron

    def get_weights(self):
        return self.neuron.get_weights()
