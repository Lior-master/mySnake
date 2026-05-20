import random
import pygame

def food_generation(snake_body, settings):
    while True:
        food_x = random.randint(0, settings.grid_width - 1)
        food_y = random.randint(0, settings.grid_height - 1)
        if [food_x, food_y] not in snake_body:
            return food_x, food_y
        
def food_drawing(screen, food_coord, settings):
    pygame.draw.circle(
        screen,
        settings.color_food,
        (food_coord[0] * settings.cell_size + settings.cell_size // 2, food_coord[1] * settings.cell_size + settings.cell_size // 2),
        settings.cell_size // 2
    )