# Manhattan distance between player and box + box and goal
# This only works with one box, remove later
def heuristic(state):
    player_point = state.player_point
    box_point = state.boxes_points[0]
    goal_point = state.goals_points[0]
    return abs(player_point.x - box_point.x) + abs(player_point.y - box_point.y) \
           + abs(box_point.x - goal_point.x) + abs(box_point.y - goal_point.y)

class LocalGreedy:
    @staticmethod
    def local_greedy(initial_state):
        steps = 0
        visited = []
        queue = []
        queue.append(initial_state)
        while queue:
            state = queue.pop(0)
            if state.is_solution():
                print("Solution found in ", steps, " steps using Local Greedy Search")
                return state
            if state not in visited:
                visited.append(state)
                for child in state.get_children():
                    queue.append(child)
            queue= sorted(queue, key=heuristic)
            steps += 1
        return None