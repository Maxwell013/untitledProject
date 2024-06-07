
### SCREEN
SCREEN_WIDTH = 1800
SCREEN_HEIGHT = 900

CELL_SIZE = 300
CELL_BORDER = 10
###
CELL_COLUMNS = SCREEN_WIDTH // CELL_SIZE
CELL_ROWS = SCREEN_HEIGHT // CELL_SIZE

CELL_OFFSET_X = SCREEN_WIDTH % CELL_SIZE / 2
CELL_OFFSET_Y = SCREEN_HEIGHT % CELL_SIZE / 2

### COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


if __name__ == "__main__":
    print(CELL_COLUMNS, CELL_ROWS)
    print(CELL_OFFSET_X, CELL_OFFSET_Y)