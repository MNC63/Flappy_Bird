import pygame
import sys


def draw_floor():
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))


pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
bg = pygame.image.load('FileGame/assets/background-night.png')
bg = pygame.transform.scale2x(bg)
floor = pygame.image.load('FileGame/assets/floor.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg, (0, 0))
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)
