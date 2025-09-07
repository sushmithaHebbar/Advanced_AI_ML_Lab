import os
import random
import threading
import time

# --- Game Config ---
ROWS, COLS = 6, 8   # Grid size
NUM_OBSTACLES = 12  # Number of obstacles '#'
OBSTACLE_REFRESH_TIME = 5  # seconds between obstacle udates

# --- Game State Variables ---
grid = [[' ' for _ in range(COLS)] for _ in range(ROWS)]

# Place Start 'S'
start_pos = (0, 0)
grid[start_pos[0]][start_pos[1]] = 'S'

# Place End 'E'
end_pos = (ROWS - 1, COLS - 1)
grid[end_pos[0]][end_pos[1]] = 'E'

lock = threading.Lock()  # to prevent race conditions

# --- Functions ---
def place_random_score():
    """Place a '1' in a random empty cell."""
    while True:
        r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
        if grid[r][c] == ' ':
            grid[r][c] = '1'
            return (r, c)

def place_random_obstacles():
    """Regenerate obstacles at random empty positions."""
    with lock:
        # Clear old obstacles
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '#':
                    grid[r][c] = ' '

        # Place new obstacles
        placed = 0
        while placed < NUM_OBSTACLES:
            r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
            if grid[r][c] == ' ':
                grid[r][c] = '#'
                placed += 1

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(current_grid, player_position, score):
    clear_screen()
    display_grid = [row[:] for row in current_grid]
    r, c = player_position
    display_grid[r][c] = 'P'
    for row in display_grid:
        print(' '.join(row))
    print(f"\nScore: {score}")

def get_move():
    valid_moves = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
    while True:
        move = input("Enter your move (u, d, l, r): ").lower().strip()
        if move in valid_moves:
            return valid_moves[move]
        print("Invalid move. Please enter 'u', 'd', 'l', or 'r'.")

def obstacle_refresher():
    """Background thread to udate obstacles every few seconds."""
    while not game_over:
        time.sleep(OBSTACLE_REFRESH_TIME)
        place_random_obstacles()

# --- Initialize ---
player_pos = [start_pos[0], start_pos[1]]
score = 0
game_over = False
score_pos = place_random_score()
place_random_obstacles()

# Start obstacle refresher thread
threading.Thread(target=obstacle_refresher, daemon=True).start()

print("Welcome to the Timed Grid Game!")
print("Navigate from 'S' to 'E'.")
print("Collect '1's for points. Avoid '#' obstacles.")
print(f"Obstacles change automatically every {OBSTACLE_REFRESH_TIME} seconds!")
input("Press Enter to start...")

# --- Game Loop ---
while not game_over:
    print_grid(grid, player_pos, score)

    dr, dc = get_move()
    new_row, new_col = player_pos[0] + dr, player_pos[1] + dc

    with lock:
        # Check bounds
        if not (0 <= new_row < ROWS and 0 <= new_col < COLS):
            print("You can't move off the grid!")
            input("Press Enter to continue...")
            continue

        cell_content = grid[new_row][new_col]

        if cell_content == '#':
            print("You hit an obstacle! Move blocked.")
            input("Press Enter to continue...")
            continue

        # Clear old player pos
        if (player_pos[0], player_pos[1]) != start_pos:
            grid[player_pos[0]][player_pos[1]] = ' '

        # udate player position
        player_pos = [new_row, new_col]

        if cell_content == '1':
            score += 1
            print("You found a point! Score +1.")
            grid[new_row][new_col] = ' '
            score_pos = place_random_score()
        
        if score==10:
            game_over = True
            print_grid(grid, player_pos, score)
            print("\n🎉 Congratulations! You reached the end!")
            print(f"Your final score is: {score}")
            print("Game Over.")
            break

        if cell_content == 'E':
            game_over = True
            print_grid(grid, player_pos, score)
            print("\n🎉 Congratulations! You reached the end!")
            print(f"Your final score is: {score}")
            print("Game Over.")
            break

    # input("Press Enter to continue...")

