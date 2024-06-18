import config
import random 

def make_grid(value, w, h):
    return  [[value]*h for _ in range(w)]


def within_bounds(x,y):
    height_constraint = y>=0 and y<config.GRID_DIMS[0]
    width_constraint = x>=0 and x<config.GRID_DIMS[1]

    return width_constraint and height_constraint


def add_sand_color():
    rand_value = random.randint(-5,5)
    sand = [s+rand_value for s in config.SAND]
    return sand

def update_grid(sand_grid):
    new_grid = make_grid(config.BLACK, config.GRID_DIMS[0], config.GRID_DIMS[1])
    for row in range(config.GRID_DIMS[0]):
        for col in range(config.GRID_DIMS[1]):
            current_state = sand_grid[row][col]
            if(current_state!=config.BLACK):
                if(not within_bounds(col, row+1)):
                    new_grid[row][col] = current_state
                else:
                    below = sand_grid[row+1][col]
                    if(below==config.BLACK):
                        new_grid[row+1][col] = current_state
                    else:
                        proba = -1 # if -1 means stay in place
                        if(within_bounds(col-1, row+1) and within_bounds(col+1,row+1)):
                            down_left = sand_grid[row+1][col-1]
                            down_right = sand_grid[row+1][col+1]
                            if(down_left == config.BLACK and down_right == config.BLACK):
                                proba = .5 # 50 50 on which way to go
                            elif (down_left == config.BLACK):
                                proba = 0
                            elif(down_right == config.BLACK):
                                proba = 1
                        elif(within_bounds(col-1, row+1)):
                            down_left = sand_grid[row+1][col-1]
                            if(down_left == config.BLACK):
                                proba = 0
                        elif(within_bounds(col+1,row+1)):
                            down_right = sand_grid[row+1][col+1]
                            if(down_right == config.BLACK):
                                proba = 1
                        if(proba == -1):
                            new_grid[row][col] = current_state
                        elif(random.random()>proba):
                            new_grid[row+1][col-1] = current_state
                        else:
                            new_grid[row+1][col+1] = current_state

    return new_grid