from classes.Point import Point

from classes.Direction import Direction


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
            '+': 'player_on_goal',
            ' ': 'blank'
        }

        rows = board.split('\n')
        matrix = [list(row.rstrip()) for row in rows]

        positions = {
            'wall': [],
            'player': [],
            'goal': [],
            'box': [],
            'blank': []
        }

        for row_idx in range(len(matrix)):
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

        return positions

    @staticmethod
    def get_deadlocks(walls, blanks):
        deadlocks = []
        for blank in blanks:
            if SokobanUtils.is_deadlock(blank, walls):
                deadlocks.append(blank)
        return deadlocks

    @staticmethod
    def is_deadlock(blank, walls):
        if SokobanUtils.is_corner_deadlock(blank, walls):
            return True
        if SokobanUtils.is_wall_deadlock(blank, walls):
            return True
        return False

    # TODO: implement if necessary
    @staticmethod
    def is_wall_deadlock(blank, walls):
        return False

    @staticmethod
    def is_corner_deadlock(blank, walls):
        if blank.move(Direction.TOP) in walls:
            if blank.move(Direction.LEFT) in walls:
                return True
            if blank.move(Direction.RIGHT) in walls:
                return True
        if blank.move(Direction.BOTTOM) in walls:
            if blank.move(Direction.LEFT) in walls:
                return True
            if blank.move(Direction.RIGHT) in walls:
                return True
        return False
