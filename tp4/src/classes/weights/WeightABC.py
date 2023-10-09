from abc import ABC, abstractmethod


class WeightABC(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def calculate(self, weights_qty):
        pass
