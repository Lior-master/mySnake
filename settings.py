import pygame
class Settings:
    def __init__(self, Width, Height, fps=7):
        self.Grid_Width = Width // 20
        self.Grid_Height = Height // 20
        self.Cell_Size = 20
        self.FPS = fps
        self.WIDTH = Width
        self.HEIGHT = Height
        self.SCORE = 0
        self.color_food = (255, 0, 0)

    def game_over(self, screen):
        # Show a Game Over message centered on the screen
        font = pygame.font.SysFont(None, 36)
        text = font.render("Game Over! Your score: " + str(self.SCORE), True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        pygame.display.update()

        # Wait until the player closes the window or presses a key/mouse button
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False