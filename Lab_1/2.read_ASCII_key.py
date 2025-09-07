
from advanced_grid_layout import create_grid_matrix

# def read_ascii_grid(grd_string):
#     """Convert ASCII grid string into a 2D list"""
#     return [list(line) for line in grd_string.strip().split("\n")]

# def create_grid_with_st_t(n):A
#     """Create a grid with 'S' (start) and 'T' (task) positions"""
    
#     return grid

def find_start_and_tasks(grid):
    """Find start 'S' and all task cells 'T' with coordinates"""
    start = None
    tasks = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'T':
                tasks.append((i, j))
    return start, tasks

def pretty_print(grid):
    """Nicely display the grid"""
    for row in grid:
        print(" ".join(row))

# Example ASCII Grid (could also be loaded dynamically from a file)
# ascii_grid = """
# #######
# #..T..#
# #..#T.#
# #S.#T.#
# #######
# """



# Use the dynamic grid with S and T positions
n=int(input("Enter the num of rows and cols :"))
grid = create_grid_matrix(n)  # Create a 6x6 grid with S and T
pretty_print(grid)

start, tasks = find_start_and_tasks(grid)

print("\nStart position:", start)
print("Task cells:", tasks)

# No infinite loop - just display once
