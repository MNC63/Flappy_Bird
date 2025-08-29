import pygame
import sys
import random


# ------------
# Functions
# ------------
def draw_floor():
    """ Draw double fllor to create infinite scrolling effect"""
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))


def create_pipe():
    bottom_pipe = pipe_sf.get_rect(
        midtop=(SCREEN_WIDTH//2 + 200, random.randint(250, 350)))
    top_pipe = pipe_sf.get_rect(
        midbottom=(SCREEN_WIDTH//2 + 200, bottom_pipe.top - 130))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    new_pipes = []
    for bottom, top in pipes:
        bottom.centerx -= 5
        top.centerx -= 5
        new_pipes.append((bottom, top))
    return new_pipes


def draw_pipes(pipes):
    for bottom, top in pipes:
        screen.blit(pipe_sf, bottom)
        filp_pipe = pygame.transform.flip(pipe_sf, False, True)
        screen.blit(filp_pipe, top)


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
pipe_ls = []

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

pipe_sf = pygame.image.load('FileGame/assets/pipe-green.png')
pipe_sf = pygame.transform.scale2x(pipe_sf)

spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)


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
                bird_movement -= 6
        if event.type == spawnpipe:
            pipe_ls.append(create_pipe())

    # Background
    screen.blit(bg, (0, 0))

    # Bird Movement
    screen.blit(bird, bird_rect)
    bird_movement += gravity
    bird_rect.centery += bird_movement

    # Pipe Movement
    pipe_ls = move_pipes(pipe_ls)
    draw_pipes(pipe_ls)

    # Floor Movement
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    # Update the display
    pygame.display.update()
    clock.tick(60)
