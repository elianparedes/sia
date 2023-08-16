from classes.Node import Node
from classes.StateUtils import StateUtils


class DFS:
    @staticmethod
    def dfs(initial_state):
        size = 0
        visited = []
        queue = []
        root = Node(None, initial_state)
        queue.append(root)
        while queue:
            node = queue.pop(-1)
            if node.state.is_solution():
                print("Solution found opening ", size, " nodes using DFS")
                StateUtils.draw_solution(node, 0)
                return node.state
            if node not in visited:
                visited.append(node)
                for child in node.get_children():
                    queue.append(child)
            size += 1
        return None
