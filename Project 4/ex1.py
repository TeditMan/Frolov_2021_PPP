import pygame
from pygame.draw import *
from random import randint
pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 30
finished = False
x, y, r, h = 0, 0, 0, 0
k, i = 0, 0
color = (0, 0, 0)
dx, dy = randint(-100, 100), randint(-100, 100)
missed = True
moving = True
f = 0
clock = pygame.time.Clock()
screen_length = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_length, screen_height))
pygame.display.update()


def new_ball():     # создать новый шар
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(100, 500)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def fail(p1, u1):   # нарисовать красный крест
    a = 30
    line(screen, RED, (p1 - a, u1 + a), (p1 + a, u1 - a), 10)
    line(screen, RED, (p1 + a, u1 + a), (p1 - a, u1 - a), 10)


def gj(p1, u1):
    a = 30
    line(screen, GREEN, (p1 - a * 2 / 3, u1 - a), (p1, u1 + a), 10)
    line(screen, GREEN, (p1 + a * 2 / 3, u1 - a), (p1, u1 + a), 10)


while not finished:
    clock.tick(FPS)
    if f == 0:
        new_ball()
        pygame.display.update()
        k += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and h < 1:
            if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= r ** 2:
                print('hit!')
                i += 1
                circle(screen, BLACK, (x, y), r)
                gj(1100, 100)
                pygame.display.update()
                moving = False
            else:
                print('miss!')
                fail(1100, 100)
                pygame.display.update()
            h += 1
            missed = False
    if moving is True:
        circle(screen, BLACK, (x, y), r)
        pygame.display.update()
        x += dx / 50
        y += dy / 50
        circle(screen, color, (x, y), r)
        pygame.display.update()
        if x + r >= screen_length - 2 or x - r <= 2:
            dx = -dx
        if y + r >= screen_height - 2 or y - r <= 2:
            dy = -dy
    if f == 59:
        if missed:
            print('missed')
        h = 0
        moving = True
        dx, dy = randint(-100, 100), randint(-100, 100)
        screen.fill(BLACK)
    f += 1
    f %= 60

print('попал', i, 'раз')
print('всего', k, 'шаров')
print('доля попаданий:', i / k)
pygame.quit()
