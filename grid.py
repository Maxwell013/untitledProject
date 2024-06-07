from consts import CELL_COLUMNS, CELL_ROWS

class Grid:

    def __init__(self) -> None:
        
        column = [[0] * CELL_ROWS]
        self.cells = column * CELL_COLUMNS