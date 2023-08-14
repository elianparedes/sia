class State:
    def __init__(self, boxes_points, walls_points, player_point, goals_points):
        self.walls_points = walls_points
        self.player_point = player_point
        self.goals_points = goals_points
        self.boxes_points = boxes_points

    def __hash__(self):
        return hash((self.walls_points, self.player_point, self.goals_points, self.boxes_points))


    def __eq__(self, other):
        return self.walls_points == other.walls_points and self.player_point == other.player_point and self.goals_points == other.goals_points and self.boxes_points == other.boxes_points

#TODO: Implement, check boxes and walls
    def can_move(self, direction):

#TODO: Implement
    def has_deadlocks(self):
        return False

#TODO: Implement
    def move(self, direction):
        return False