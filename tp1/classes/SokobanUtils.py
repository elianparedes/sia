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

        positions = {
            'wall': [],
            'player': [],
            'goal': [],
            'box': [],
        }

        for row_idx, row in enumerate(matrix):
            for col_idx, cell in enumerate(row):
                if cell in objects:
                    object_type = objects[cell]
                    positions.setdefault(object_type, []).append(Point(row_idx, col_idx))
                    if object_type == 'box_on_goal':
                        positions.setdefault('box', []).append(Point(row_idx, col_idx))
                        positions.setdefault('goal', []).append(Point(row_idx, col_idx))
                    elif object_type == 'player_on_goal':
                        positions.setdefault('goal', []).append(Point(row_idx, col_idx))

        return positions
