import pygame
class Settings:
    def __init__(self, Width, Height, fps=7):
        self.grid_width = Width // 20
        self.grid_height = Height // 20
        self.cell_size = 20
        self.fps = fps
        self.width = Width
        self.height = Height
        self.color_food = (255, 0, 0)
