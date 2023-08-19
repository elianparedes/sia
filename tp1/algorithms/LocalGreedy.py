from collections import deque

from algorithms.AlgorithmABC import AlgorithmABC
from classes.Node import Node
from heuristics.ManhattanDistance import ManhattanDistance


class LocalGreedy(AlgorithmABC):
    @classmethod
    def execute(cls, initial_state):
        size = 0
        visited = set()
        stack = deque()
        root = Node(None, initial_state)
        stack.append(root)

        while stack:
            node = stack.pop()
            if node.state.is_solution():
                return node, size

            if node not in visited:
                visited.add(node)
                sorted_children = sorted(node.get_children(),
                                         key=lambda child: ManhattanDistance.calculate(child.state))
                stack.extend(reversed(sorted_children))
            size += 1

        return None
