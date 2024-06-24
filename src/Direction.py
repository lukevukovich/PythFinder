from enum import Enum


class Direction(Enum):
    """
    An enumeration to represent the four cardinal directions.
    """

    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)
