# -------- Importing libraries and dependencies -----------
import pygame
import time
from Cell import Cell, CELL_WIDTH
from Grid import Grid
from pprint import pprint

# -------- Defining useful constants -----------
# Colors
GREY = (20, 20, 20)
PURPLE = (100, 0, 100)

# Screen dimensions (pixels)
SCREEN_SIZE = (750, 750)  # width, height
cols = int(SCREEN_SIZE[0] / CELL_WIDTH)
rows = int(SCREEN_SIZE[1] / CELL_WIDTH)

# -------- Defining and initializing game variables -----------
running = True
generate_done = False
clock = pygame.time.Clock()
grid = []

# -------- Initializing the Game environment -----------
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Maze Generator")


# -------- Defining Solution Functions -----------
def draw_solution_cell(x, y):
    offset = CELL_WIDTH//4
    width = CELL_WIDTH//2
    pygame.draw.rect(screen, PURPLE, (x + offset, y + offset, width, width), 0)
    pygame.display.update()


def plot_route_back(sol):
    x = (cols-1)*CELL_WIDTH
    y = (rows-1)*CELL_WIDTH

    draw_solution_cell(x, y)

    while (x, y) != (0, 0):
        x, y = sol[x, y]
        draw_solution_cell(x, y)
        time.sleep(0.1)


# -------- Main Game Loop -----------
# For every loop iteration, check for changes and draw the cells on the grid
# Keep running the game until 'running' is set to false

maze = Grid(screen, rows, cols) # creates an empty maze

while running:
    # stop the game if the user presses the game window's quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not generate_done:  # Keep drawing maze cells until 'generate_done' is True
        screen.fill(GREY)  # Fill the background grey

        # select the current cell and mark it as visited
        maze.current_cell.visited = True
        maze.current_cell.current = True

        #  Draw each cell in the grid
        for y in range(rows):
            for x in range(cols):
                maze.grid[y][x].draw()

        maze.next_cell = maze.current_cell.findNeighborCells() # select the next cell to draw

        # If there is a new cell to select, set it to current cell and create walls
        if maze.next_cell:
            maze.solution[maze.next_cell.x, maze.next_cell.y] = (maze.current_cell.x, maze.current_cell.y)

            maze.current_cell.neighbors = []

            maze.stack.append(maze.current_cell)

            maze.removeWalls()

            maze.current_cell.current = False

            maze.current_cell = maze.next_cell

        elif len(maze.stack) > 0:
            maze.current_cell.current = False
            maze.current_cell = maze.stack.pop()

        elif len(maze.stack) == 0:  # If the maze has rendered all cells, stop drawing
            generate_done = True
    else:  # If the maze has been generated, display the solution animation
        # pprint(maze.solution)
        plot_route_back(maze.solution)

    # Display the game screen
    pygame.display.flip()

    # frame rate per second
    clock.tick(60)

# When the loop is stopped ('running' = false), end the game
pygame.quit()
