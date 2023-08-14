from collections import defaultdict
class BFS:
    @staticmethod
    def bfs(initial_state):
        visited = []
        queue = []
        queue.append(initial_state)
        while queue:
            state = queue.pop(0)
            if state.is_solution():
                print("Solutionnnn")
                return state
            if state not in visited:
                visited.append(state)
                for child in state.get_children():
                    queue.append(child)
        return None
