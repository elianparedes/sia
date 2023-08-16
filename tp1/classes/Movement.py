from enum import Enum


class Movement(Enum):

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
            Movement.TOP: (Movement.LEFT, Movement.RIGHT),
            Movement.RIGHT: (Movement.TOP, Movement.BOTTOM),
            Movement.BOTTOM: (Movement.LEFT, Movement.RIGHT),
            Movement.LEFT: (Movement.TOP, Movement.BOTTOM)
        }.get(self)
