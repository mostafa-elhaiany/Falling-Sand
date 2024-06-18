# Constants
CELL_SIZE = (2, 2)  # Width and height of each cell
GRID_DIMS = (200, 150)  # Number of rows and columns
CLICK_RANGE = 5

ACCELERATION = 1
ACCELERATION_RANDOMNESS = 2 # plus range from original accelaration
# Calculate screen dimensions
SCREEN_WIDTH = CELL_SIZE[0] * GRID_DIMS[1]
SCREEN_HEIGHT = CELL_SIZE[1] * GRID_DIMS[0]
SCREEN_DIMS = (SCREEN_WIDTH, SCREEN_HEIGHT)
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SAND = (194, 178, 128) 
