import numpy as np
import pygame as pygame
import random as rnd
import pygame.freetype
pygame.init()
FPS = 60
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
WIDTH = 1366
HEIGHT = 768
g = 1
dt = 1
balls_array = []
targets_array = []
targets_hit = 0
points_count = 0
targets_number = 2
delay = 121


class Ball:
    def __init__(self, screen: pygame.Surface):
        self.x = 0
        self.y = 0
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = rnd.choice(GAME_COLORS)
        self.screen = screen
        self.health = 75

    def move(self):
        self.x += self.vx * dt
        self.y = self.y + ((self.vy + g * dt) ** 2 - self.vy ** 2) / 2 * g
        self.vy += g * dt
        if self.x + self.r > WIDTH:
            self.vx = - 0.1 * self.vx
            self.x = WIDTH - self.r
        if self.x - self.r < 0:
            self.vx = - 0.1 * self.vx
            self.x = self.r
        if self.y + self.r > HEIGHT - 30:
            self.vy = - 0.1 * self.vy
            self.y = HEIGHT - 30 - self.r
            self.health -= 1
        if self.y - self.r < 0:
            self.vy = - 0.1 * self.vy
            self.y = self.r
        if self.y > HEIGHT - 30 - self.r - 2:
            self.vx *= 0.9

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hit_test(self, obj):
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen, x=40, y=HEIGHT-40):
        self.x = x
        self.y = y
        self.dx = 10
        self.dy = 10
        self.dr = np.power(self.dx ** 2 + self.dy ** 2, 1 / 2)
        self.power = 10
        self.ll = self.power + 50
        self.pulling_value = 0
        self.width = 10
        self.color = GREY
        self.screen = screen
        self.move_right_bool = False
        self.move_left_bool = False

    def targeting(self, event_):
        self.dx = event_.pos[0] - self.x
        self.dy = event_.pos[1] - self.y
        self.dr = np.power(self.dx ** 2 + self.dy ** 2, 1 / 2)

    def start_pulling(self, event_):
        if event_:
            self.pulling_value = 1

    def end_pulling(self):
        ball = Ball(self.screen)
        ball.x = self.x + self.dx * self.ll / self.dr
        ball.y = self.y + self.dy * self.ll / self.dr
        ball.vx = self.power * self.dx / self.dr / 2
        ball.vy = self.power * self.dy / self.dr / 2
        balls_array.append(ball)
        self.pulling_value = 0
        self.power = 10
        self.ll = self.power + 50

    def draw(self):
        pygame.draw.rect(self.screen, GREEN, (self.x - 30, self.y, 60, 30))
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.width)
        pygame.draw.polygon(self.screen, self.color, [
            (self.x - self.dy * self.width / self.dr, self.y + self.dx * self.width / self.dr),
            (self.x + self.dx * self.ll / self.dr - self.dy * self.width / self.dr,
             self.y + self.dy * self.ll / self.dr + self.dx * self.width / self.dr),
            (self.x + self.dx * self.ll / self.dr + self.dy * self.width / self.dr,
             self.y + self.dy * self.ll / self.dr - self.dx * self.width / self.dr),
            (self.x + self.dy * self.width / self.dr, self.y - self.dx * self.width / self.dr)
            ])

    def power_up(self):
        if self.pulling_value:
            if self.power < 100:
                self.power += 1
                self.ll = self.power + 50
                self.color = RED
            else:
                self.color = GREY

    def move_right(self):
        self.move_right_bool = True
        if self.x <= WIDTH:
            self.x += 3

    def move_left(self):
        if self.x > 0:
            self.x -= 3


class Target:
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.r = 0
        self.vx = rnd.randint(-5, 5)
        self.vy = 0
        self.color = GREEN
        self.screen = screen

    def new_target(self):
        self.x = rnd.randint(600, 780)
        self.y = rnd.randint(300, 550)
        self.r = rnd.randint(10, 25)

    def hit(self):
        global targets_hit, points_count
        points_count += 1
        targets_hit += 1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx * dt
        self.y = self.y + ((self.vy + g * dt) ** 2 - self.vy ** 2) / 2 * g
        self.vy += g * dt
        if self.x + self.r > WIDTH:
            self.vx = - self.vx
        if self.x - self.r < 0:
            self.vx = - self.vx
        if self.y + self.r > HEIGHT - 30:
            self.vy = - self.vy
        if self.y - self.r < 0:
            self.vy = - self.vy


screen_ = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
clock = pygame.time.Clock()
finished = False
gun = Gun(screen_)
for i in range(targets_number):
    a = Target(screen_)
    a.new_target()
    targets_array.append(a)
gun.color = GREY

while not finished:
    screen_.fill(WHITE)
    pygame.draw.rect(screen_, (0, 0, 0), (0, HEIGHT - 30, WIDTH, 30))
    gun.draw()
    for t in targets_array:
        t.draw()
    for b in balls_array:
        b.draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and delay >= 120:
            gun.start_pulling(event)
        elif event.type == pygame.MOUSEBUTTONUP and delay >= 120:
            gun.end_pulling()
        elif event.type == pygame.MOUSEBUTTONUP and delay < 120:
            gun.pulling_value = 0
            gun.power = 10
            gun.ll = gun.power + 50
        elif event.type == pygame.MOUSEMOTION and delay >= 120:
            gun.targeting(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            gun.move_right_bool = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            gun.move_right_bool = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            gun.move_left_bool = True
        elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            gun.move_left_bool = False

    for t in targets_array:
        t.move()
    for b in balls_array:
        b.move()
        if b.health == 0:
            balls_array.pop(balls_array.index(b))
        for target in targets_array:
            if b.hit_test(target) and b.vx ** 2 + b.vy ** 2 >= 80:
                targets_array.pop(targets_array.index(target))
    if delay == 120:
        for i in range(targets_number):
            a = Target(screen_)
            a.new_target()
            targets_array.append(a)
    if targets_hit == len(targets_array) and delay >= 120:
        delay = 0
        targets_hit = 0
    if gun.pulling_value:
        gun.power_up()
    if gun.move_right_bool is True:
        gun.move_right()
    if gun.move_left_bool is True:
        gun.move_left()

    delay += 1
pygame.quit()
