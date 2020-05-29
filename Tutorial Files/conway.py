# Conway's Game of Life

import random, time, copy

WIDTH = 60
HEIGHT = 20

# Create a list for the cells
next_cells = []
for x in range(WIDTH):
    column = [] # Create a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')  # Add a living cell
        else:
            column.append(' ')   # Add a dead cell
    next_cells.append(column)   # next_cells is a list of column lists

while True: # Main program loop
    print('\n\n\n\n\n') # Separate each step with newlines.
    current_cells = copy.deepcopy(next_cells)

    # Print current_cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')  # Print the # or space
        print() # Print a newline at the end of the row

    # Calculate the next step's cells based on the current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring coordinates
            # '% WIDTH' ensures left_coord is always between 0 and WIDTH - 1
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT

            # Count number of living neighbours:
            num_neighbours = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbours += 1 # Top-left neighbour is alive
            if current_cells[x][above_coord] == '#':
                num_neighbours += 1 # Top neighbour is alive
            if current_cells[right_coord][above_coord] == '#':
                num_neighbours += 1 # Top-right neighbour is alive
            if current_cells[left_coord][y] == '#':
                num_neighbours += 1 # Left neighbour is alive
            if current_cells[right_coord][y] == '#':
                num_neighbours += 1 # Right neighbour is alive
            if current_cells[left_coord][below_coord] == '#':
                num_neighbours += 1 # Bottom-left neighbour is alive
            if current_cells[x][below_coord] == '#':
                num_neighbours += 1 # Bottom neighbour is alive
            if current_cells[right_coord][below_coord] == '#':
                num_neighbours += 1 # Bottom-right neighbour is alive

            # Set cells based on Conway's Game of Life rules
            if current_cells[x][y] == '#' and (num_neighbours == 2 or num_neighbours == 3):
                # Living cells with 2 or 3 neighbours stay alive
                next_cells[x][y] == '#'
            elif current_cells[x][y] == ' ' and num_neighbours == 3:
                # Dead cells with 3 neighbours come alive
                next_cells[x][y] == '#'
            else:
                # Everything else dies or stays dead
                next_cells[x][y] = ' '

    # Add a 1-second pause to reduce flickering
    time.sleep(1)











