 ++
pygame.init()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
colors_list = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 120
finished = False
f = 0
delta = 50
try_count = 0
points_count = 0
bonus_points = 5
balls_count = 0
hit = False
array_of_points = []
# lvl = int(input('выберите уровень сложности от 1 до 3: '))
lvl = 300
number_of_balls = 8

# авторизация, добавление новых игроков в таблицу
nickname = str(input('Введите ваш никнейм, или придумайте новый: '))
with open('Table.txt', 'r') as file:
    inp = file.read().split('\n')
    registered = False
    for k1 in range(len(inp)):
        if inp[k1].split()[2] == nickname:
            registered = True
if registered is False:
    with open('Table.txt', 'a') as file:
        new_string = str('\n' + str(len(inp) + 1) + ' - ' + nickname + ' : ' + str(0))
        file.write(new_string)
# обновление переменной inp - массив из строк таблицы лидеров
with open('Table.txt', 'r') as file:
    inp = file.read().split('\n')

"""
# balance of levels
if lvl == 1:
    lvl = 480
    number_of_balls = 6
elif lvl == 2:
    lvl = 360
    number_of_balls = 7
elif lvl == 3:
    lvl = 240
    number_of_balls = 8
"""

clock = pygame.time.Clock()
screen_length = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_length, screen_height), pygame.FULLSCREEN)
pygame.display.update()


colors = []
pool = []
moving_array = []
dx = []
dy = []


def generate_arrays_for_balls():
    global colors, pool, moving_array, dx, dy
    for p in range(number_of_balls):
        colors.append(colors_list[randint(0, 5)])
        pool.append([randint(100, 1266), randint(100, 668), randint(20, 100)])
        moving_array.append(True)
        dx.append(randint(-100, 100))
        dy.append(randint(-100, 100))


def do_pool_correction():
    global pool
    intersection_value = 1
    while intersection_value > 0:
        intersection_value = 0
        for i in range(len(pool)):
            for k in range(i + 1, len(pool)):
                if (pool[k][0] - pool[i][0]) ** 2 + (pool[k][1] - pool[i][1]) ** 2 < (pool[k][2] + pool[i][2] + 2) ** 2:
                    intersection_value += 1
        if intersection_value > 0:
            for i in range(len(pool)):
                pool[i][0] = randint(100, 1100)
                pool[i][1] = randint(100, 500)
                pool[i][2] = randint(20, 100)


def clear_arrays():
    global colors, pool, moving_array, dx, dy
    colors = []
    pool = []
    moving_array = []
    dx = []
    dy = []


def create_balls_from_arrays():
    for p in range(number_of_balls):
        circle(screen, colors[p], (pool[p][0], pool[p][1]),
               pool[p][2])
        pygame.display.update()


def move_balls():
    for kk in range(number_of_balls):
        if moving_array[kk] is True:
            circle(screen, BLACK, (pool[kk][0], pool[kk][1]), pool[kk][2])
            pool[kk][0] += dx[kk] / delta
            pool[kk][1] += dy[kk] / delta
            circle(screen, colors[kk], (pool[kk][0], pool[kk][1]), pool[kk][2])
            pygame.display.update()
            if pool[kk][0] + dx[kk] / delta + pool[kk][2] >= screen_length or pool[kk][0] +\
                    dx[kk] / delta - pool[kk][2] <= 0:
                dx[kk] = -dx[kk]
            if pool[kk][1] + dy[kk] / delta + pool[kk][2] >= screen_height or pool[kk][1] +\
                    dy[kk] / delta - pool[kk][2] <= 0:
                dy[kk] = -dy[kk]
            for i in range(kk + 1, number_of_balls):
                if (pool[i][0] + dx[i] / delta - pool[kk][0] - dx[kk] / delta) ** 2 +\
                        (pool[i][1] + dy[i] / delta - pool[kk][1] - dy[kk] / delta) ** 2 <\
                        (pool[i][2] + pool[kk][2]) ** 2 and moving_array[i] is True:
                    a = pool[i][0] - pool[kk][0]
                    b = pool[i][1] - pool[kk][1]
                    c = np.power(a ** 2 + b ** 2, 1 / 2)
                    s11 = a / c
                    s21 = b / c
                    s12 = b / c
                    s22 = -a / c
                    dx1 = (s12 * dy[kk] - s22 * dx[kk]) / (s12 * s21 - s11 * s22)
                    dx2 = (s12 * dy[i] - s22 * dx[i]) / (s12 * s21 - s11 * s22)
                    dy1 = (s11 * dy[kk] - s21 * dx[kk]) / (s11 * s22 - s12 * s21)
                    dy2 = (s11 * dy[i] - s21 * dx[i]) / (s11 * s22 - s12 * s21)
                    dx1_ = ((pool[kk][2] ** 2 - pool[i][2] ** 2) * dx1 + 2 * pool[i][2] ** 2 * dx2) / (
                                pool[kk][2] ** 2 + pool[i][2] ** 2)
                    dx2_ = (2 * pool[kk][2] ** 2 * dx1 + (pool[i][2] ** 2 - pool[kk][2] ** 2) * dx2) / (
                                pool[kk][2] ** 2 + pool[i][2] ** 2)
                    dy1_ = dy1
                    dy2_ = dy2
                    dx_kk = s11 * dx1_ + s12 * dy1_
                    dy_kk = s21 * dx1_ + s22 * dy1_
                    dx_i = s11 * dx2_ + s12 * dy2_
                    dy_i = s21 * dx2_ + s22 * dy2_
                    dx[kk] = dx_kk
                    dy[kk] = dy_kk
                    dx[i] = dx_i
                    dy[i] = dy_i


while not finished:
    clock.tick(FPS)
#
    if f == 0:
        generate_arrays_for_balls()
        do_pool_correction()
        create_balls_from_arrays()
#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finished = True
        elif try_count == 20:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for o in range(number_of_balls):
                if (event.pos[0] - pool[o][0]) ** 2 + (event.pos[1] - pool[o][1]) ** 2 <= pool[o][2] ** 2 and\
                        moving_array[o] is True:
                    circle(screen, BLACK, (pool[o][0], pool[o][1]), pool[o][2])
                    moving_array[o] = False
                    if pool[o][2] <= 40:
                        points_count += 4
                    elif 40 < pool[o][2] <= 60:
                        points_count += 3
                    elif 60 < pool[o][2] <= 80:
                        points_count += 2
                    elif 80 < pool[o][0]:
                        points_count += 1
                    balls_count += 1
                    hit = True
                    pygame.display.update()
            if hit is False:
                points_count -= 1
#
    move_balls()
#
    if f == lvl - 20:
        for ii in range(number_of_balls):
            moving_array[ii] = False
            screen.fill(BLACK)
            pygame.display.update()
    elif f == lvl - 1:
        clear_arrays()
        if number_of_balls == balls_count:
            points_count += bonus_points
        balls_count = 0
        hit = False
        try_count += 1
    f += 1
    f %= lvl

# обновление таблицы лидеров, упорядочивание таблицы
with open('Table.txt', 'w') as file:
    for k1 in range(len(inp)):
        if inp[k1].split()[2] == nickname and int(inp[k1].split()[4]) < points_count:
            a1 = inp[k1].split()
            a1[4] = str(points_count)
            inp[k1] = ' '.join(a1)
            print('new record!')
        elif inp[k1].split()[2] == nickname and int(inp[k1].split()[4]) >= points_count:
            print('current record: ', inp[k1].split()[4])
    for k1 in range(len(inp)):
        array_of_points.append(int(inp[k1].split()[4]))
    file.write('\n'.join(inp))

with open('Table.txt', 'r') as file:
    inp = file.read().split('\n')
length = len(inp)
inp1 = []
for l1 in range(length):
    count = 0
    k1 = -1
    while count < len(inp):
        count = 0
        k1 += 1
        for i1 in range(len(inp)):
            if int(inp[k1].split()[4]) >= int(inp[i1].split()[4]):
                count += 1
    inp1.append(inp[k1])
    inp.pop(k1)
for l1 in range(len(inp1)):
    inp1[l1] = str(str(l1 + 1) + ' - ' + inp1[l1].split()[2] + ' : ' + inp1[l1].split()[4])
with open('Table.txt', 'w') as file:
    file.write('\n'.join(inp1))

# завершение программы
print('количество очков: ', points_count)
pygame.quit()
