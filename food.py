import random


def food_generation(Grid_Width, Grid_Height):
    food_x = random.randint(0, Grid_Width - 1)
    food_y = random.randint(0, Grid_Height - 1)
    return food_x, food_y