import heapq
from tp1.classes.Node import Node
from tp1.classes.StateUtils import StateUtils


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


class LocalGreedy:
    @staticmethod
    def local_greedy(initial_state):
        size = 0
        visited = set()
        queue = []
        root = Node(None, initial_state)
        heapq.heappush(queue, _UtilityNode(root, 0))

        while queue:
            utility_node = heapq.heappop(queue)
            node = utility_node.node

            if node.state.is_solution():
                print("Solution found opening ", size, " nodes using Local Greedy Search")
                StateUtils.draw_solution(node, 0)
                return node.state

            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    heuristic_value = heuristic(child.state)
                    heapq.heappush(queue, _UtilityNode(child, heuristic_value))

            size += 1
            print(size)
        return None