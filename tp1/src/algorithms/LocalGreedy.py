from collections import deque

from src.algorithms.AlgorithmABC import AlgorithmABC
from src.classes.Node import Node
from src.heuristics.ManhattanDistance import ManhattanDistance


class LocalGreedy(AlgorithmABC):
    @classmethod
    def execute(cls, initial_state, heuristic_fn=None, on_state_change=None):
        if heuristic_fn is None:
            heuristic_fn = ManhattanDistance
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
                children = []
                for child in node.get_children():
                    if child not in visited:
                        children.append(child)
                sorted_children = sorted(children,
                                         key=lambda child: heuristic_fn.calculate(child.state))
                frontier.extend(reversed(sorted_children))
            expanded_nodes += 1

        return None
