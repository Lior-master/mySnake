import pygame

global SCORE
SCORE = 0
def game_over(settings, screen):
        # Show a Game Over message centered on the screen
        font = pygame.font.SysFont(None, 36)
        text = font.render("Game Over! Your score: " + str(SCORE), True, (255, 255, 255))
        text_rect = text.get_rect(center=(settings.width // 2, settings.height // 2))
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