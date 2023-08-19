from abc import ABC, abstractmethod

from classes.State import State


class HeuristicABC(ABC):
    @classmethod
    @abstractmethod
    def calculate(cls, state: State) -> int:
        pass
