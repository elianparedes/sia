class StateBuilder:
    def __init__(self, width, height):
        self.grid = [[' ' for _ in range(height)] for _ in range(width)]

    def add_points(self, points, char):
        for point in points:
            self.grid[point.x][point.y] = char
        return self

    def build(self):
        return self.grid

    def __str__(self):
        return '\n'.join(''.join(row) for row in self.grid)

    def print_grid(self):
        for row in self.grid:
            print(''.join(row))
