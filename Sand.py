import random
import utils, config

class Sand:
    """
    Sand class to keep track of every individual sand grain
    checking for dropped sand should be more optimized than checking the entire array every iteration
    """
    def __init__(self, x, y, a=1): 
        self.x = x # column
        self.y = y # row
        self.v = 0 # velocity 
        self.t = 1 # time step
        self. a = a # acceleration

    def print(self): # to string function 
        print("x:",self.x,"y:",self.y)

    def update(self, grid):
        """
        Update every individual sand grain with its individual velocity 
        """
        self.v += self.a * self.t
        final_y = int(self.y + self.v * self.t)
        new_y = self.y+1
        while new_y<=final_y: # checks if it should stop before the final destination
            if(utils.within_bounds(self.x,new_y)):
                below = grid[new_y][self.x]
                if(below == config.BLACK):
                    self.y = new_y
                    new_y+=1
                else:
                    proba = -1
                    if(utils.within_bounds(self.x-1, new_y) and utils.within_bounds(self.x+1,new_y)):
                        down_left = grid[new_y][self.x-1]
                        down_right = grid[new_y][self.x+1]
                        if(down_left == config.BLACK and down_right == config.BLACK):
                            proba = .5 # 50 50 on which way to go
                        elif (down_left == config.BLACK):
                            proba = 0
                        elif(down_right == config.BLACK):
                            proba = 1
                    elif(utils.within_bounds(self.x-1, new_y)):
                        down_left = grid[new_y][self.x-1]
                        if(down_left == config.BLACK):
                            proba = 0
                    elif(utils.within_bounds(self.x+1,new_y)):
                        down_right = grid[new_y][self.x+1]
                        if(down_right == config.BLACK):
                            proba = 1
                    if(proba!=-1):
                        if(random.random()>proba):
                            self.y = new_y
                            self.x -=1
                        else:                    
                            self.y = new_y
                            self.x +=1
                    break
            else:
                break
            
    