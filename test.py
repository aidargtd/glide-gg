import pygame
import os
import sys
import math
import random

BLACK = 'black'
RED = 'red'
BLUE = 'blue'
DEEP_GRAY = (54, 54, 54)
FPS = 60
SIZE = WIDTH, HEIGHT = 600, 800
SPEED_MOVEMENT_TRUE = 4.5
SPEED_MOVEMENT_FALSE = -4.5
CONVERT_ANGLE_TO_SIDE = 100
count = 0

array_walls1 = [[65, 0, 0, 5, True],
                [65, -200, 0, 5, True],
                [320, -400, 0, 5, True],
                [65, -600, 0, 5, True],
                [65, -800, 0, 5, True],
                [320, -1000, 0, 5, True],
                ]

for i in range(100):
    #     if random.choice([True, False]):
    array_walls1.append([65, -1200 - (i * 200), 0, 5, True])
    # else:
    #     array_walls1.append([320, -1200 - (i * 200), 0, 5, True])

INX_X_POS = 0
INX_Y_POS = 1
INX_X_SPEED = 2
INX_Y_SPEED = 3
INX_INVIZ = 4

all_walls = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Wall1(pygame.sprite.Sprite):
    image = load_image("base_wall_2_1.png")

    def __init__(self, arr_data):
        super().__init__(all_walls)
        self.image = Wall1.image
        self.image = pygame.transform.rotate(self.image, random.randint(0, 90))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        x_pos, y_pos, x_speed, y_speed = arr_data[0], arr_data[1], arr_data[2], arr_data[3]
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed_x = x_speed
        self.speed_y = y_speed

    def update(self):
        # if not pygame.sprite.collide_mask(self, mountain):
        #     self.rect = self.rect.move(0, 1)
        self.rect = self.rect.move(self.speed_x, self.speed_y)


def delete_wall(walls_list):
    for enemy in walls_list:
        if enemy.rect.y > 800:
            walls_list.remove(enemy)


def create_walls(array_walls1):
    for i in range(len(array_walls1)):
        array_walls1[i][INX_Y_POS] = array_walls1[i][INX_Y_POS] + array_walls1[i][INX_Y_SPEED]
        array_walls1[i][INX_X_POS] = array_walls1[i][INX_X_POS] + array_walls1[i][INX_X_SPEED]
        if array_walls1[i][INX_Y_POS] >= -200 and array_walls1[i][INX_INVIZ]:
            array_walls1[i][INX_INVIZ] = False
            Wall1(array_walls1[i])


class RedCircle(pygame.sprite.Sprite):
    def __init__(self, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('red_circle.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.init_red_angle = 0
        self.rect.x = 385
        self.rect.y = 585

    def update(self, speed_move):
        self.init_red_angle += speed_move
        angle_red = self.init_red_angle * math.pi / 180
        self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_red)) + (HEIGHT // 2) - 115
        self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_red)) + HEIGHT - 215
        for i in all_walls:
            if pygame.sprite.collide_mask(self, i):
                exit()


class BlueCircle(pygame.sprite.Sprite):
    def __init__(self, speed=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('blue_circle.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.init_blue_angle = 180
        self.rect.x = 185
        self.rect.y = 585

    def update(self, speed_move):
        self.init_blue_angle += speed_move
        angle_blue = self.init_blue_angle * math.pi / 180
        self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_blue)) + (HEIGHT // 2 - 115)
        self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_blue)) + (HEIGHT - 215)
        for i in all_walls:
            if pygame.sprite.collide_mask(self, i):
                exit()


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")
all_sprites = pygame.sprite.Group()

fps = 60
fps_clock = pygame.time.Clock()
red_circle = RedCircle()
blue_circle = BlueCircle()
all_sprites.add(red_circle, blue_circle)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    create_walls(array_walls1)
    delete_wall(all_sprites)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        red_circle.update(SPEED_MOVEMENT_TRUE)
        blue_circle.update(SPEED_MOVEMENT_TRUE)
    elif keys[pygame.K_LEFT]:
        red_circle.update(SPEED_MOVEMENT_FALSE)
        blue_circle.update(SPEED_MOVEMENT_FALSE)
    else:
        red_circle.update(0)
        blue_circle.update(0)
    screen.fill(BLACK)
    pygame.draw.circle(screen, DEEP_GRAY, (300, 600), 100, 2)
    all_walls.update()
    all_walls.draw(screen)
    all_sprites.draw(screen)
    pygame.display.update()
    fps_clock.tick(fps)
pygame.quit()
