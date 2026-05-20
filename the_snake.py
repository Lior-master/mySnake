import pygame
class Snake:
    def __init__(self, settings):
        self.body = [[settings.Grid_Width // 2, settings.Grid_Height // 2],
                     [settings.Grid_Width // 2, settings.Grid_Height // 2 + 1],
                     [settings.Grid_Width // 2, settings.Grid_Height // 2 + 2]]
        self.direction = (0, -1)  # Initial direction: up
        self.color = (0, 255, 0)  # Green color for the snake

    def draw(self, screen, settings):
        for segment in self.body:
            pixel_x = segment[0] * settings.Cell_Size
            pixel_y = segment[1] * settings.Cell_Size
            pygame.draw.rect(
                screen,
                self.color,
                (pixel_x, pixel_y, settings.Cell_Size, settings.Cell_Size)
            )