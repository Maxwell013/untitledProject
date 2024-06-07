import pygame

from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from grid import Grid
from render import render

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
grid = Grid()
pygame.display.set_caption("Untitled Python Project")

running = True

while running:

    render(grid, screen)

    for event in pygame.event.get():
        match event.type:

            case pygame.QUIT:
                running = False

            case default:
                pass

pygame.quit()
exit(0)