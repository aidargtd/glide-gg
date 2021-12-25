import os
import sys
import pygame
import random


count = 0

FPS = 60
WIDTH = 700
HIGHT = 900

pygame.init()

array_walls1 = [[50, 0, 0, 2, True],
                [50, -200, 0, 2, True],
                [435, -400, 0, 2, True],
                [-200, -150, 2, 3, True],
                [1150, -1050, -2, 3, True]]
INX_X_POS = 0
INX_Y_POS = 1
INX_X_SPEED = 2
INX_Y_SPEED = 3
INX_INVIZ = 4


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


all_sprites = pygame.sprite.Group()


# class Mountain(pygame.sprite.Sprite):
#     image = load_image("mountains.png")
#
#     def __init__(self):
#         super().__init__(all_sprites)
#         self.image = Mountain.image
#         self.rect = self.image.get_rect()
#         self.mask = pygame.mask.from_surface(self.image)
#         self.rect.bottom = HIGHT
#
#
# mountain = Mountain()


class Wall1(pygame.sprite.Sprite):
    image = load_image("wall1.png")

    def __init__(self, arr_data):
        super().__init__(all_sprites)
        self.image = Wall1.image
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
        if enemy.rect.y > 900:
            walls_list.remove(enemy)


def create_walls(array_walls1):
    for i in range(len(array_walls1)):
        array_walls1[i][INX_Y_POS] = array_walls1[i][INX_Y_POS] + array_walls1[i][INX_Y_SPEED]
        array_walls1[i][INX_X_POS] = array_walls1[i][INX_X_POS] + array_walls1[i][INX_X_SPEED]
        if array_walls1[i][INX_Y_POS] >= 0 and array_walls1[i][INX_INVIZ]:
            array_walls1[i][INX_INVIZ] = False
            Wall1(array_walls1[i])


size = width, height = WIDTH, HIGHT
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    create_walls(array_walls1)
    count += 1
    print(count, len(all_sprites))

    delete_wall(all_sprites)

    all_sprites.update()
    screen.fill('black')
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)
pygame.quit()
