from enum import Enum


class Direction(Enum):
    TOP = (-1, 0)
    RIGHT = (0, 1)
    BOTTOM = (1, 0)
    LEFT = (0, -1)
    TOP_LEFT = (-1, -1)
    TOP_RIGHT = (-1, 1)
    BOTTOM_LEFT = (1, -1)
    BOTTOM_RIGHT = (1, 1)

    @property
    def orthogonal(self):
        return {
            Direction.TOP: (Direction.LEFT, Direction.RIGHT),
            Direction.RIGHT: (Direction.TOP, Direction.BOTTOM),
            Direction.BOTTOM: (Direction.LEFT, Direction.RIGHT),
            Direction.LEFT: (Direction.TOP, Direction.BOTTOM)
        }.get(self)


