import pygame
import sys
import random
import config
import utils
from Sand import Sand

# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode(config.SCREEN_DIMS)
pygame.display.set_caption('Falling Sand Simulation')

mouse_dragging = False

# Initialize grid state
sand_grid = utils.make_grid(config.BLACK, config.GRID_DIMS[0], config.GRID_DIMS[1])
sand = []

def draw_grid(screen, cell_size):
    for s in sand:
        rect = pygame.Rect(s.x * cell_size[0], s.y * cell_size[1], cell_size[0], cell_size[1])
        pygame.draw.rect(screen, sand_grid[s.y][s.x], rect)

def create_sand_around_point(x, y):
    global sand
    center_col = x // config.CELL_SIZE[0]
    center_row = y // config.CELL_SIZE[1]
    if(config.CLICK_RANGE>0):
        for r_dif in range(-config.CLICK_RANGE, config.CLICK_RANGE, 1):
            row = center_row+r_dif
            for c_dif in range(-config.CLICK_RANGE, config.CLICK_RANGE, 1):
                col = center_col+c_dif
                if 0 <= row < config.GRID_DIMS[0] and 0 <= col < config.GRID_DIMS[1] and random.random()>0.5:
                    sand.append(Sand(col, row))
                    sand_grid[row][col] = utils.add_sand_color()
    else:
        sand.append(Sand(center_col, center_row))
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

        # draw grid        
        draw_grid(screen, config.CELL_SIZE)

        # Update display
        pygame.display.flip()
    
        # update particles
        sand_grid = utils.update_sand(sand, sand_grid)

        # Cap the frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
