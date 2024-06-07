# File      :   main.py
# Author    :   Maxence Carignan
# Date      :   2024-06-07
# Function  :   Main file

from time import sleep
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
    sleep(0.05)
    grid.update()


    for event in pygame.event.get():
        match event.type:

            case pygame.QUIT:
                running = False

            case pygame.KEYDOWN:
                grid.update()

            case default:
                pass

pygame.quit()
exit(0)