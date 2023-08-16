from classes.Node import Node
from classes.StateUtils import StateUtils
import heapq


# Basic heuristic used for testing, remove later
def heuristic(state):
    player_point = state.player_point
    box_point = state.boxes_points.pop()
    state.boxes_points.add(box_point)
    goal_point = state.goals_points.pop()
    state.goals_points.add(goal_point)
    return abs(player_point.x - box_point.x) + abs(player_point.y - box_point.y) \
           + abs(box_point.x - goal_point.x) + abs(box_point.y - goal_point.y)


class _UtilityNode:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Node: {self.node}, Priority: {self.priority}"


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
                    priority = new_cost + heuristic(child.getState())
                    heapq.heappush(frontier, _UtilityNode(child, priority))

            size += 1
        return None
