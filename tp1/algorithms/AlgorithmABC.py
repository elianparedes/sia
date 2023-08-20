from abc import ABC, abstractmethod

from classes.Node import Node


class AlgorithmABC(ABC):

    """ Execute algorithm
    :returns If None, then no solution. Else tuple[last_node, expanded_nodes, frontier_size]
    """
    @classmethod
    @abstractmethod
    def execute(cls, initial_state, heuristic_fn=None) -> tuple[Node, int, int] | None:
        pass
