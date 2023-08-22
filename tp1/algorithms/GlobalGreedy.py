import heapq

from algorithms.AlgorithmABC import AlgorithmABC
from algorithms.AlgorithmsUtils import _UtilityNode
from classes.Node import Node
from heuristics.ManhattanDistance import ManhattanDistance


class GlobalGreedy(AlgorithmABC):
    @classmethod
    def execute(cls, initial_state, heuristic_fn=None, on_state_change=None):
        if heuristic_fn is None:
            heuristic_fn = ManhattanDistance
        expanded_nodes = 0
        visited = set()
        frontier = []
        root = Node(None, initial_state, 0)
        heapq.heappush(frontier, _UtilityNode(root, 0))

        while frontier:
            utility_node = heapq.heappop(frontier)
            node = utility_node.node

            if (on_state_change is not None):
                on_state_change(node.state)

            if node.state.is_solution():
                return node, expanded_nodes, len(frontier)

            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    if child not in visited:
                        heuristic_value = heuristic_fn.calculate(child.state)
                        heapq.heappush(frontier, _UtilityNode(child, heuristic_value))
            expanded_nodes += 1

        return None
