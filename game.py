import pygame
import sys


# ------------
# Functions
# ------------
def draw_floor():
    """ Draw double fllor to create infinite scrolling effect"""
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))


# ------------
# Game setup
# ------------
pygame.init()

# screen and clock
SCREEN_WIDTH, SCREEN_HEIGHT = 432, 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Game Variables
floor_x_pos = 0
gravity = 0.25
bird_movement = 0

# ------------
# Load assets
# ------------
bg = pygame.image.load('FileGame/assets/background-night.png')
bg = pygame.transform.scale2x(bg)

floor = pygame.image.load('FileGame/assets/floor.png')
floor = pygame.transform.scale2x(floor)

bird = pygame.image.load('FileGame/assets/yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100, SCREEN_HEIGHT // 2))


# ------------
# Game Loop
# ------------
while True:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 8

    # Background
    screen.blit(bg, (0, 0))

    # Floor Movement
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    # Bird Movement
    screen.blit(bird, bird_rect)
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # Update the display
    pygame.display.update()
    clock.tick(60)
