import numpy as np
import pygame as pg
from pygame.draw import *
pg.init()

FPS = 30
screen = pg.display.set_mode((600, 600))
screen.fill((255, 255, 255))


circle(screen, (255, 255, 0), (300, 300), 120)


def rect_with_angle(x, y, a, b, aa):
    aa = aa * np.pi / 180
    polygon(screen, (0, 0, 0), [(x, y), (x + a * np.cos(aa), y + a * np.sin(aa)), (x + a * np.cos(aa) - b * np.sin(aa),
                                y + a * np.sin(aa) + b * np.cos(aa)), (x - b * np.sin(aa), y + b * np.cos(aa)), (x, y)])


rect_with_angle(390, 218, 15, 85, 70)
rect_with_angle(290, 250, 15, 85, 120)
circle(screen, (255, 0, 0), (250, 270), 20)
circle(screen, (0, 0, 0), (250, 270), 8)
circle(screen, (255, 0, 0), (350, 270), 20)
circle(screen, (0, 0, 0), (350, 270), 8)
rect(screen, (0, 0, 0), (235, 350, 135, 20))
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
