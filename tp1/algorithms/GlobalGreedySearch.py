import heapq

from algorithms.AlgorithmsUtils import _UtilityNode, Heuristics
from classes.Node import Node


class GlobalGreedySearch:
    @staticmethod
    def global_greedy_search(initial_state):
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
                    heuristic_value = Heuristics.heuristic_manhattan_distance(child.state)
                    heapq.heappush(queue, _UtilityNode(child, heuristic_value))

            size += 1
        return None
