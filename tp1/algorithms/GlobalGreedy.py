import heapq

from algorithms.AlgorithmABC import AlgorithmABC
from algorithms.AlgorithmsUtils import _UtilityNode
from classes.Node import Node
from heuristics.ManhattanDistance import ManhattanDistance


class GlobalGreedy(AlgorithmABC):
    @classmethod
    def execute(cls, initial_state):
        size = 0
        visited = set()
        queue = []
        root = Node(None, initial_state)
        heapq.heappush(queue, _UtilityNode(root, 0))

        while queue:
            utility_node = heapq.heappop(queue)
            node = utility_node.node
            if node.state.is_solution():
                return node, size

            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    heuristic_value = ManhattanDistance.calculate(child.state)
                    heapq.heappush(queue, _UtilityNode(child, heuristic_value))
            size += 1

        return None
