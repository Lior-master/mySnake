import pygame
class Settings:
    def __init__(self, Width, Height, fps=7, cell_size=20, snake_size=None):
        self.grid_width = Width // cell_size
        self.grid_height = Height // cell_size
        self.cell_size = cell_size
        self.fps = fps
        self.width = Width
        self.height = Height
        self.color_food = (255, 0, 0)
