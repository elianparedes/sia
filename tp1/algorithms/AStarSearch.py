from algorithms.AlgorithmsUtils import _UtilityNode, Heuristics
from tp1.classes.Node import Node
from tp1.classes.StateUtils import StateUtils
import heapq


class AStarSearch:

    @staticmethod
    def a_star_search(initial_state):
        size = 0
        frontier = []
        heapq.heappush(frontier, _UtilityNode(Node(None, initial_state), 0))
        total_cost: dict[Node, float] = {Node(None, initial_state): 0}

        while frontier:
            utility_node = heapq.heappop(frontier)
            node = utility_node.node

            if node.state.is_solution():
                print("Solution found opening ", size, " nodes using A*")
                StateUtils.draw_solution(node, 0)
                return node.state

            for child in node.get_children():
                new_cost = total_cost[node] + 1  # cost = 1
                if child not in total_cost or new_cost < total_cost[child]:
                    total_cost[child] = new_cost
                    priority = new_cost + Heuristics.heuristic_manhattan_distance(child.getState())
                    heapq.heappush(frontier, _UtilityNode(child, priority))

            size += 1
        return None
