import numpy as np
import pygame as pg
from pygame.draw import *
pg.init()

FPS = 30
screen = pg.display.set_mode((1000, 600))
screen.fill((255, 255, 255))

#
rect(screen, (249, 225, 131), (0, 0, 1000, 130))
rect(screen, (255, 203, 183), (0, 130, 1000, 130))
rect(screen, (249, 215, 148), (0, 260, 1000, 130))
rect(screen, (195, 152, 145), (0, 390, 1000, 210))
circle(screen, (255, 239, 0), (500, 130), 60)
#
coord = [(1000, 190), (0, 280), (10, 240)]

dx = 0.1
z = []
for i in range(1000):
    z.append((10 + dx, 240 - (0.006 * dx * dx)))
    dx += 0.15
for i in range(1000):
    coord.append(z[i])

h = [(200, 115), (220, 140), (360, 220), (420, 212), (490, 235), (550, 200), (610, 210), (630, 195)]
for i in range(len(h)):
    coord.append(h[i])

dx = 0.1
z1 = []
for i in range(1000):
    z1.append((630 + dx, 195 - (dx * dx * 0.01)))
    dx += 0.09
for i in range(1000):
    coord.append(z1[i])

h1 = [(745, 112), (790, 150), (830, 140), (870, 160), (910, 145)]
for i in range(len(h1)):
    coord.append(h1[i])


coord1 = [(1000, 390), (0, 390), (0, 300), (15, 300), (40, 330)]

dx = 0.1
z2 = []
for i in range(1000):
    z2.append((40 + dx, 330 - (- 0.01 * dx * dx + 1.8 * dx)))
    dx += 0.2
for i in range(1000):
    coord1.append(z2[i])

h2 = [(290, 310), (365, 325), (430, 360), (520, 340)]
for i in range(len(h2)):
    coord1.append(h2[i])

dx = 0.1
z3 = []
for i in range(600):
    z3.append((520 + dx, 340 - (- 0.01 * dx * dx + 1.8 * dx)))
    dx += 0.2
for i in range(600):
    coord1.append(z3[i])

h3 = [(720, 330), (770, 280), (810, 310), (840, 270), (900, 280), (1000, 220)]
for i in range(len(h3)):
    coord1.append(h3[i])

coord2 = [(1000, 600), (0, 600), (0, 290), (120, 330), (200, 430)]
dx = 0.1
z4 = []
for i in range(600):
    z4.append((200 + dx, 430 + (- 0.01 * dx * dx + 2.5 * dx)))
    dx += 0.2
for i in range(600):
    coord2.append(z4[i])

h4 = [(450, 590), (600, 500)]
for i in range(len(h4)):
    coord2.append(h4[i])

dx = 0.2
z4 = []
for i in range(600):
    z4.append((600 + dx, 500 + (- 0.005 * dx * dx + 1 * dx)))
    dx += 0.4
for i in range(600):
    coord2.append(z4[i])

dx = 0.2
z5 = []
for i in range(600):
    z5.append((839.5 + dx, 452.3 - (- 0.005 * dx * dx + 1.6 * dx)))
    dx += 0.4
for i in range(600):
    coord2.append(z5[i])


def bird(x, y):
    coord_b = [(x, y), (x + 25, y - 15)]
    dx1 = 0
    g = []
    for k in range(700):
        g.append((x + 25 - dx1, y - 15 - (- 0.02 * dx1 * dx1 + 0.0005 * dx1)))
        dx1 += 25 / 700
    for k in range(700):
        coord_b.append(g[k])

    hg = [(x - 25, y - 15)]
    for k in range(len(hg)):
        coord_b.append(hg[k])

    dx1 = 0
    g1 = []
    for k in range(700):
        g1.append((x - 25 + dx1, y - 15 - (- 0.02 * dx1 * dx1 + 0.0005 * dx1)))
        dx1 += 25 / 700
    for k in range(700):
        coord_b.append(g1[k])

    hg1 = [(x, y)]
    for k in range(len(hg1)):
        coord_b.append(hg[k])

    polygon(screen, (0, 0, 0), coord_b)


#
circle(screen, (255, 145, 0), (733, 119), 15)
polygon(screen, (255, 145, 0), coord)
polygon(screen, (161, 43, 7), coord1)
polygon(screen, (19, 18, 33), coord2)
bird(500, 130)
bird(500, 250)
bird(500, 300)
bird(400, 300)
bird(420, 240)
bird(760, 500)
bird(760, 430)
bird(670, 465)
bird(600, 420)
#
pg.display.update()
clock = pg.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
#
print(z4[599])
