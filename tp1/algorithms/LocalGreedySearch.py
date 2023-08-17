from collections import deque

from algorithms.AlgorithmsUtils import Heuristics
from classes.Node import Node


class LocalGreedySearch:
    @staticmethod
    def local_greedy_search(initial_state):
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
                                         key=lambda child: Heuristics.heuristic_manhattan_distance(child.state))
                stack.extend(reversed(sorted_children))

            size += 1
        return None
