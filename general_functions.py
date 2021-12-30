import os
import sys
import pygame
from db_functions import *
from parametres import *


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


def get_pict_name_by_id(id):
    return select_one_with_aspect(IMAGES, ID, id, NAME)


def correct_obst_arr(arr):
    for i in range(len(arr)):
        arr[i] = list(arr[i][INX_ID_LEVEL + 1:])
        image_id = arr[i][INX_IMG_NAME]
        arr[i][INX_IMG_NAME] = get_pict_name_by_id(image_id)
    return arr


def get_obstacles(id_level, obst_type):
    obstacles = select_all_with_aspect(obst_type,
                                       ID_LEVEL, id_level, *TABLES[obst_type])
    return HIDDEN_OBSTACLE, correct_obst_arr(obstacles)

# def get_side_obstacles(id_level):
#     obstacles = select_all_with_aspect(SIDE_OBSTACLES,
#                                        ID_LEVEL, id_level, *TABLES[SIDE_OBSTACLES])
#
#     return HIDDEN_OBSTACLE, correct_obst_arr(obstacles)
#
#
# def get_twist_obstacles(id_level):
#     obstacles = select_all_with_aspect(TWIST_OBSTACLES,
#                                        ID_LEVEL, id_level, *TABLES[TWIST_OBSTACLES])
#
#     return HIDDEN_OBSTACLE, correct_obst_arr(obstacles)
