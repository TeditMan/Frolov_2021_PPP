import numpy as np
from random import choice
from random import randint as rnd
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
g = 9.8
WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen1: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen1
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y = self.y - self.vy + g / 2
        self.vy -= g
        if self.x > WIDTH or self.x < 0:
            self.vx = - self.vx
        if self.y > HEIGHT or self.y < 0:
            self.vy = - self.vy

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hit_test(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen1):
        self.x = 10
        self.y = 550
        self.screen = screen1
        self.f2_power = 10
        self.f2_on = 0
        self.an = np.pi / 2
        self.color = GREY

    def fire2_start(self, event1):
        if event1:
            self.f2_on = 1

    def fire2_end(self, event1):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = np.arctan2((event1.pos[1]-new_ball.y), (event1.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * np.cos(self.an)
        new_ball.vy = - self.f2_power * np.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targeting(self, event1):
        """Прицеливание. Зависит от положения мыши."""
        if event1:
            self.an = np.arctan((event1.pos[1]-450) / (event1.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x + np.cos(self.an) * (50 + self.f2_power),
                                                                     self.y + np.sin(self.an) * (50 + self.f2_power)), 15)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen1, x=0, y=0, r=0):
        self.points = 0
        self.live = 1
        self.x = x
        self.y = y
        self.r = r
        self.color = RED
        self.screen = screen1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targeting(event)

    for b in balls:
        b.move()
        if b.hit_test(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()
pygame.quit()
