from abc import ABC, abstractmethod

from src.classes.Node import Node


class AlgorithmABC(ABC):

    """ Execute algorithm
    :returns If None, then no solution. Else tuple[last_node, expanded_nodes, frontier_size]
    """
    @classmethod
    @abstractmethod
    def execute(cls, initial_state, heuristic_fn=None, on_state_change=None) -> tuple[Node, int, int] | None:
        pass
