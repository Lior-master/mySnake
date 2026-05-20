import pygame
from food import food_drawing, food_generation
import gameplay
from settings import Settings
from the_snake import Snake

pygame.init()

settings = Settings(400, 400)

# Create the game window
screen = pygame.display.set_mode((settings.width, settings.height))

# Clock used to control the game speed
clock = pygame.time.Clock()

# Snake position in the grid
snake = Snake(settings)

# Food position in the grid
food_coord = food_generation(snake.body, settings)

# Main game loop condition
running = True
DIRECTION_CHANGED = False

while running:
    # Handle user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Handle keyboard input
        elif not DIRECTION_CHANGED:
            DIRECTION_CHANGED = snake.touche_mov(event, DIRECTION_CHANGED)

    # Move the snake by one cell
    snake.move(settings)


    food_coord = snake.check_eat_food(food_coord,settings)

    running = snake.is_alive()
    
    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the snake
    snake.draw(screen, settings)

    # Draw the food
    food_drawing(screen, food_coord, settings)

    pygame.display.set_caption("My Snake - Score: " + str(gameplay.SCORE))

    # Update the display
    pygame.display.update()
    DIRECTION_CHANGED = False
    # Limit the game speed
    clock.tick(settings.fps)

gameplay.game_over(settings,screen)

pygame.quit()
exit()