import itertools
from heuristics.HeuristicABC import HeuristicABC


class BipartiteHeuristic(HeuristicABC):
    @classmethod
    def calculate(cls, state) -> int:
        distances = []
        min_sum = float('inf')
        for box in state.boxes_points:
            distance = []
            for goal in state.goals_points:
                if box not in state.goals_points and goal not in state.boxes_points:
                    box_distance = abs(box.x - goal.x) + abs(box.y - goal.y)
                    box_distance += abs(state.player_point.x - box.x) + abs(state.player_point.y - box.y)
                    distance.append(box_distance)

            if len(distance) > 0:
                distances.append(distance)

        # We now find the minimum row-col combination by iterating over all possible scenarios
        for permutation in itertools.permutations(range(len(distances)), len(distances)):
            current_sum = sum(distances[row][col] for row, col in enumerate(permutation))
            min_sum = min(min_sum, current_sum)

        return min_sum
