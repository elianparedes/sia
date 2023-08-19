import heapq

from algorithms.AlgorithmABC import AlgorithmABC
from algorithms.AlgorithmsUtils import _UtilityNode
from classes.Node import Node
from heuristics.HeuristicsCombination import HeuristicsCombination
from heuristics.ManhattanDistance import ManhattanDistance
from heuristics.MinDistance import MinDistance


class AStar(AlgorithmABC):

    @classmethod
    def execute(cls, initial_state):
        expanded_nodes = 0
        frontier = []
        heapq.heappush(frontier, _UtilityNode(Node(None, initial_state, 0), 0))
        total_cost: dict[Node, float] = {Node(None, initial_state, 0): 0}

        while frontier:
            utility_node = heapq.heappop(frontier)
            node = utility_node.node
            if node.state.is_solution():
                return node, expanded_nodes, len(frontier)

            for child in node.get_children():
                new_cost = total_cost[node] + 1  # cost = 1
                if child not in total_cost or new_cost < total_cost[child]:
                    total_cost[child] = new_cost
                    priority = new_cost + HeuristicsCombination.calculate(child.get_state(), ManhattanDistance, MinDistance)
                    heapq.heappush(frontier, _UtilityNode(child, priority))

            expanded_nodes += 1
        return None
