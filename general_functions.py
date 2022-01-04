import os
import sys
import pygame
from pygame.font import match_font

from db_functions import *
from parametres import *

fps_clock = pygame.time.Clock()

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('pictures', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == SPECIAL_VALUE:
            colorkey = image.get_at(START_OF_SCREEN)
        image.set_colorkey(colorkey)
    return image


def quit():
    pygame.quit()
    sys.exit()


def print_text(screen, message, x, y, font_size=30, font_color=WHITE_COLOR, font_type='font/Roboto-Light.ttf'):
    font_type = pygame.font.Font(match_font(font_type), font_size)
    text = font_type.render(message, True, font_color)
    screen.blit(text, (x, y))
    return text.get_rect()


def correct_obst_arr(arr):
    for i in range(len(arr)):
        arr[i] = list(arr[i][INX_IMG_ID:])
        image_id = arr[i][INX_IMG_NAME]
        img_name = select_one_with_aspect(IMAGES, ID, image_id, NAME)[0]
        arr[i][INX_IMG_NAME] = img_name
    return arr


def get_obstacles(id_level, obst_type):
    obstacles = select_all_with_aspect(obst_type,
                                       ID_LEVEL, id_level, *TABLES[obst_type])
    return correct_obst_arr(obstacles)


def check_sane_y_cord(y):
    return NOT_UPDATE_Y_CORD_1 <= y <= NOT_UPDATE_Y_CORD_2


def get_loc_walls_gr(al_walls_gr):
    loc_walls_group = pygame.sprite.Group()
    for wall in al_walls_gr:
        if check_sane_y_cord(wall.rect.y):
            wall.add(loc_walls_group)
    return loc_walls_group


def get_dodged(walls_group):
    counter = 0
    for wall in walls_group:
        if wall.rect.y >= DODGE_Y_CORD:
            counter += 1
    return counter


def check_level_complited(walls_group):
    f = True
    for wall in walls_group:
        if wall.rect.y < 1000:
            f = False
    return f


def get_bank(l_id):
    coins_amount = select_one_with_aspect(LEVELS, ID, l_id, COINS)[0]
    return coins_amount


def nullify_coins(l_id):
    update_aspect(LEVELS, COINS, ZERO_COINS, ID, l_id)


def pay_coins(coins, user_id=1):
    cash = select_one_with_aspect(USERS,ID, user_id, COINS_AMOUNT)[0]
    update_aspect(USERS, COINS_AMOUNT, coins + cash, ID, user_id)


def print_level_number(sc, l_id):
    print_text(sc, f'Сюжет:  {l_id // 10}', 490, 10, 20)
    print_text(sc, f'Уровень: {l_id % 10}', 490, 25, 20)
