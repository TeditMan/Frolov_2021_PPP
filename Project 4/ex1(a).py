import pygame
from pygame.draw import *
from random import randint
import numpy as np
pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
colors_list = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 60
finished = False
k, k1, i, f = 0, 0, 0, 0
pool, colors, moving, dx, dy = [], [], [], [], []
pool1, colors1, moving1, dx1, dy1 = [], [], [], [], []
number_of_balls, number_of_triangles = 0, 0
lvl = int(input('выберите уровень сложности от 1 до 5: '))
if lvl == 1:
    lvl = 120
    number_of_balls = randint(0, 2)
    number_of_triangles = 2 - number_of_balls
elif lvl == 2:
    lvl = 90
    number_of_balls = randint(0, 4)
    number_of_triangles = 4 - number_of_balls
elif lvl == 3:
    lvl = 60
    number_of_balls = randint(0, 6)
    number_of_triangles = 6 - number_of_balls
elif lvl == 4:
    lvl = 40
    number_of_balls = randint(0, 8)
    number_of_triangles = 8 - number_of_balls
elif lvl == 5:
    lvl = 20
    number_of_balls = randint(0, 10)
    number_of_triangles = 10 - number_of_balls
clock = pygame.time.Clock()
screen_length = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_length, screen_height))
pygame.display.update()


def new_balls():
    global pool, colors, moving, dx, dy, k
    pool = []
    colors = []
    moving = []
    dx = []
    dy = []
    for p in range(number_of_balls):
        x = randint(100, 1100)
        y = randint(100, 500)
        r = randint(10, 100)
        colors.append(colors_list[randint(0, 5)])
        pool.append([x, y, r])
        moving.append(True)
        dx.append(randint(-100, 100))
        dy.append(randint(-100, 100))
        circle(screen, colors[p], (pool[p][0], pool[p][1]), pool[p][2])
        k += 1
        pygame.display.update()


def new_triangles():
    global pool1, colors1, moving1, dx1, dy1, k1
    pool1 = []
    colors1 = []
    moving1 = []
    dx1 = []
    dy1 = []
    for p in range(number_of_triangles):
        x = randint(100, 1100)
        y = randint(100, 500)
        r = randint(10, 100)
        colors1.append(colors_list[randint(0, 5)])
        pool1.append([x, y, r])
        moving1.append(True)
        dx1.append(randint(-100, 100))
        dy1.append(randint(-100, 100))
        polygon(screen, colors1[p], [(pool1[p][0], pool1[p][1] - pool1[p][2]),
                                     (pool1[p][0] + pool1[p][2] * np.sin(np.pi / 3),
                                      pool1[p][1] + pool1[p][2] * np.cos(np.pi / 3)),
                                     (pool1[p][0] - pool1[p][2] * np.sin(np.pi / 3),
                                      pool1[p][1] + pool1[p][2] * np.cos(np.pi / 3))])
        k1 += 1
        pygame.display.update()


while not finished:
    clock.tick(FPS)
    if f == 0:
        new_balls()
#        new_triangles()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for o in range(number_of_balls):
                if (event.pos[0] - pool[o][0]) ** 2 + (event.pos[1] - pool[o][1]) ** 2 <= pool[o][2] ** 2:
                    i += 1
                    circle(screen, BLACK, (pool[o][0], pool[o][1]), pool[o][2])
                    moving[o] = False
                    pygame.display.update()
#                """elif ... условие попадания в треугольник"""
    for o in range(number_of_balls):
        if moving[o] is True:
            circle(screen, BLACK, (pool[o][0], pool[o][1]), pool[o][2])
            pool[o][0] += dx[o] / 50
            pool[o][1] += dy[o] / 50
            circle(screen, colors[o], (pool[o][0], pool[o][1]), pool[o][2])
            pygame.display.update()
            if pool[o][0] + pool[o][2] >= screen_length - 2 or pool[o][0] - pool[o][2] <= 2:
                dx[o] = -dx[o]
            if pool[o][1] + pool[o][2] >= screen_height - 2 or pool[o][1] - pool[o][2] <= 2:
                dy[o] = -dy[o]
#    for o in range(number_of_triangles):
#        if moving1[o] is True:
#            polygon(screen, BLACK, [(pool1[o][0], pool1[o][1] - pool1[o][2]),
#                                    (pool1[o][0] + pool1[o][2] * np.sin(np.pi / 3),
#                                    pool1[o][1] + pool1[o][2] * np.cos(np.pi / 3)),
#                                    (pool1[o][0] - pool1[o][2] * np.sin(np.pi / 3),
#                                    pool1[o][1] + pool1[o][2] * np.cos(np.pi / 3))])
#            pool1[o][0] += dx1[o] / 50
#            pool1[o][1] += dy1[o] / 50
#            polygon(screen, colors1[o], [(pool1[o][0], pool1[o][1] - pool1[o][2]),
#                                         (pool1[o][0] + pool1[o][2] * np.sin(np.pi / 3),
#                                          pool1[o][1] + pool1[o][2] * np.cos(np.pi / 3)),
#                                         (pool1[o][0] - pool1[o][2] * np.sin(np.pi / 3),
#                                          pool1[o][1] + pool1[o][2] * np.cos(np.pi / 3))])
#            pygame.display.update()
#            if pool1[o][0] + pool1[o][2] >= screen_length - 2 or pool1[o][0] - pool1[o][2] <= 2:
#                dx1[o] = -dx1[o]
#            if pool1[o][1] + pool1[o][2] >= screen_height - 2 or pool1[o][1] - pool1[o][2] <= 2:
#                dy1[o] = -dy1[o]
    if f == lvl - 1:
        screen.fill(BLACK)
    f += 1
    f %= lvl

print('попал', i, 'раз')
print('всего', k, 'шаров')
print('доля попаданий:', i / k)
pygame.quit()
