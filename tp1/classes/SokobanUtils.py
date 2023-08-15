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

        rows = board.split('\n')
        matrix = [list(row.rstrip()) for row in rows]
        matrix = matrix[1:-1]

        positions = {
            'wall': [],
            'player': [],
            'goal': [],
            'box': [],
        }

        for row_idx in range(len(matrix)):
            print(row_idx)
            for col_idx in range(len(matrix[row_idx])):
                cell = matrix[row_idx][col_idx]
                if cell in objects:
                    object_type = objects[cell]
                    positions.setdefault(object_type, []).append(Point(row_idx, col_idx))
                    if object_type == 'box_on_goal':
                        positions.setdefault('box', []).append(Point(row_idx, col_idx))
                        positions.setdefault('goal', []).append(Point(row_idx, col_idx))
                    elif object_type == 'player_on_goal':
                        positions.setdefault('goal', []).append(Point(row_idx, col_idx))
                else:
                    print("Position (%d, %d) does not correspond to an object." % (row_idx, col_idx))

        return positions
