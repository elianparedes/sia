class _UtilityNode:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"Node: {self.node}, Priority: {self.priority}"


class Heuristics:
    @staticmethod
    def heuristic_manhattan_distance(state):
        total_distance = 0
        for box in state.boxes_points:
            min_for_box = None
            for goal in state.goals_points:
                if min_for_box is None:
                    min_for_box = abs(box.x - goal.x) + abs(box.y - goal.y)
                if min_for_box > abs(box.x - goal.x) + abs(box.y - goal.y):
                    min_for_box = abs(box.x - goal.x) + abs(box.y - goal.y)
            total_distance += min_for_box
        return total_distance

    @staticmethod
    def min_heuristic(state):
        min_distance = None
        for box in state.boxes_points:
            player_distance = abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y)
            for goal in state.goals_points:
                goal_distance = abs(box.x - goal.x) + abs(box.y - goal.y)
                total_distance = player_distance + goal_distance
                if min_distance is None or min_distance > total_distance:
                    min_distance = total_distance
        return min_distance
