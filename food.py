import random

def food_generation(snake_body, Grid_Width, Grid_Height):
    while True:
        food_x = random.randint(0, Grid_Width - 1)
        food_y = random.randint(0, Grid_Height - 1)
        if [food_x, food_y] not in snake_body:
            return food_x, food_y