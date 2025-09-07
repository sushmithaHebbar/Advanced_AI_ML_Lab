import pygame
import sys

# --- Initialize pygame ---
pygame.init()

# --- Game Settings ---
CELL_SIZE = 80
ROWS, COLS = 4, 5
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 200, 0)
GRAY = (180, 180, 180)

# --- Grid Definition ---
# 'S' = Start, 'E' = End, '#' = Obstacle, '1' = Point
grid = [
    ['#', 'S', ' ', '1', '#'],
    [' ', ' ', '1', '#', '#'],
    ['#', '1', ' ', '1', 'E'],
    ['#', '#', ' ', ' ', '#'],
]

# Find Start
player_pos = None
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == 'S':
            player_pos = [r, c]
            break
    if player_pos:
        break

score = 0
game_over = False

# --- Setup Display ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid Game")
font = pygame.font.SysFont("Arial", 28)

clock = pygame.time.Clock()

def draw_grid():
    """Draws the entire grid + player"""
    screen.fill(WHITE)

    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            cell = grid[r][c]

            if cell == '#':
                pygame.draw.rect(screen, BLACK, rect)
            elif cell == '1':
                pygame.draw.rect(screen, YELLOW, rect)
            elif cell == 'E':
                pygame.draw.rect(screen, RED, rect)
            else:
                pygame.draw.rect(screen, GRAY, rect)

            pygame.draw.rect(screen, WHITE, rect, 2)  # grid lines

    # Draw Player
    pr, pc = player_pos
    prect = pygame.Rect(pc * CELL_SIZE, pr * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, BLUE, prect)

    # Draw Score
    score_text = font.render(f"Score: {score}", True, GREEN)
    screen.blit(score_text, (10, HEIGHT - 40))


# --- Game Loop ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        dr, dc = 0, 0
        if keys[pygame.K_UP]:
            dr, dc = -1, 0
        elif keys[pygame.K_DOWN]:
            dr, dc = 1, 0
        elif keys[pygame.K_LEFT]:
            dr, dc = 0, -1
        elif keys[pygame.K_RIGHT]:
            dr, dc = 0, 1

        if dr != 0 or dc != 0:
            new_r = player_pos[0] + dr
            new_c = player_pos[1] + dc

            # Boundary check
            if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                cell = grid[new_r][new_c]
                if cell != '#':  # not obstacle
                    player_pos = [new_r, new_c]

                    if cell == '1':
                        score += 1
                        grid[new_r][new_c] = ' '  # collect point
                    elif cell == 'E':
                        game_over = True

    # Draw everything
    draw_grid()

    if game_over:
        msg = font.render("You reached the end!", True, RED)
        screen.blit(msg, (40, HEIGHT//2 - 20))

    pygame.display.flip()
    clock.tick(FPS)

# import pygame
# import sys

# # --- Initialize pygame ---
# pygame.init()

# # --- Game Settings ---
# CELL_SIZE = 80
# ROWS, COLS = 4, 5
# WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
# FPS = 10

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 200, 0)
# RED = (200, 0, 0)
# BLUE = (0, 0, 200)
# YELLOW = (255, 200, 0)
# GRAY = (200, 200, 200)

# # --- Grid Definition ---
# # 'S' = Start, 'E' = End, '#' = Obstacle, '1' = Point, ' ' = Empty
# grid = [
#     ['#', 'S', ' ', ' ', '#'],
#     [' ', '1', ' ', '#', '#'],
#     ['#', ' ', ' ', '1', 'E'],
#     ['#', '#', ' ', ' ', '#'],
# ]

# # Find Start
# player_pos = None
# for r in range(ROWS):
#     for c in range(COLS):
#         if grid[r][c] == 'S':
#             player_pos = [r, c]
#             grid[r][c] = 'P'   # replace Start with Player
#             break
#     if player_pos:
#         break

# score = 0
# game_over = False

# # --- Setup Display ---
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Grid Game")
# font = pygame.font.SysFont("consolas", 40, bold=True)
# score_font = pygame.font.SysFont("Arial", 28)

# clock = pygame.time.Clock()

# def draw_grid():
#     """Draws the grid with pygame symbols (characters)."""
#     screen.fill(WHITE)

#     for r in range(ROWS):
#         for c in range(COLS):
#             rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)

#             # background color
#             pygame.draw.rect(screen, GRAY, rect)
#             pygame.draw.rect(screen, BLACK, rect, 2)  # grid lines

#             # symbol to draw
#             cell = grid[r][c]

#             if cell == '#':
#                 text = font.render("#", True, BLACK)
#             elif cell == '1':
#                 text = font.render("1", True, YELLOW)
#             elif cell == 'E':
#                 text = font.render("E", True, RED)
#             elif cell == 'P':
#                 text = font.render("P", True, BLUE)
#             else:
#                 text = font.render(" ", True, WHITE)

#             # center text in cell
#             text_rect = text.get_rect(center=rect.center)
#             screen.blit(text, text_rect)

#     # Draw Score
#     score_text = score_font.render(f"Score: {score}", True, GREEN)
#     screen.blit(score_text, (10, HEIGHT - 40))


# # --- Game Loop ---
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     keys = pygame.key.get_pressed()

#     if not game_over:
#         dr, dc = 0, 0
#         if keys[pygame.K_UP]:
#             dr, dc = -1, 0
#         elif keys[pygame.K_DOWN]:
#             dr, dc = 1, 0
#         elif keys[pygame.K_LEFT]:
#             dr, dc = 0, -1
#         elif keys[pygame.K_RIGHT]:
#             dr, dc = 0, 1

#         if dr != 0 or dc != 0:
#             new_r = player_pos[0] + dr
#             new_c = player_pos[1] + dc

#             # Boundary check
#             if 0 <= new_r < ROWS and 0 <= new_c < COLS:
#                 cell = grid[new_r][new_c]
#                 if cell != '#':  # not obstacle
#                     # Clear old position
#                     grid[player_pos[0]][player_pos[1]] = ' '

#                     # Move player
#                     player_pos = [new_r, new_c]

#                     if cell == '1':
#                         score += 1
#                     elif cell == 'E':
#                         game_over = True

#                     # Place player in new cell
#                     grid[new_r][new_c] = 'P'

#     # Draw everything
#     draw_grid()

#     if game_over:
#         msg = score_font.render("You reached the end!", True, RED)
#         screen.blit(msg, (40, HEIGHT//2 - 20))

#     pygame.display.flip()
#     clock.tick(FPS)
