import pygame

pygame.init()

# Taille de la fenêtre
WIDTH = 600
HEIGHT = 600

# Taille d'une case de la grille
CELL_SIZE = 20

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Snake")

# Horloge pour contrôler la vitesse
clock = pygame.time.Clock()

# Position du serpent dans la grille
snake_x = 10
snake_y = 10


running = True

while running:
    # 1. Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x -= 1  # Exemple de mouvement vers la gauche
            elif event.key == pygame.K_RIGHT:
                snake_x += 1  # Exemple de mouvement vers la droite
            elif event.key == pygame.K_UP:
                snake_y -= 1  # Exemple de mouvement vers le haut
            elif event.key == pygame.K_DOWN:
                snake_y += 1  # Exemple de mouvement vers le bas

    # 2. Dessiner le fond
    screen.fill((0, 0, 0))

    # 3. Convertir la position grille en pixels
    pixel_x = snake_x * CELL_SIZE
    pixel_y = snake_y * CELL_SIZE

    # 4. Dessiner le serpent
    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE)
    )

    # 5. Mettre à jour l'écran
    pygame.display.update()

    # 6. Limiter la vitesse
    clock.tick(10)

pygame.quit()