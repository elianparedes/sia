from collections import deque

from algorithms.AlgorithmABC import AlgorithmABC
from classes.Node import Node
from heuristics.ManhattanDistance import ManhattanDistance


class LocalGreedy(AlgorithmABC):
    @classmethod
    def execute(cls, initial_state):
        expanded_nodes = 0
        visited = set()
        frontier = deque()
        root = Node(None, initial_state, 0)
        frontier.append(root)

        while frontier:
            node = frontier.pop()
            if node.state.is_solution():
                return node, expanded_nodes, len(frontier)

            if node not in visited:
                visited.add(node)
                sorted_children = sorted(node.get_children(),
                                         key=lambda child: ManhattanDistance.calculate(child.state))
                frontier.extend(reversed(sorted_children))
            expanded_nodes += 1

        return None
