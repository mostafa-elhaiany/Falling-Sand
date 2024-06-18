import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = (10, 10)  # Width and height of each cell
GRID_DIMS = (50, 50)  # Number of rows and columns

# Calculate screen dimensions
SCREEN_WIDTH = CELL_SIZE[0] * GRID_DIMS[1]
SCREEN_HEIGHT = CELL_SIZE[1] * GRID_DIMS[0]
SCREEN_DIMS = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SAND = (194, 178, 128) 

# Initialize screen
screen = pygame.display.set_mode(SCREEN_DIMS)
pygame.display.set_caption('Falling Sand Simulation')


# Initialize grid state
sand_grid = [[BLACK for _ in range(GRID_DIMS[1])] for _ in range(GRID_DIMS[0])]

def draw_grid(screen, cell_size, grid_dims):
    for row in range(grid_dims[0]):
        for col in range(grid_dims[1]):
            rect = pygame.Rect(col * cell_size[0], row * cell_size[1], cell_size[0], cell_size[1])
            # pygame.draw.rect(screen, WHITE, rect, 1)
            pygame.draw.rect(screen, sand_grid[row][col], rect)

def handle_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        col = x // CELL_SIZE[0]
        row = y // CELL_SIZE[1]
        if 0 <= row < GRID_DIMS[0] and 0 <= col < GRID_DIMS[1]:
            sand_grid[row][col] = SAND


def main():
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                handle_event(event)

        # Fill screen with black
        screen.fill(BLACK)
        
        # Draw grid
        draw_grid(screen, CELL_SIZE, GRID_DIMS)
        
        # Update display
        pygame.display.flip()
        
        # Cap the frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
