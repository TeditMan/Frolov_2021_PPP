"""
import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, RED, event.pos, 50)
                pygame.display.update()
            elif event.button == 3:
                circle(screen,  BLUE, event.pos, 50)
                pygame.display.update()

pygame.quit()
"""
import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1400, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
x, y, r = 0, 0, 0


def new_ball():
    # рисует новый шарик
    global x, y, r
    x = randint(100, 1300)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    new_ball()
    print(x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            print(event.pos[0], x)
            # print((event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 - r ** 2)
            if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= r ** 2:
                print('hit!')
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
