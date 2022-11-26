# -------- Importing libraries and dependencies -----------
import pygame
import random

# -------- Defining useful constants -----------
# Colors
WHITE = (255, 255, 255)
GREY = (20, 20, 20)
BLACK = (0, 0, 0)
PURPLE = (100, 0, 100)
BLUE = (0, 0, 255)

# Cell dimensions (pixels)
CELL_WIDTH = 75


# -------- Creating a template (known as a class) for each maze cell -----------
class Cell:
    def __init__(self, screen, grid, cols, rows, x, y):  # Cell class is initialized with width, height
        global CELL_WIDTH
        # cell dimensions
        self.x = x * CELL_WIDTH
        self.y = y * CELL_WIDTH
        self.screen = screen
        self.cols = cols
        self.rows = rows
        self.grid = grid

        self.visited = False  # Indicates if cell has already been drawn in maze
        self.current = False  # Indicates whether the cell is currently selected (shown as red)

        # Indicates the existence of walls to the top, right, bottom, and left of the cell
        self.walls = [True, True, True, True]

        # neighbors
        self.neighbors = []

        self.top = 0
        self.right = 0
        self.bottom = 0
        self.left = 0

        self.next_cell = 0

    # Function to draw cell on maze screen based on its walls, colors, and maze position
    def draw(self):
        if self.current:  # If cell is currently selected, color it red
            pygame.draw.rect(self.screen, BLUE, (self.x, self.y, CELL_WIDTH, CELL_WIDTH))
        elif self.visited:  # If cell has been previously selected, color it white
            pygame.draw.rect(self.screen, WHITE, (self.x, self.y, CELL_WIDTH, CELL_WIDTH))

            # Draw the walls (colored black) of the cell if they exist
            if self.walls[0]:  # top
                pygame.draw.line(self.screen, PURPLE, (self.x, self.y), ((self.x + CELL_WIDTH), self.y), 1)
            if self.walls[1]:  # right
                pygame.draw.line(self.screen, PURPLE, ((self.x + CELL_WIDTH), self.y),
                                 ((self.x + CELL_WIDTH), (self.y + CELL_WIDTH)), 1)
            if self.walls[2]:  # bottom
                pygame.draw.line(self.screen, PURPLE, ((self.x + CELL_WIDTH), (self.y + CELL_WIDTH)),
                                 (self.x, (self.y + CELL_WIDTH)), 1)
            if self.walls[3]:  # left
                pygame.draw.line(self.screen, PURPLE, (self.x, (self.y + CELL_WIDTH)), (self.x, self.y), 1)

    def findNeighborCells(self):
        # Indicate which neighboring cells are valid (within the maze boundaries)
        if int(self.y / CELL_WIDTH) - 1 >= 0:  # check above
            self.top = self.grid[int(self.y / CELL_WIDTH) - 1][int(self.x / CELL_WIDTH)]
        if int(self.x / CELL_WIDTH) + 1 <= self.cols - 1:  # check right
            self.right = self.grid[int(self.y / CELL_WIDTH)][int(self.x / CELL_WIDTH) + 1]
        if int(self.y / CELL_WIDTH) + 1 <= self.rows - 1:  # check below
            self.bottom = self.grid[int(self.y / CELL_WIDTH) + 1][int(self.x / CELL_WIDTH)]
        if int(self.x / CELL_WIDTH) - 1 >= 0:  # check left
            self.left = self.grid[int(self.y / CELL_WIDTH)][int(self.x / CELL_WIDTH) - 1]

        # If the neighboring cells exist and have not already been visited, add to the cell's neighbors list
        if self.top != 0:
            if not self.top.visited:
                self.neighbors.append(self.top)
        if self.right != 0:
            if not self.right.visited:
                self.neighbors.append(self.right)
        if self.bottom != 0:
            if not self.bottom.visited:
                self.neighbors.append(self.bottom)
        if self.left != 0:
            if not self.left.visited:
                self.neighbors.append(self.left)

        # If the
        if len(self.neighbors) > 0:
            self.next_cell = self.neighbors[random.randrange(0, len(self.neighbors))]
            return self.next_cell
        else:
            return False


