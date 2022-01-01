import pygame
import os
import sys
import math
import random
from parametres import *
from general_functions import *
count = 0

arr_obstacles = []

INX_X_POS = 0
INX_Y_POS = 1
INX_X_SPEED = 2
INX_Y_SPEED = 3
INX_INVIZ = 4

for i in range(100):
    if random.choice([True, False]):
        arr_obstacles.append([65, 0 - (i * 185), 0, 5, True])
    else:
        arr_obstacles.append([320, 0 - (i * 185), 0, 5, True])


class Obstacle1(pygame.sprite.Sprite):
    image = load_image(BASE_WALL_IMG)

    def __init__(self, arr_data):
        super().__init__(all_walls)
        self.image = Obstacle1.image
        # random.randint(0, 90)
        self.image = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        x_pos, y_pos, x_speed, y_speed = arr_data[0], arr_data[1], arr_data[2], arr_data[3]
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed_x = x_speed
        self.speed_y = y_speed

    def update(self, angle=10):
        print(self.rect.x, self.rect.y)
        self.rect = self.rect.move(self.speed_x, self.speed_y)


def delete_obstacle(walls_list):
    for enemy in walls_list:
        if enemy.rect.y > 800:
            walls_list.remove(enemy)


def create_obstacle(obstacles_array):
    for i in range(len(obstacles_array)):
        obstacles_array[i][INX_Y_POS] = obstacles_array[i][INX_Y_POS] + obstacles_array[i][INX_Y_SPEED]
        obstacles_array[i][INX_X_POS] = obstacles_array[i][INX_X_POS] + obstacles_array[i][INX_X_SPEED]
        if obstacles_array[i][INX_Y_POS] >= -200 and obstacles_array[i][INX_INVIZ]:
            obstacles_array[i][INX_INVIZ] = False
            Obstacle1(obstacles_array[i])


# class RedCircle(pygame.sprite.Sprite):
#     def __init__(self, speed=0):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = load_image('red_circle.png')
#         self.rect = self.image.get_rect()
#         self.mask = pygame.mask.from_surface(self.image)
#         self.init_red_angle = 0
#         self.rect.x = 385
#         self.rect.y = 585
#
#     def update(self, speed_move):
#         self.init_red_angle += speed_move
#         angle_red = self.init_red_angle * math.pi / 180
#         self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_red)) + (HEIGHT // 2) - 115
#         self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_red)) + HEIGHT - 215
#         for i in all_walls:
#             if pygame.sprite.collide_mask(self, i):
#                 exit()
#
#
# class BlueCircle(pygame.sprite.Sprite):
#     def __init__(self, speed=0):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = load_image('blue_circle.png')
#         self.rect = self.image.get_rect()
#         self.mask = pygame.mask.from_surface(self.image)
#         self.init_blue_angle = 180
#         self.rect.x = 185
#         self.rect.y = 585
#
#     def update(self, speed_move):
#         self.init_blue_angle += speed_move
#         angle_blue = self.init_blue_angle * math.pi / 180
#         self.rect.x = (CONVERT_ANGLE_TO_SIDE * math.cos(angle_blue)) + (HEIGHT // 2 - 115)
#         self.rect.y = (CONVERT_ANGLE_TO_SIDE * math.sin(angle_blue)) + (HEIGHT - 215)
#         for i in all_walls:
#             if pygame.sprite.collide_mask(self, i):
#                 exit()


pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")
all_walls = pygame.sprite.Group()

fps = 60
fps_clock = pygame.time.Clock()
# red_circle = RedCircle()
# blue_circle = BlueCircle()
# all_sprites.add(red_circle, blue_circle)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    create_obstacle(arr_obstacles)
    delete_obstacle(all_walls)
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_RIGHT]:
    #     red_circle.update(SPEED_MOVEMENT_TRUE)
    #     blue_circle.update(SPEED_MOVEMENT_TRUE)
    # elif keys[pygame.K_LEFT]:
    #     red_circle.update(SPEED_MOVEMENT_FALSE)
    #     blue_circle.update(SPEED_MOVEMENT_FALSE)
    # else:
    #     red_circle.update(0)
    #     blue_circle.update(0)
    screen.fill(BLACK_COLOR)
    # pygame.draw.circle(screen, DEEP_GRAY, (300, 600), 100, 1)
    all_walls.update()
    all_walls.draw(screen)
    pygame.display.update()
    fps_clock.tick(fps)
pygame.quit()
