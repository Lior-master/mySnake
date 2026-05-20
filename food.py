import random
import pygame

def food_generation(snake_body, Grid_Width, Grid_Height):
    while True:
        food_x = random.randint(0, Grid_Width - 1)
        food_y = random.randint(0, Grid_Height - 1)
        if [food_x, food_y] not in snake_body:
            return food_x, food_y
        
def food_drawing(screen, food_coord, settings):
    pygame.draw.circle(
        screen,
        settings.color_food,
        (food_coord[0] * settings.Cell_Size + settings.Cell_Size // 2, food_coord[1] * settings.Cell_Size + settings.Cell_Size // 2),
        settings.Cell_Size // 2
    )