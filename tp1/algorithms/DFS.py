from collections import deque

from classes.Node import Node
from classes.StateUtils import StateUtils


class DFS:
    @staticmethod
    def dfs(initial_state):
        size = 0
        visited = set()
        stack = deque()
        root = Node(None, initial_state)
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.state.is_solution():
                print("Solution found opening ", size, " nodes using DFS")
                StateUtils.draw_solution(node, 0)
                return node.state
            if node not in visited:
                visited.add(node)
                for child in node.get_children():
                    stack.append(child)
            size += 1
        return None
