from collections import deque

from algorithms.AlgorithmABC import AlgorithmABC
from classes.Node import Node


class DFS(AlgorithmABC):
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
                for child in node.get_children():
                    frontier.append(child)

            expanded_nodes += 1
        return None
