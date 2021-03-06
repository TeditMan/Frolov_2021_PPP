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

FPS = 60
finished = False
try_count = 0
x, y, r, h = 0, 0, 0, 0
k, i = 0, 0
lvl = int(input('выберите уровень от 1 до 3: '))
if lvl == 1:
    lvl = 80
elif lvl == 2:
    lvl = 60
elif lvl == 3:
    lvl = 40
color = (0, 0, 0)
dx, dy = randint(-100, 100), randint(-100, 100)
missed = True
moving = True
f = 0
clock = pygame.time.Clock()
screen_length = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_length, screen_height), pygame.FULLSCREEN)
pygame.display.update()


def new_ball():
    """новый шар"""
    global x, y, r, color
    x = randint(100, 1266)
    y = randint(100, 668)
    r = randint(25, 75)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def fail(p1, u1):
    """красный крест за промах"""
    a = 30
    line(screen, RED, (p1 - a, u1 + a), (p1 + a, u1 - a), 10)
    line(screen, RED, (p1 + a, u1 + a), (p1 - a, u1 - a), 10)


def gj(p1, u1):
    """зелёная галочка за попадание"""
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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        elif try_count == 100:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and h < 1:
            if (event.pos[0] - x) ** 2 + (event.pos[1] - y) ** 2 <= r ** 2:
                i += 1
                circle(screen, BLACK, (x, y), r)
                gj(1100, 100)
                pygame.display.update()
                moving = False
            else:
                fail(1100, 100)
                pygame.display.update()
            h += 1
            missed = False
    if moving is True:
        circle(screen, BLACK, (x, y), r)
        x += dx / 50
        y += dy / 50
        circle(screen, color, (x, y), r)
        pygame.display.update()
        if x + r >= screen_length - 2 or x - r <= 2:
            dx = -dx
        if y + r >= screen_height - 2 or y - r <= 2:
            dy = -dy
    if f == lvl - 1:
        h = 0
        moving = True
        dx, dy = randint(-100, 100), randint(-100, 100)
        screen.fill(BLACK)
        try_count += 1
    f += 1
    f %= lvl

print('попал', i, 'раз')
print('всего', k - 1, 'шаров')
print('доля попаданий:', i / (k - 1))
pygame.quit()
