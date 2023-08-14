from classes.Point import Point


class SokobanUtils:
    def __init__(self):
        raise NotImplementedError("Class instantiation not supported")

    @staticmethod
    def parse_sokoban_board(board):
        objects = {
            '#': 'wall',
            '@': 'player',
            '.': 'goal',
            '$': 'box',
            '*': 'box_on_goal',
            '+': 'player_on_goal'
        }

        rows = board.strip().split('\n')
        matrix = [list(row) for row in rows]

        positions = {}

        for row_idx, row in enumerate(matrix):
            for col_idx, cell in enumerate(row):
                if cell in objects:
                    object_type = objects[cell]
                    positions.setdefault(object_type, []).append((Point(row_idx, col_idx)))

        return positions
