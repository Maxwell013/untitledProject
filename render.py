import pygame
from pygame import Surface

from grid import Grid
from consts import *

Color = tuple[int, int, int]
Position = tuple[int, int]

def render(grid: Grid, screen: Surface) -> None:

    for x in range(len(grid.cells)):

        for y in range(len(grid.cells[x])):
            drawCell(screen, WHITE, (x, y))

    pygame.display.update()

def drawCell(screen: Surface, color: Color, pos: Position) -> None:

    x = CELL_OFFSET_X + CELL_SIZE * (pos[0] + 0)
    y = CELL_OFFSET_Y + CELL_SIZE * (pos[1] + 0)

    cell = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    
    pygame.draw.rect(screen, color, cell)
    pygame.draw.rect(screen, BLACK, cell, CELL_BORDER)
