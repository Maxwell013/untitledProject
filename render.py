# File      :   render.py
# Author    :   Maxence Carignan
# Date      :   2024-06-07
# Function  :   Rendering the grid data

import pygame
from pygame import Surface

from grid import Grid
from consts import *
from alias import *

def render(grid: Grid, screen: Surface) -> None:

    for x in range(len(grid.cells)):

        for y in range(len(grid.cells[x])):

            cell = grid.getCell((x, y))
            drawCell(screen, cell, (x, y))

    pygame.display.update()

def drawCell(screen: Surface, cell: CellType, pos: Position) -> None:

    x = CELL_OFFSET_X + CELL_SIZE * (pos[0] + 0)
    y = CELL_OFFSET_Y + CELL_SIZE * (pos[1] + 0)

    rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    
    match cell:
        case CellType.EMPTY:
            color = WHITE
        case CellType.FILLED:
            color = BLACK
    
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, CELL_BORDER)
