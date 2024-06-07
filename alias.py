from enum import Enum

Color = tuple[int, int, int]
Position = tuple[int, int]


class CellType(Enum):

    EMPTY = 0
    FILLED = 1