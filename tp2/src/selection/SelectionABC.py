from abc import ABC, abstractmethod


class SelectionABC(ABC):
    @classmethod
    @abstractmethod
    def select(cls, population: [], individuals: int):
        pass
