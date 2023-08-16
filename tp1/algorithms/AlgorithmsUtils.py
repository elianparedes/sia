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
            for goal in state.goals_points:
                total_distance += abs(box.x - goal.x) + abs(box.y - goal.y)
        return total_distance
