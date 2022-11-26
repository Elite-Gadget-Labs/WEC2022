# -------- Importing libraries and dependencies -----------
import pygame
from Cell import Cell, CELL_WIDTH

# -------- Defining useful constants -----------
# Colors
GREY = (20, 20, 20)


# -------- Creating a template (known as a class) for each maze cell -----------
class Grid:
    def __init__(self, screen, rows, cols):
        self.stack = []
        self.screen = screen
        self.rows = rows
        self.cols = cols
        self.solution = {}
        self.grid = []

        for y in range(rows):
            self.grid.append([])
            for x in range(cols):
                self.grid[y].append(Cell(self.screen, self.grid, self.cols, self.rows, x, y))

        self.current_cell = self.grid[0][0]
        self.next_cell = self.grid[0][0]

        # self.current_cell = self.grid  # start the cursor at the top left cell
        # self.next_cell = self.grid[0][0]

    def init_maze(self):
        # -------- Initializing an Empty Maze -----------
        for y in range(self.rows):
            self.grid.append([])
            for x in range(self.cols):
                self.grid[y].append(Cell(self.screen, self.grid, self.cols, self.rows, x, y))

    def removeWalls(self):
        x = int(self.current_cell.x / CELL_WIDTH) - int(self.next_cell.x / CELL_WIDTH)
        y = int(self.current_cell.y / CELL_WIDTH) - int(self.next_cell.y / CELL_WIDTH)
        if x == -1:  # right of current
            self.current_cell.walls[1] = False
            self.next_cell.walls[3] = False
            self.solution[
                self.next_cell.x + CELL_WIDTH,
                self.next_cell.y
            ] = (self.current_cell.x, self.current_cell.y)
        elif x == 1:  # left of current
            self.current_cell.walls[3] = False
            self.next_cell.walls[1] = False
            self.solution[
                self.next_cell.x - CELL_WIDTH,
                self.next_cell.y
            ] = (self.current_cell.x, self.current_cell.y)
        elif y == -1:  # bottom of current
            self.current_cell.walls[2] = False
            self.next_cell.walls[0] = False
            self.solution[
                self.next_cell.x,
                self.next_cell.y + CELL_WIDTH
            ] = (self.current_cell.x, self.current_cell.y)
        elif y == 1:  # top of current
            self.current_cell.walls[0] = False
            self.next_cell.walls[2] = False
            self.solution[
                self.next_cell.x,
                self.next_cell.y - CELL_WIDTH
            ] = (self.current_cell.x, self.current_cell.y)
