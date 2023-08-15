from classes.Direction import Direction
from classes.StateUtils import StateUtils


class State:
    def __init__(self, boxes_points, walls_points, player_point, goals_points, deadlocks_points):
        self.walls_points = walls_points
        self.player_point = player_point
        self.goals_points = goals_points
        self.boxes_points = boxes_points
        self.deadlocks_points = deadlocks_points

    def __hash__(self):
        return hash((self.walls_points, self.player_point, self.goals_points, self.boxes_points))

    def __eq__(self, other):
        return self.walls_points == other.walls_points and self.player_point == other.player_point and self.goals_points == other.goals_points and self.boxes_points == other.boxes_points

    def can_continue_search(self, direction):
        return self.can_move(direction) and not self.has_deadlocks(direction)

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
                new_boxes_points.append(next_box_point)
                return State(new_boxes_points, self.walls_points, next_point, self.goals_points, self.deadlocks_points)
            return State(self.boxes_points, self.walls_points, next_point, self.goals_points, self.deadlocks_points)

    def get_children(self):
        children = []
        for direction in Direction:
            if self.can_continue_search(direction):
                children.append(self.move(direction))
        return children

    def is_solution(self):
        return set(self.boxes_points).issubset(set(self.goals_points))
