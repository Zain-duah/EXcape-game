import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Avoid the Blocks!")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player (a rectangle)
player = pygame.Rect(200, 500, 50, 50)
player_speed = 5

# Obstacles
obstacles = []
obstacle_speed = 3
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Spawn obstacles randomly
    if random.randint(1, 20) == 1:
        obstacles.append(pygame.Rect(random.randint(0, 350), 0, 50, 50))

    # Move player (left/right)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < 350:
        player.x += player_speed

    # Move & draw obstacles
    for obstacle in obstacles[:]:
        obstacle.y += obstacle_speed
        pygame.draw.rect(screen, RED, obstacle)

        # Collision check
        if player.colliderect(obstacle):
            running = False

        # Remove off-screen obstacles
        if obstacle.y > 600:
            obstacles.remove(obstacle)

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Quit if window closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(30)  # 30 FPS

pygame.quit()