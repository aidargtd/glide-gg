from menu_files.menu_page import MenuPage
from general_functions import *
from Button import Button
import gaming_cycle
from load_music import *

"""
    Здесь описываются кнопки, которые направляют вас на уровени
"""


class MenuNextLevelsPage(MenuPage):
    # Цифры это координаты кнопок, PYGAME)
    def render_extra(self, screen):
        print_text(screen, HOPE_TITLE, 50, 100, FONT_FORTY_SIZE, font_type=FONT_ROB_THIN, font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ПЯТОГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_first_lvl3.draw(50, 150, BTN_FIRST_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=51)

        btn_sec_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_sec_lvl3.draw(110, 150, BTN_SECOND_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=52)

        btn_third_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_third_lvl3.draw(170, 150, BTN_THIRD_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=53)

        btn_fourth_lvl4 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_X)
        btn_fourth_lvl4.draw(50, 210, BTN_FOURTH_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=54)

        btn_five_lvl5 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_five_lvl5.draw(110, 210, BTN_FIFTH_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=55)

        btn_six_lvl6 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_six_lvl6.draw(170, 210, BTN_SIXTH_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=56)

        print_text(screen, ACCEPTANCE_TITLE, 50, 270, FONT_FORTY_SIZE, font_type=FONT_ROB_THIN, font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ШЕСТОГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_first_lvl3.draw(50, 320, BTN_FIRST_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=61)

        btn_sec_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_sec_lvl3.draw(110, 320, BTN_SECOND_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=62)

        btn_third_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_third_lvl3.draw(170, 320, BTN_THIRD_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=63)

        btn_fourth_lvl4 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_fourth_lvl4.draw(50, 370, BTN_FOURTH_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=64)

        btn_five_lvl5 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_five_lvl5.draw(110, 370, BTN_FIFTH_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=65)

        btn_six_lvl6 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_six_lvl6.draw(170, 370, BTN_SIXTH_LEVEL, gaming_cycle.game_cycle, FONT_SIZE_FIFTY, id=66)
