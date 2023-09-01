from src.heuristics.HeuristicABC import HeuristicABC


class ManhattanDistance(HeuristicABC):
    @classmethod
    def calculate(cls, state) -> int:
        total_distance = 0
        min_for_a_box  = None
        for box in state.boxes_points:
            min_for_box = None
            if min_for_a_box is None:
                min_for_a_box = abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y)
            if min_for_a_box > abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y):
                min_for_a_box = abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y)
            for goal in state.goals_points:
                if min_for_box is None:
                    min_for_box = abs(box.x - goal.x) + abs(box.y - goal.y)
                if min_for_box > abs(box.x - goal.x) + abs(box.y - goal.y):
                    min_for_box = abs(box.x - goal.x) + abs(box.y - goal.y)
            total_distance += min_for_box
        return total_distance + min_for_a_box
