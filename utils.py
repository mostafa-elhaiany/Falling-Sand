import config
import random 
from typing import List
from Sand import Sand
def make_grid(value, w, h):
    """
    Creates a 2D matrix to keep track of sand grains and their colours
    """
    return  [[value]*h for _ in range(w)]

def within_bounds(x,y):
    """
    Checks if a point x,y is within the canvas bounds (screen width, screen height)
    """
    height_constraint = y>=0 and y<config.GRID_DIMS[0]
    width_constraint = x>=0 and x<config.GRID_DIMS[1]
    return width_constraint and height_constraint

def add_sand_color():
    """
    Just for visuals sand colours are randomly generated based on a start colour
    """
    rand_value = random.randint(-5,5)
    sand = [s+rand_value for s in config.SAND]
    return sand

def update_sand(sand: List[Sand], sand_grid):
    """
    Updates all sand grains inside the list and updates the location on the matrix
    """
    new_grid = make_grid(config.BLACK, config.GRID_DIMS[0], config.GRID_DIMS[1])
    for s in sand:
        colour = sand_grid[s.y][s.x]
        s.update(sand_grid)
        new_grid[s.y][s.x] = colour
    return new_grid
