# Manhattan distance between player and box + box and goal
# This only works with one box, remove later
from classes.Node import Node
from classes.StateUtils import StateUtils


def heuristic(state):
    player_point = state.player_point
    box_point = state.boxes_points[0]
    goal_point = state.goals_points[0]
    return abs(player_point.x - box_point.x) + abs(player_point.y - box_point.y) \
           + abs(box_point.x - goal_point.x) + abs(box_point.y - goal_point.y)

class LocalGreedy:
    @staticmethod
    def local_greedy(initial_state):
        size = 0
        visited = []
        queue = []
        root = Node(None, initial_state)
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.state.is_solution():
                print("Solution found opening ", size, " nodes using Local Greedy Search")
                StateUtils.draw_solution(node, 0)
                return node.state
            if node.state not in visited:
                visited.append(node)
                for child in node.get_children():
                    queue.append(child)
            queue= sorted(queue, key=heuristic)
            size += 1
        return None