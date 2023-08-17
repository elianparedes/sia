from abc import ABC, abstractmethod

from classes.Node import Node


class AlgorithmABC(ABC):
    @classmethod
    @abstractmethod
    def execute(cls, initial_state) -> tuple[Node, int] | None:
        pass
