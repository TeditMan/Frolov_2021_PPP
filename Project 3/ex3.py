import pygame
from pygame.draw import *
import numpy as np
pygame.init()


def fish(x, y, k):
    """Рыба. x, y координаты центра тела рыбы, k - коэффициент размера рыбы: если k < 0, то рыба смотрит налево,
     иначе - направо"""

    ellipse(screen, (13, 110, 60), [x - 40 * abs(k), y - 15 * abs(k), 80 * abs(k), 30 * abs(k)])
    circle(screen, (0, 0, 250), (x + 20 * k, y), 6 * abs(k), 6 * abs(k))
    circle(screen, (0, 0, 0), (x + k * 21, y), 2 * abs(k), 2 * abs(k))
    polygon(screen, (136, 5, 0), [[x - 40 * k, y], [x - 60 * k, y + 3 * abs(k)], [x - 55 * k, y - 15 * abs(k)],
                                  [x - 37 * k, y - 7 * abs(k)]], 0)
    polygon(screen, (136, 5, 0),
            [[x, y - 15 * abs(k)], [x - 10 * k, y - 30 * abs(k)], [x + 15 * k, y - 25 * abs(k)],
             [x + 10 * k, y - 14 * abs(k)]], 0)
    polygon(screen, (136, 5, 0),
            [[x, y + 15 * abs(k)], [x + 10 * k, y + 14 * abs(k)], [x + 15 * k, y + 20 * abs(k)],
             [x - 2 * abs(k), y + 25 * abs(k)]], 0)
    polygon(screen, (136, 5, 0),
            [[x - 20 * k, y + 12 * abs(k)], [x - 10 * k, y + 14 * abs(k)], [x - 10 * k, y + 20 * abs(k)],
             [x - 22 * k, y + 25 * abs(k)]], 0)


def bird(x, y, k):
    """Птица. x, y координаты центра тела птицы, k - коэффициент размера птицы: если k < 0, то птица смотрит налево,
     иначе - направо"""

    # служебный код
    z = False
    pool = [130, 80, 50, 8, 80, 40, 70, 65]
    for i in range(len(pool)):
        pool[i] *= abs(k)
    pool1 = [-65, 35, 95, 125, -45, -39, 5, -30]
    for i in range(len(pool1)):
        pool1[i] *= abs(k)

    # условия для k < 0
    if k < 0:
        k = - k
        for i in range(len(pool1)):
            pool1[i] = - pool1[i] - pool[i]
        z = True

    # основная часть тела
    ellipse(screen, (255, 255, 255), [x + pool1[0], y - 35 * k, pool[0], 70 * k])
    ellipse(screen, (255, 255, 255), [x + pool1[1], y - 25 * k, pool[1], 30 * k])
    ellipse(screen, (255, 255, 255), [x + pool1[2], y - 40 * k, pool[2], 30 * k])
    ellipse(screen, (0, 0, 0), [x + pool1[3], y - 35 * k, pool[3], 8 * k])
    ellipse(screen, (255, 255, 255), [x + pool1[4], y + 5 * k, pool[4], 50 * k])
    ellipse(screen, (255, 255, 255), [x + pool1[5], y + 15 * k, pool[5], 50 * k])
    ellipse(screen, (255, 255, 255), [x + pool1[6], y + 40 * k, pool[6], 15 * k])
    ellipse(screen, (255, 255, 255), [x + pool1[7], y + 55 * k, pool[7], 15 * k])

    # служебный код
    if z is True:
        c = k
        k = - k
    else:
        c = k

    # хвост
    polygon(screen, (255, 255, 255),
            [[x - 65 * k, y + 5 * c], [x - 105 * k, y - 5 * c], [x - 95 * k, y - 35 * c], [x - 55 * k, y - 15 * c]], 0)

    # крылья
    polygon(screen, (255, 255, 255),
            [[x - 35 * k, y - 25 * c], [x - 55 * k, y - 55 * c], [x - 115 * k, y - 70 * c], [x - 125 * k, y - 85 * c],
             [x - 50 * k, y - 90 * c], [x + 5 * k, y - 85 * c], [x + 8 * k, y - 35 * c]], 0)
    polygon(screen, (255, 255, 255),
            [[x - 25 * k, y - 35 * c], [x - 45 * k, y - 65 * c], [x - 105 * k, y - 80 * c], [x - 115 * k, y - 95 * c],
             [x - 60 * k, y - 100 * c], [x + 15 * k, y - 95 * c], [x + 18 * k, y - 15 * c]], 0)

    # клюв
    polygon(screen, (255, 232, 0),
            [[x + 142 * k, y - 30 * c], [x + 168 * k, y - 30 * c], [x + 160 * k, y - 23 * c],
             [x + 144 * k, y - 21 * c]], 0)

    # ноги
    polygon(screen, (255, 232, 0),
            [[x + 70 * k, y + 43 * c], [x + 90 * k, y + 47 * c], [x + 75 * k, y + 50 * c], [x + 85 * k, y + 55 * c],
             [x + 70 * k, y + 57 * c], [x + 65 * k, y + 65 * c], [x + 65 * k, y + 51 * c]])
    polygon(screen, (255, 232, 0), [[x + 35 * k, y + 60 * c], [x + 55 * k, y + 64 * c], [x + 40 * k, y + 67 * c],
                                    [x + 50 * k, y + 72 * c], [x + 35 * k, y + 74 * c], [x + 30 * k, y + 82 * c],
                                    [x + 30 * k, y + 64 * c]])


def font():
    """фон, как на исходной картинке - набор разноцветных прямоугольников"""
    rect(screen, (23, 11, 125), (0, 0, 700, 80))
    rect(screen, (88, 93, 238), (0, 80, 700, 50))
    rect(screen, (225, 137, 201), (0, 130, 700, 80))
    rect(screen, (235, 93, 197), (0, 210, 700, 100))
    rect(screen, (243, 165, 49), (0, 310, 700, 90))
    rect(screen, (6, 120, 195), (0, 400, 700, 350))


def albatross1(x, y, k):
    """Чайка первого типа(наклонённая влево). x, y - координаты чайки, k - коэффициент размера"""
    arc(screen, (255, 255, 255), [x, y, 60 * k, 30 * k], np.pi / 6, 7 * np.pi / 6, 2)
    arc(screen, (255, 255, 255), [x + 56 * k, y - 6 * k, 60 * k, 30 * k], np.pi / 12, np.pi, 2)
    circle(screen, (255, 255, 255), [x + 56 * k, y + 7 * k], 2 * int(k), 2 * int(k))


def albatross2(x, y, k):
    """чайка второго типа(горизонтальная). x, y - координаты чайки, k - коэффициент размера"""
    arc(screen, (255, 255, 255), [x, y, 60 * k, 30 * k], 0, np.pi, 2)
    arc(screen, (255, 255, 255), [x + 60 * k, y + 2 * k, 60 * k, 30 * k], 0, np.pi, 2)
    circle(screen, (255, 255, 255), [x + 60 * k, y + 15 * k], 2 * int(k), 2 * int(k))


def albatross3(x, y, k):
    """чайка третьего типа(наклонённая вправо). x, y - координаты чайки, k - коэффициент размера"""
    arc(screen, (255, 255, 255), [x, y, 60 * k, 30 * k], 0, 11 * np.pi / 12, 2)
    arc(screen, (255, 255, 255), [x + 58 * k, y + 5 * k, 60 * k, 30 * k], 0, 11 * np.pi / 12, 2)
    circle(screen, (255, 255, 255), [x + 60 * k, y + 15 * k], 2 * int(k), 2 * int(k))


screen = pygame.display.set_mode((700, 750))
fps = 30
clock = pygame.time.Clock()

# фон, рыбы, птицы
font()
fish(600, 500, 1)
fish(450, 600, 1)
fish(100, 550, - 1)
bird(200, 450, 1 / 4)
bird(350, 500, 3 / 4)
bird(570, 420, - 1/4)

# альбатросы
albatross1(60, 100, 0.5)
albatross1(80, 150, 1)
albatross1(500, 200, 0.7)
albatross1(180, 300, 0.3)
albatross2(300, 200, 1)
albatross2(60, 50, 0.5)
albatross2(150, 320, 0.3)
albatross3(400, 50, 1)
albatross3(200, 100, 0.5)
albatross3(190, 335, 0.4)


pygame.display.update()
finished = False
while not finished:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
