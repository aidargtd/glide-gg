from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *
from db_functions import *
import pygame as pg
from input_box import InputBox

pg.init()


class BeforeInfinityLevel(MenuPage):
    player_name_input = InputBox(100, 100, 140, 32)

    def render_extra(self, screen):
        x = 10
        print_text(screen, TOP_PLAYER, x, 50, FONT_FORTY_SIZE, WHITE_COLOR, font_type=FONT_ROB_THIN)
        max_score = select_max_elem('score', )[0]
        name_player = \
            select_one_with_aspect(INF_LEVELS, SCORE, select_max_elem(SCORE, )[0], NAME_PLAYER)[0]
        print_text(screen, f'{name_player}  {max_score}', 350, 50, FONT_FORTY_SIZE, DEEP_GRAY,
                   font_type=FONT_ROB_THIN)

        print_text(screen, MESSAGE_BEFORE_START_GAME, 20, 130, FONT_FORTY_SIZE, DEEP_GRAY,
                   font_type=FONT_ROB_THIN)
