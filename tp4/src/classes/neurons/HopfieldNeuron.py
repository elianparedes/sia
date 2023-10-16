from src.classes.neurons.NeuronABC import NeuronABC


class HopfieldNeuron(NeuronABC):

    def __init__(self, state: int, weights: list[float]) -> None:
        super().__init__()
        self.state = state
        self.weights = weights

    def get_weights(self) -> list[float]:
        return self.weights

    def set_weights(self, weights: list[float]):
        self.weights = weights

    def get_state(self) -> int:
        return self.state

    def set_state(self, state: int):
        self.state = state
