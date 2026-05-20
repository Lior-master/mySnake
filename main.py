import pygame
import random
from food import food_generation

pygame.init()

# Window size
WIDTH = 600
HEIGHT = 600

# Size of one grid cell
CELL_SIZE = 20

# Number of cells in the grid
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Snake")

# Clock used to control the game speed
clock = pygame.time.Clock()

# Snake position in the grid
snake_body = [
    [10,10],
    [9,10],
    [8,10]

]

# Food position in the grid
food_coord = food_generation(GRID_WIDTH, GRID_HEIGHT)

# Initial movement direction
# The snake starts by moving to the right
direction_x = 1
direction_y = 0

# Main game loop condition
running = True

while running:
    # Handle user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard input
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction_x != 1:
                direction_x = -1
                direction_y = 0

            elif event.key == pygame.K_RIGHT and direction_x != -1:
                direction_x = 1
                direction_y = 0

            elif event.key == pygame.K_UP and direction_y != 1:
                direction_x = 0
                direction_y = -1

            elif event.key == pygame.K_DOWN and direction_y != -1:
                direction_x = 0
                direction_y = 1

    # Move the snake by one cell
    [snake_x, snake_y] = snake_body[0]
    snake_x += direction_x
    snake_y += direction_y
    snake_body.insert(0, [snake_x, snake_y])

    # Check if the snake hits the wall
    if snake_x < 0 or snake_x >= GRID_WIDTH or snake_y < 0 or snake_y >= GRID_HEIGHT:
        running = False

    if (snake_x == food_coord[0]) and (snake_y == food_coord[1]):
        # The snake eats the food, we generate new food
        food_coord = food_generation(GRID_WIDTH, GRID_HEIGHT)
    else:
        # The snake moves without eating, we remove the tail
        snake_body.pop()

    for segment in snake_body[1:]:
        if segment == [snake_x, snake_y]:
            # The snake hits itself
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))

    for segment in snake_body:
        pixel_x = segment[0] * CELL_SIZE
        pixel_y = segment[1] * CELL_SIZE
        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE)
        )

    pygame.draw.circle(
        screen,
        (255, 0, 0),
        (food_coord[0] * CELL_SIZE + CELL_SIZE // 2, food_coord[1] * CELL_SIZE + CELL_SIZE // 2),
        CELL_SIZE // 2
    )

    # Update the display
    pygame.display.update()

    # Limit the game speed
    clock.tick(7)

pygame.quit()