import heapq

from algorithms.AlgorithmsUtils import _UtilityNode, Heuristics
from classes.Node import Node
from classes.StateUtils import StateUtils


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
                print("Solution found opening ", size, " nodes using Global Greedy Search")
                StateUtils.draw_solution(node, 0)
                return node.state

            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    heuristic_value = Heuristics.heuristic_manhattan_distance(child.state)
                    heapq.heappush(queue, _UtilityNode(child, heuristic_value))

            size += 1
        return None
