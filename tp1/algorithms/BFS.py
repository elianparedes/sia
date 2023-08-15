from tp1.classes.Node import Node
from tp1.classes.StateUtils import StateUtils


class BFS:
    @staticmethod
    def bfs(initial_state):
        steps = 0
        visited = []
        queue = []
        root = Node(None, initial_state)
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.state.is_solution():
                print("Solution found in ", steps, " steps using BFS")
                StateUtils.draw_solution(node, 0)
                return node.state
            if node not in visited:
                visited.append(node)
                for child in node.get_children():
                    queue.append(child)
            steps += 1
        return None
