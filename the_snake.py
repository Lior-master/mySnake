import pygame
from food import food_generation
import settings

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

    def move(self,settings):
        [snake_x, snake_y] = self.body[0]
        snake_x += self.direction[0]
        snake_y += self.direction[1]
        self.body.insert(0, [snake_x, snake_y])

        # Handle the snake going through the walls (wrap around)
        if self.body[0][0] < 0:
            self.body[0][0] = settings.Grid_Width - 1
        elif self.body[0][0] >= settings.Grid_Width:
            self.body[0][0] = 0
        if self.body[0][1] < 0:
            self.body[0][1] = settings.Grid_Height - 1
        elif self.body[0][1] >= settings.Grid_Height:
            self.body[0][1] = 0

    def check_self_collision(self):
        head = self.body[0]
        return head not in self.body[1:]
    
    def touche_mov(self, event, direction_changed):
        if event.type == pygame.KEYDOWN and not direction_changed:
            if event.key == pygame.K_UP and self.direction != (0, 1):
                self.direction = (0, -1)
                return True

            elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                self.direction = (0, 1)
                return True

            elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                self.direction = (-1, 0)
                return True

            elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                self.direction = (1, 0)
                return True

        return direction_changed
    
    def check_eat_food(self, food_coord,settings):
        if self.body[0] == list(food_coord):
            food_coord = food_generation(self.body, settings.Grid_Width, settings.Grid_Height)
            settings.SCORE += 1
        else :
            self.body.pop()
        return food_coord