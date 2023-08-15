from classes.Direction import Direction
from classes.StateUtils import StateUtils


class State:
    def __init__(self, boxes_points, walls_points, player_point, goals_points, deadlocks_points):
        self.walls_points = walls_points
        self.player_point = player_point
        self.goals_points = goals_points
        self.boxes_points = boxes_points
        self.deadlocks_points = deadlocks_points

    def __str__(self):
        object_symbols = {
            'wall': '#',
            'player': '@',
            'goal': '.',
            'box': '$',
            'box_on_goal': '*',
            'player_on_goal': '+'
        }

        all_points = [
            self.player_point,
            *self.boxes_points,
            *self.walls_points,
            *self.goals_points,
            *self.deadlocks_points
        ]

        max_row = max(point.x for point in all_points)
        max_col = max(point.y for point in all_points)

        matrix = [[' '] * (max_col + 1) for _ in range(max_row + 1)]

        for point in self.walls_points:
            matrix[point.x][point.y] = object_symbols['wall']

        for point in self.goals_points:
            matrix[point.x][point.y] = object_symbols['goal']

        for point in self.deadlocks_points:
            matrix[point.x][point.y] = object_symbols['wall']

        for point in self.boxes_points:
            if point in self.goals_points:
                matrix[point.x][point.y] = object_symbols['box_on_goal']
            else:
                matrix[point.x][point.y] = object_symbols['box']

        if self.player_point in self.goals_points:
            matrix[self.player_point.x][self.player_point.y] = object_symbols['player_on_goal']
        else:
            matrix[self.player_point.x][self.player_point.y] = object_symbols['player']

        return '\n'.join([''.join(row) for row in matrix])

    def __hash__(self):
        # Combine the hash values of the attributes
        hash_tuple = (
            tuple(self.boxes_points),
            tuple(self.walls_points),
            self.player_point,
            tuple(self.goals_points),
        )
        return hash(hash_tuple)

    def __eq__(self, other):
        return self.walls_points == other.walls_points and self.player_point == other.player_point and self.goals_points == other.goals_points and self.boxes_points == other.boxes_points

    def can_continue_search(self, direction):
        return self.can_move(direction)  # and not self.has_deadlocks(direction)

    def can_move(self, direction):
        next_point = self.player_point.move(direction)
        if next_point in self.walls_points:
            return False
        if next_point in self.boxes_points:
            next_box_point = next_point.move(direction)
            if next_box_point in self.walls_points or next_box_point in self.boxes_points:
                return False
        return True

    def has_deadlocks(self, point):
        return point in self.deadlocks_points

    def move(self, direction):
        if self.is_solution():
            print("Solution found :D")
            return

        if self.can_continue_search(direction):
            next_point = self.player_point.move(direction)
            if next_point in self.boxes_points:
                next_box_point = next_point.move(direction)
                new_boxes_points = self.boxes_points.copy()
                new_boxes_points.remove(next_point)
                new_boxes_points.add(next_box_point)
                return State(new_boxes_points, self.walls_points, next_point, self.goals_points, self.deadlocks_points)
            return State(self.boxes_points, self.walls_points, next_point, self.goals_points, self.deadlocks_points)

    def get_children(self):
        children = []
        for direction in Direction:
            if self.can_continue_search(direction):
                children.append(self.move(direction))
        return children

    def is_solution(self):
        return self.boxes_points.issubset(self.goals_points)
