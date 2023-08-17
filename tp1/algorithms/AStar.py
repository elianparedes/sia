import heapq

from algorithms.AlgorithmABC import AlgorithmABC
from algorithms.AlgorithmsUtils import _UtilityNode, Heuristics
from classes.Node import Node


class AStar(AlgorithmABC):

    @classmethod
    def execute(cls, initial_state):
        size = 0
        frontier = []
        heapq.heappush(frontier, _UtilityNode(Node(None, initial_state), 0))
        total_cost: dict[Node, float] = {Node(None, initial_state): 0}

        while frontier:
            utility_node = heapq.heappop(frontier)
            node = utility_node.node

            if node.state.is_solution():
                return node, size

            for child in node.get_children():
                new_cost = total_cost[node] + 1  # cost = 1
                if child not in total_cost or new_cost < total_cost[child]:
                    total_cost[child] = new_cost
                    priority = new_cost + Heuristics.heuristic_manhattan_distance(child.getState())
                    heapq.heappush(frontier, _UtilityNode(child, priority))

            size += 1
        return None
