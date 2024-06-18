import pygame
import sys
import random
# Initialize Pygame
pygame.init()

# Constants
CELL_SIZE = (5, 5)  # Width and height of each cell
GRID_DIMS = (100, 70)  # Number of rows and columns

click_range = 4

# Calculate screen dimensions
SCREEN_WIDTH = CELL_SIZE[0] * GRID_DIMS[1]
SCREEN_HEIGHT = CELL_SIZE[1] * GRID_DIMS[0]
SCREEN_DIMS = (SCREEN_WIDTH, SCREEN_HEIGHT)
print(SCREEN_DIMS)
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SAND = (194, 178, 128) 

# Initialize screen
screen = pygame.display.set_mode(SCREEN_DIMS)
pygame.display.set_caption('Falling Sand Simulation')


mouse_dragging = False

# Initialize grid state
sand_grid = [[BLACK for _ in range(GRID_DIMS[1])] for _ in range(GRID_DIMS[0])]

def draw_grid(screen, cell_size, grid_dims):
    for row in range(grid_dims[0]):
        for col in range(grid_dims[1]):
            rect = pygame.Rect(col * cell_size[0], row * cell_size[1], cell_size[0], cell_size[1])
            pygame.draw.rect(screen, sand_grid[row][col], rect)


def add_sand_color():
    rand_value = random.randint(-5,5)
    sand = [s+rand_value for s in SAND ]
    return sand

def handle_event(event):
    global mouse_dragging
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_dragging = True
        x, y = event.pos
        center_col = x // CELL_SIZE[0]
        center_row = y // CELL_SIZE[1]
        for r_dif in range(-click_range, click_range, 1):
            row = center_row+r_dif
            for c_dif in range(-click_range, click_range, 1):
                col = center_col+c_dif
                if 0 <= row < GRID_DIMS[0] and 0 <= col < GRID_DIMS[1] and random.random()>0.5:
                    sand_grid[row][col] = add_sand_color()
    elif event.type == pygame.MOUSEBUTTONUP:
        mouse_dragging = False
    elif event.type == pygame.MOUSEMOTION and mouse_dragging:
        x, y = event.pos
        center_col = x // CELL_SIZE[0]
        center_row = y // CELL_SIZE[1]
        for r_dif in range(-click_range, click_range, 1):
            row = center_row+r_dif
            for c_dif in range(-click_range, click_range, 1):
                col = center_col+c_dif
                if 0 <= row < GRID_DIMS[0] and 0 <= col < GRID_DIMS[1] and random.random()>0.5:
                    sand_grid[row][col] = add_sand_color()



def update_grid():
    new_grid  = [[BLACK for _ in range(GRID_DIMS[1])] for _ in range(GRID_DIMS[0])]

    for row in range(GRID_DIMS[0]):
        for col in range(GRID_DIMS[1]):
            current_state = sand_grid[row][col]
            if(current_state!=BLACK):
                if(row+1<GRID_DIMS[0]):
                    below = sand_grid[row+1][col]
                    if(below == BLACK):
                        new_grid[row+1][col] = current_state
                    else:
                        if(col-1>=0 and col+1<GRID_DIMS[1]):
                            down_left = sand_grid[row+1][col-1]
                            down_right = sand_grid[row+1][col+1]
                            if(down_left==BLACK and down_right==BLACK):
                                if(random.random()>.5):
                                    new_grid[row+1][col-1] = current_state
                                else:
                                    new_grid[row+1][col+1] = current_state
                            elif(down_left==BLACK):
                                new_grid[row+1][col-1] = current_state
                            elif(down_right==BLACK):
                                new_grid[row+1][col+1] = current_state
                            else:
                                new_grid[row][col] = current_state
                        elif(col-1<0):
                            down_right = sand_grid[row+1][col+1]
                            if(down_right==BLACK):
                                new_grid[row+1][col+1] = current_state
                            else:
                                new_grid[row][col] = current_state
                        else:
                            down_left = sand_grid[row+1][col-1]
                            if(down_left==BLACK):
                                new_grid[row+1][col-1] = current_state
                            else:
                                new_grid[row][col] = current_state
                else:
                    new_grid[row][col] = current_state

    return new_grid

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
        screen.fill(BLACK)
        
        # Draw grid
        draw_grid(screen, CELL_SIZE, GRID_DIMS)
        
        # Update display
        pygame.display.flip()
        
        sand_grid = update_grid()
        # Cap the frame rate
        clock.tick(60)

if __name__ == '__main__':
    main()
