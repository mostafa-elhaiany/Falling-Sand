import pygame
import sys
import random
import config
import utils

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode(config.SCREEN_DIMS)
pygame.display.set_caption('Falling Sand Simulation')

mouse_dragging = False

# Initialize grid state
sand_grid = utils.make_grid(config.BLACK, config.GRID_DIMS[0], config.GRID_DIMS[1])

def draw_grid(screen, cell_size, grid_dims):
    for row in range(grid_dims[0]):
        for col in range(grid_dims[1]):
            rect = pygame.Rect(col * cell_size[0], row * cell_size[1], cell_size[0], cell_size[1])
            pygame.draw.rect(screen, sand_grid[row][col], rect)



def create_sand_around_point(x, y):
    center_col = x // config.CELL_SIZE[0]
    center_row = y // config.CELL_SIZE[1]
    if(config.CLICK_RANGE>0):
        for r_dif in range(-config.CLICK_RANGE, config.CLICK_RANGE, 1):
            row = center_row+r_dif
            for c_dif in range(-config.CLICK_RANGE, config.CLICK_RANGE, 1):
                col = center_col+c_dif
                if 0 <= row < config.GRID_DIMS[0] and 0 <= col < config.GRID_DIMS[1] and random.random()>0.5:
                    sand_grid[row][col] = utils.add_sand_color()
    else:
        sand_grid[center_row][center_col] = utils.add_sand_color()

def handle_event(event):
    global mouse_dragging
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_dragging = True
        x, y = event.pos
        create_sand_around_point(x,y)
    elif event.type == pygame.MOUSEBUTTONUP:
        mouse_dragging = False
    elif event.type == pygame.MOUSEMOTION and mouse_dragging:
        x, y = event.pos
        create_sand_around_point(x,y)


def main():
    global sand_grid
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                handle_event(event)

        # Fill screen with black
        screen.fill(config.BLACK)
        
        # Draw grid
        draw_grid(screen, config.CELL_SIZE, config.GRID_DIMS)
        
        # Update display
        pygame.display.flip()
        
        sand_grid = utils.update_grid(sand_grid)
        # Cap the frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
