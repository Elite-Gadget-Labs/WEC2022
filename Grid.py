# -------- Importing libraries and dependencies -----------
import pygame
from Cell import Cell, CELL_WIDTH


# -------- Creating a template (known as a class) for the Grid -----------
class Grid:
    def __init__(self, screen, rows, cols):
        self.stack = []
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.solution = {}
        self.grid = []

        # Initialize the grid array using the given columns and rows
        for y in range(rows):
            self.grid.append([])
            for x in range(cols):
                self.grid[y].append(Cell(self.screen, self.grid, self.cols, self.rows, x, y))

        self.current_cell = self.grid[0][0]  # Set the first selected cell to the top left
        self.next_cell = self.grid[0][0]

    def removeWalls(self):  # Function to remove walls between the current cell and the next cell
        x = int(self.current_cell.x / CELL_WIDTH) - int(self.next_cell.x / CELL_WIDTH)
        y = int(self.current_cell.y / CELL_WIDTH) - int(self.next_cell.y / CELL_WIDTH)
        if x == -1:  # right of current
            self.current_cell.walls[1] = False
            self.next_cell.walls[3] = False

        elif x == 1:  # left of current
            self.current_cell.walls[3] = False
            self.next_cell.walls[1] = False

        elif y == -1:  # bottom of current
            self.current_cell.walls[2] = False
            self.next_cell.walls[0] = False

        elif y == 1:  # top of current
            self.current_cell.walls[0] = False
            self.next_cell.walls[2] = False
