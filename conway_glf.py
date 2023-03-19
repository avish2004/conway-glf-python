#by Aditya Vishwakarma

import pygame
import numpy as np

# initialize Pygame
pygame.init()

# set up display
width, height = 800, 800
screen = pygame.display.set_mode((height, width))

# set up colors
BLACK = 0, 0, 0
WHITE = 255, 255, 255

# create grid
grid = np.zeros((height, width))

# set up initial state
grid[300:305, 400:405] = np.array([[0, 0, 1, 0, 0],
                                    [0, 0, 0, 1, 0],
                                    [0, 1, 1, 1, 0],
                                    [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0]])

# main game loop
while True:

    # clear screen
    screen.fill(BLACK)

    # create copy of grid for updating
    new_grid = np.copy(grid)

    # iterate over each cell in the grid
    for i in range(height):
        for j in range(width):
            
            # compute number of live neighbors
            num_neighbors = np.sum(grid[max(0, i-1):min(height, i+2), 
                                         max(0, j-1):min(width, j+2)]) - grid[i, j]

            # update cell based on rules of the game 
            if grid[i, j] == 1 and (num_neighbors < 2 or num_neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and num_neighbors == 3:
                new_grid[i, j] = 1

            # draw cell
            if new_grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (j, i, 1, 1))

    # update grid
    grid = new_grid

    # update display
    pygame.display.flip()

    # check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

