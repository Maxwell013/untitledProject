# File      :   grid.py
# Author    :   Maxence Carignan
# Date      :   2024-06-07
# Function  :   Grid class

from consts import CELL_COLUMNS, CELL_ROWS
from alias import Position, CellType


class Grid:

    def __init__(self) -> None:

        self.cells = [[CellType.EMPTY for _ in range(CELL_ROWS)] for __ in range(CELL_COLUMNS)]
        
        # Hardcoded start
        self.setCell((1, 0), CellType.FILLED)
        self.setCell((0, 1), CellType.FILLED)
        self.setCell((1, 1), CellType.FILLED)
        self.setCell((1, 2), CellType.FILLED)
        self.setCell((2, 2), CellType.FILLED)

    def getCell(self, pos: Position) -> CellType:

        x = pos[0]
        y = pos[1]

        return self.cells[x][y]
    
    def setCell(self, pos: Position, cell_type: CellType) -> None:

        x = pos[0]
        y = pos[1]

        self.cells[x][y] = cell_type
    
    def checkCell(self, cell_pos: Position) -> bool:
        
        x = cell_pos[0] % CELL_COLUMNS
        y = cell_pos[1] % CELL_ROWS

        match self.getCell((x, y)):
            
            case CellType.EMPTY:
                return False

            case CellType.FILLED:
                return True

    def checkNeighbors(self, cell_pos: Position) -> int:

        neighbor_count = -1 * self.checkCell(cell_pos)

        for offset_x in range(-1, 2):

            for offset_y in range(-1, 2):
                
                x = cell_pos[0] + offset_x
                y = cell_pos[1] + offset_y
                
                neighbor_count += self.checkCell((x, y))
        
        return neighbor_count

    def update(self) -> None:

        new_cells = [column.copy() for column in self.cells]
        
        for x in range(len(self.cells)):

            for y in range(len(self.cells[x])):

                neighbors = self.checkNeighbors((x, y))

                if  not self.checkCell((x, y)): # Dead
                    if neighbors == 3: # Reproduction
                        new_cells[x][y] = CellType.FILLED

                elif neighbors < 2 or neighbors > 3: # Under/over-population
                    new_cells[x][y] = CellType.EMPTY

        self.cells = new_cells