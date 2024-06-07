import pygame
from pygame import Surface

from grid import Grid
from consts import *

Color = tuple[int, int, int]
Position = tuple[int, int]

def render(grid: Grid, screen: Surface) -> None:
    
    screen.fill(GREEN)

    x = 0
    
    for column in grid.cells:
        y = 0
        for cell in column:
            drawCell(screen, WHITE, (x, y))

            y += 1
        x += 1

    pygame.display.update()

def drawCell(screen: Surface, color: Color, pos: Position) -> None:

    x = CELL_OFFSET_X + CELL_SIZE * (pos[0] + 0)
    y = CELL_OFFSET_Y + CELL_SIZE * (pos[1] + 0)

    cell = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
    
    pygame.draw.rect(screen, WHITE, cell)
    pygame.draw.rect(screen, BLACK, cell, CELL_BORDER)
