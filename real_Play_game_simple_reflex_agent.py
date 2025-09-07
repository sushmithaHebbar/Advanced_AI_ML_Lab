import pygame
import random
import sys

# --- Game Config ---
GRID_SIZE = 20
CELL_SIZE = 30
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)   # Food
RED = (200, 0, 0)     # Demon
BLUE = (0, 0, 200)    # Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reflex Agent Demo")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

# --- Entities ---
player = [GRID_SIZE // 2, GRID_SIZE // 2]  # Start center
score = 0

# Place first food
food = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]

# Demons (multiple)
demons = []
for _ in range(5):
    d = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
    while d == food or d == player:  # avoid overlap
        d = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
    demons.append(d)

# --- Game Loop ---
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Controls ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player[1] > 0:
        player[1] -= 1
    if keys[pygame.K_DOWN] and player[1] < GRID_SIZE - 1:
        player[1] += 1
    if keys[pygame.K_LEFT] and player[0] > 0:
        player[0] -= 1
    if keys[pygame.K_RIGHT] and player[0] < GRID_SIZE - 1:
        player[0] += 1

    # --- Eat Food ---
    if player == food:
        score += 1
        # Place new food not overlapping demons
        food = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]
        while food in demons or food == player:
            food = [random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)]

    # --- Move Demons Randomly ---
    for i in range(len(demons)):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)])
        new_x = max(0, min(GRID_SIZE - 1, demons[i][0] + dx))
        new_y = max(0, min(GRID_SIZE - 1, demons[i][1] + dy))
        # Don’t allow demon on food
        if [new_x, new_y] != food:
            demons[i] = [new_x, new_y]

    # --- Check Collision ---
    if player in demons:
        print("💀 Game Over! Final Score:", score)
        running = False

    # --- Draw Grid ---
    screen.fill(BLACK)
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

    # Draw food
    pygame.draw.circle(screen, GREEN, (food[0] * CELL_SIZE + CELL_SIZE // 2,
                                       food[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    # Draw demons
    for d in demons:
        pygame.draw.circle(screen, RED, (d[0] * CELL_SIZE + CELL_SIZE // 2,
                                         d[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    # Draw player
    pygame.draw.circle(screen, BLUE, (player[0] * CELL_SIZE + CELL_SIZE // 2,
                                      player[1] * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

    # Score text
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()






