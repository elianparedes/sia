from src.heuristics.HeuristicABC import HeuristicABC


class MinDistance(HeuristicABC):
    @classmethod
    def calculate(cls, state) -> int:
        min_distance = None
        for box in state.boxes_points:
            player_distance = abs(box.x - state.player_point.x) + abs(box.y - state.player_point.y)
            for goal in state.goals_points:
                goal_distance = abs(box.x - goal.x) + abs(box.y - goal.y)
                total_distance = player_distance + goal_distance
                if min_distance is None or min_distance > total_distance:
                    min_distance = total_distance
        return min_distance
