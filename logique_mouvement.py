import pygame
DIRECTION_CHANGED = False

def touche_mov(snake, event, direction_changed):
    if event.type == pygame.KEYDOWN and not direction_changed:
        if event.key == pygame.K_UP and snake.direction != (0, 1):
            snake.direction = (0, -1)
            return True

        elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
            snake.direction = (0, 1)
            return True

        elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
            snake.direction = (-1, 0)
            return True

        elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
            snake.direction = (1, 0)
            return True

    return direction_changed


def move_snake(snake):
    [snake_x, snake_y] = snake.body[0]
    snake_x += snake.direction[0]
    snake_y += snake.direction[1]
    snake.body.insert(0, [snake_x, snake_y])

def forward_the_wall(snake, settings):
    if snake.body[0][0] < 0:
        snake.body[0][0] = settings.Grid_Width - 1
    elif snake.body[0][0] >= settings.Grid_Width:
        snake.body[0][0] = 0
    if snake.body[0][1] < 0:
        snake.body[0][1] = settings.Grid_Height - 1
    elif snake.body[0][1] >= settings.Grid_Height:
        snake.body[0][1] = 0