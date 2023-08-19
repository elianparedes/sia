from heuristics.HeuristicABC import HeuristicABC


class ManhattanDistance(HeuristicABC):
    @classmethod
    def calculate(cls, state) -> int:
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
