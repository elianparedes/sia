from enum import Enum


class Direction(Enum):
    TOP = (-1, 0)
    RIGHT = (0, 1)
    BOTTOM = (1, 0)
    LEFT = (0, -1)

