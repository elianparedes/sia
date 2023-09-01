from collections import deque

from src.algorithms.AlgorithmABC import AlgorithmABC
from src.classes.Node import Node


class DFS(AlgorithmABC):
    @classmethod
    def execute(cls, initial_state, heuristic_fn=None, on_state_change=None):
        expanded_nodes = 0
        visited = set()
        frontier = deque()
        root = Node(None, initial_state, 0)
        frontier.append(root)
        while frontier:
            node = frontier.pop()

            if (on_state_change is not None):
                on_state_change(node.state)
                
            if node.state.is_solution():
                return node, expanded_nodes, len(frontier)

            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    if child not in visited:
                        frontier.append(child)

            expanded_nodes += 1
        return None
