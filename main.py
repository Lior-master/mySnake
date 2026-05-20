import pygame
from food import food_drawing, food_generation
from settings import Settings
from the_snake import Snake
from logique_mouvement import DIRECTION_CHANGED, forward_the_wall, move_snake, touche_mov

pygame.init()

settings = Settings(400, 400)

# Create the game window
screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))

# Clock used to control the game speed
clock = pygame.time.Clock()

# Snake position in the grid
snake = Snake(settings)

# Food position in the grid
food_coord = food_generation(snake.body, settings.Grid_Width, settings.Grid_Height)

# Initial movement direction
# The snake starts by moving to the right
snake.direction = (1, 0)

# Main game loop condition
running = True

while running:
    # Handle user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard input
        elif not DIRECTION_CHANGED:
            DIRECTION_CHANGED = touche_mov(snake, event, DIRECTION_CHANGED)

    # Move the snake by one cell
    move_snake(snake)

    # Handle the snake going through the walls (wrap around)

    forward_the_wall(snake, settings)


    if snake.body[0] == list(food_coord):
        # The snake eats the food, we generate new food
        food_coord = food_generation(snake.body, settings.Grid_Width, settings.Grid_Height)
        settings.SCORE += 1
    else:
        # The snake moves without eating, we remove the tail
        snake.body.pop()

    for segment in snake.body[1:]:
        if segment == snake.body[0]:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    snake.draw(screen, settings)

    # Draw the food
    food_drawing(screen, food_coord, settings)

    pygame.display.set_caption("My Snake - Score: " + str(settings.SCORE))

    # Update the display
    pygame.display.update()
    DIRECTION_CHANGED = False
    # Limit the game speed
    clock.tick(settings.FPS)


pygame.quit()