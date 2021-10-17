import pygame
from pygame.draw import *
pygame.init()


def fish(x, y, k):
    """function is drawing a fish(body is an ellipse, eyes are two circles, flippers are a number of polygons)"""
    ellipse(screen, (13, 110, 60), [x, y, 80 * k, 30 * k])
    circle(screen, (0, 0, 250), (x + 60 * k, y + 15 * k), 6 * k, 6 * k)
    circle(screen, (0, 0, 0), (x + k * 61, y + 15 * k), 2 * k, 2 * k)
    polygon(screen, (136, 5, 0), [[x, y + 15 * k], [x - 20 * k, y + 18 * k], [x - 15 * k, y], [x + 3 * k, y + 8 * k]],
            0)
    polygon(screen, (136, 5, 0),
            [[x + 40 * k, y], [x + 30 * k, y - 15 * k], [x + 55 * k, y - 10 * k], [x + 50 * k, y + k]], 0)
    polygon(screen, (136, 5, 0),
            [[x + 40 * k, y + 30 * k], [x + 50 * k, y + 29 * k], [x + 55 * k, y + 35 * k], [x + 38 * k, y + 40 * k]], 0)
    polygon(screen, (136, 5, 0),
            [[x + 20 * k, y + 27 * k], [x + 30 * k, y + 29 * k], [x + 30 * k, y + 35 * k], [x + 18 * k, y + 40 * k]], 0)


def bird(x, y, k):
    """рисуем птицу: сперва тело как набор эллипсов, потом хвост, крылья, клюв и когти как многоугольники"""
    ellipse(screen, (255, 255, 255), [x, y, 130 * k, 70 * k])
    ellipse(screen, (255, 255, 255), [x + 100 * k, y + 10 * k, 80 * k, 30 * k])
    ellipse(screen, (255, 255, 255), [x + 160 * k, y - 5 * k, 50 * k, 30 * k])
    ellipse(screen, (0, 0, 0), [x + 190 * k, y, 8 * k, 8 * k])
    ellipse(screen, (255, 255, 255), [x + 20 * k, y + 40 * k, 80 * k, 50 * k])
    ellipse(screen, (255, 255, 255), [x + 26 * k, y + 50 * k, 40 * k, 50 * k])
    ellipse(screen, (255, 255, 255), [x + 70 * k, y + 75 * k, 70 * k, 15 * k])
    ellipse(screen, (255, 255, 255), [x + 35 * k, y + 90 * k, 65 * k, 15 * k])

    # tail
    polygon(screen, (255, 255, 255),
            [[x, y + 40 * k], [x - 40 * k, y + 30 * k], [x - 30 * k, y], [x + 10 * k, y + 20 * k]], 0)

    # wings
    polygon(screen, (255, 255, 255),
            [[x + 30 * k, y + 10 * k], [x + 10 * k, y - 20 * k], [x - 50 * k, y - 35 * k], [x - 60 * k, y - 50 * k],
             [x + 15 * k, y - 55 * k], [x + 70 * k, y - 50 * k], [x + 73 * k, y]], 0)
    polygon(screen, (255, 255, 255),
            [[x + 40 * k, y], [x + 20 * k, y - 30 * k], [x - 40 * k, y - 45 * k], [x - 50 * k, y - 60 * k],
             [x + 5 * k, y - 65 * k], [x + 80 * k, y - 60 * k], [x + 83 * k, y + 20 * k]], 0)

    # beak
    polygon(screen, (255, 232, 0),
            [[x + 207 * k, y + 5 * k], [x + 233 * k, y + 5 * k], [x + 225 * k, y + 12 * k], [x + 209 * k, y + 14 * k]],
            0)

    # clutches&
    polygon(screen, (255, 232, 0),
            [[x + 135 * k, y + 78 * k], [x + 155 * k, y + 82 * k], [x + 140 * k, y + 85 * k], [x + 150 * k, y + 90 * k],
             [x + 135 * k, y + 92 * k], [x + 130 * k, y + 100 * k], [x + 130 * k, y + 86 * k]])
    polygon(screen, (255, 232, 0), [[x + 100 * k, y + 95 * k], [x + 120 * k, y + 99 * k], [x + 105 * k, y + 102 * k],
                                    [x + 115 * k, y + 107 * k], [x + 100 * k, y + 109 * k], [x + 95 * k, y + 117 * k],
                                    [x + 95 * k, y + 99 * k]])


def bird_reversed(x, y, k):
    ellipse(screen, (255, 255, 255), [x, y, 130 * k, 70 * k])
    ellipse(screen, (255, 255, 255), [x - 55 * k, y + 10 * k, 80 * k, 30 * k])
    ellipse(screen, (255, 255, 255), [x - 85 * k, y - 5 * k, 50 * k, 30 * k])
    ellipse(screen, (0, 0, 0), [x - 72 * k, y, 8 * k, 8 * k])
    ellipse(screen, (255, 255, 255), [x + 30 * k, y + 40 * k, 80 * k, 50 * k])
    ellipse(screen, (255, 255, 255), [x + 60 * k, y + 50 * k, 40 * k, 50 * k])
    ellipse(screen, (255, 255, 255), [x - 10 * k, y + 75 * k, 70 * k, 15 * k])
    ellipse(screen, (255, 255, 255), [x + 25 * k, y + 90 * k, 65 * k, 15 * k])

    polygon(screen, (255, 255, 255),
            [[x + 120 * k, y + 40 * k], [x + 170 * k, y + 30 * k], [x + 160 * k, y], [x + 120 * k, y + 20 * k]], 0)

    polygon(screen, (255, 255, 255),
            [[x + 95 * k, y + 11 * k], [x + 115 * k, y - 19 * k], [x + 175 * k, y - 34 * k], [x + 185 * k, y - 49 * k],
             [x + 100 * k, y - 54 * k], [x + 45 * k, y - 49 * k], [x + 42 * k, y + k]], 0)
    polygon(screen, (255, 255, 255),
            [[x + 100 * k, y + 70 * k], [x + 105 * k, y - 29 * k], [x + 165 * k, y - 44 * k], [x + 175 * k, y - 59 * k],
             [x + 90 * k, y - 64 * k], [x + 35 * k, y - 59 * k], [x + 40 * k, y + 5 * k]], 0)

    polygon(screen, (255, 232, 0),
            [[x - 85 * k, y + 5 * k], [x - 112 * k, y + 5 * k], [x - 104 * k, y + 12 * k], [x - 85 * k, y + 12 * k]], 0)

    polygon(screen, (255, 232, 0),
            [[x - 5 * k, y + 78 * k], [x - 25 * k, y + 82 * k], [x - 10 * k, y + 85 * k], [x - 20 * k, y + 90 * k],
             [x - 5 * k, y + 92 * k], [x, y + 100 * k], [x, y + 86 * k]])
    polygon(screen, (255, 232, 0),
            [[x + 30 * k, y + 93 * k], [x + 10 * k, y + 97 * k], [x + 25 * k, y + 100 * k], [x + 15 * k, y + 105 * k],
             [x + 30 * k, y + 107 * k], [x + 35 * k, y + 115 * k], [x + 35 * k, y + 101 * k]])


def font():
    """фон, как на исходной картинке - набор разноцветных прямоугольников"""
    rect(screen, (23, 11, 125), (0, 0, 700, 80))
    rect(screen, (88, 93, 238), (0, 80, 700, 50))
    rect(screen, (225, 137, 201), (0, 130, 700, 80))
    rect(screen, (235, 93, 197), (0, 210, 700, 100))
    rect(screen, (243, 165, 49), (0, 310, 700, 90))
    rect(screen, (6, 120, 195), (0, 400, 700, 350))


def albatross1(x, y, k):
    """чайка первого типа(наклонённая влево). Две дуги + кружочек по центру"""
    arc(screen, (255, 255, 255), [x, y, 60 * k, 30 * k], pi / 6, 7 * pi / 6, 2)
    arc(screen, (255, 255, 255), [x + 56 * k, y - 6 * k, 60 * k, 30 * k], pi / 12, pi, 2)
    circle(screen, (255, 255, 255), [x + 56 * k, y + 7 * k], 2 * int(k), 2 * int(k))


def albatross2(x, y, k):
    """чайка второго типа(горизонтальная). Рисуем аналогично"""
    arc(screen, (255, 255, 255), [x, y, 60 * k, 30 * k], 0, pi, 2)
    arc(screen, (255, 255, 255), [x + 60 * k, y + 2 * k, 60 * k, 30 * k], 0, pi, 2)
    circle(screen, (255, 255, 255), [x + 60 * k, y + 15 * k], 2 * int(k), 2 * int(k))


def albatross3(x, y, k):
    """чайка третьего типа(наклонённая вправо). Аналогично"""
    arc(screen, (255, 255, 255), [x, y, 60 * k, 30 * k], 0, 11 * pi / 12, 2)
    arc(screen, (255, 255, 255), [x + 58 * k, y + 5 * k, 60 * k, 30 * k], 0, 11 * pi / 12, 2)
    circle(screen, (255, 255, 255), [x + 60 * k, y + 15 * k], 2 * int(k), 2 * int(k))


screen = pygame.display.set_mode((700, 750))

fps = 30
pi = 3.14
clock = pygame.time.Clock()

# main picture
font()
fish(600, 500, 1)
fish(450, 600, 1)
fish(50, 550, 1)
bird(200, 450, 1 / 4)
bird(350, 500, 3 / 4)
bird_reversed(570, 420, 1 / 4)

# drawing seagulls
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
