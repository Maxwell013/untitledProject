from enum import Enum

from consts import CELL_COLUMNS, CELL_ROWS

class CellType(Enum):
    
    EMPTY = 0
    FILLED = 1

class Grid:

    def __init__(self) -> None:
        
        column = [[CellType.EMPTY] * CELL_ROWS]
        self.cells = column * CELL_COLUMNS