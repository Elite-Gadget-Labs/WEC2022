# -------- Importing libraries and dependencies -----------
import pygame
import time
from Cell import Cell, CELL_WIDTH
from Grid import Grid
from pprint import pprint

# -------- Defining useful constants -----------
# Colors
GREY = (20, 20, 20)
BLUE = (0, 0, 255)
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
    pygame.draw.rect(screen, PURPLE, (
    x - CELL_WIDTH // 2 - CELL_WIDTH // 4, y - CELL_WIDTH // 2 - CELL_WIDTH // 4, CELL_WIDTH // 2, CELL_WIDTH // 2), 0)
    pygame.display.update()
    print("applepie")


def plot_route_back(sol):
    x = cols * CELL_WIDTH
    y = rows * CELL_WIDTH

    draw_solution_cell(x, y)

    '''
    while (x, y) != (0, 0):
        # print(x, y)
        x, y = sol[x, y]
        draw_solution_cell(x, y)
        time.sleep(0.1)'''


# -------- Main Game Loop -----------
# For every loop iteration, check for changes and draw the cells on the grid
# Keep running the game until 'running' is set to false

maze = Grid(screen, rows, cols)
maze.init_maze()

while running:
    # stop the game if the user presses the game window's quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not generate_done:
        # Fill the background grey to create an empty grid
        screen.fill(GREY)

        # select the current cell and mark it as visited
        maze.current_cell.visited = True
        maze.current_cell.current = True

        #  Draw each cell in the grid
        for y in range(rows):
            for x in range(cols):
                maze.grid[y][x].draw()

        maze.next_cell = maze.current_cell.findNeighborCells()

        if maze.next_cell:

            maze.current_cell.neighbors = []

            maze.stack.append(maze.current_cell)

            maze.removeWalls()

            maze.current_cell.current = False

            maze.current_cell = maze.next_cell

        elif len(maze.stack) > 0:
            maze.current_cell.current = False
            maze.current_cell = maze.stack.pop()

        elif len(maze.stack) == 0:
            maze.grid = []

            for y in range(rows):
                maze.grid.append([])
                for x in range(cols):
                    maze.grid[y].append(Cell(maze.screen, maze.grid, maze.cols, maze.rows, x, y))

            maze.current_cell = maze.grid[0][0]
            maze.next_cell = 0
            generate_done = True
    else:
        pprint(maze.solution)
        plot_route_back(maze.solution)

    # Display the game screen
    pygame.display.flip()

    # frame rate
    clock.tick(60)

# When the loop is stopped ('running' = false), end the game
pygame.quit()
