import pygame
import random

pygame.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Tamaño de la cuadrícula
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Inicialización del juego
snake = [(5, 5)]
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
direction = (1, 0)

# Tiempo
clock = pygame.time.Clock()
speed = 10

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                direction = (1, 0)

    # Mover la serpiente
    x, y = snake[0]
    new_head = (x + direction[0], y + direction[1])

    # Verificar colisiones con la comida
    if new_head == food:
        snake.insert(0, food)
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    else:
        snake.insert(0, new_head)
        snake.pop()

    # Verificar colisiones con las paredes
    if (
        new_head[0] < 0 or new_head[0] >= GRID_WIDTH
        or new_head[1] < 0 or new_head[1] >= GRID_HEIGHT
    ):
        running = False

    # Verificar colisiones con sí mismo
    if new_head in snake[1:]:
        running = False

    # Dibujar la pantalla
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, WHITE, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(speed)

pygame.quit()
