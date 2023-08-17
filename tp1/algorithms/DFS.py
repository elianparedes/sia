from collections import deque

from algorithms.AlgorithmABC import AlgorithmABC
from classes.Node import Node


class DFS(AlgorithmABC):
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
                for child in node.get_children():
                    stack.append(child)

            size += 1
        return None
