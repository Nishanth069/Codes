import pygame
from collections import deque
import random

# Initialize pygame and constants
pygame.init()
WIDTH, HEIGHT, GRID_SIZE = 400, 400, 40
ROWS, COLS = HEIGHT // GRID_SIZE, WIDTH // GRID_SIZE
WHITE, BLACK, RED, GREEN, BLUE, PURPLE, GRAY = (255, 255, 255), (0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (128, 0, 128), (169, 169, 169)

# Set up display and basic grid with obstacles
screen = pygame.display.set_mode((WIDTH, HEIGHT))
grid = [[0 if random.random() > 0.2 else 1 for _ in range(COLS)] for _ in range(ROWS)]
start, goal = (0, 0), (ROWS - 1, COLS - 1)
grid[start[0]][start[1]], grid[goal[0]][goal[1]] = 0, 0  # Ensure start and goal are open

def dfs():
    stack = [(start)]
    visited = {start}
    path = []

    while stack:
        x, y = stack.pop()
        path.append((x, y))

        # Draw the current state
        draw_grid(path)
        pygame.draw.rect(screen, BLUE, (y * GRID_SIZE, x * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        pygame.display.update()
        pygame.time.delay(100)

        if (x, y) == goal:
            print("Goal reached!")
            draw_grid(path)
            return

        # Explore neighbors in 4 possible directions
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in visited and grid[nx][ny] == 0:
                visited.add((nx, ny))
                stack.append((nx, ny))

    print("Goal not reachable.")

def draw_grid(path):
    screen.fill(WHITE)
    for row in range(ROWS):
        for col in range(COLS):
            color = GRAY if grid[row][col] == 1 else WHITE
            pygame.draw.rect(screen, color, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BLACK, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
    pygame.draw.rect(screen, RED, (start[1] * GRID_SIZE, start[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, GREEN, (goal[1] * GRID_SIZE, goal[0] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    for x, y in path:
        pygame.draw.rect(screen, PURPLE, (y * GRID_SIZE, x * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Main loop
def main():
    dfs()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
