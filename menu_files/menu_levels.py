from menu_files.menu_page import MenuPage
from general_functions import *
from Button import Button
from gaming_cycle import game_cycle
from load_music import *

"""
    Здесь описываются кнопки, которые направляют вас на уровени
"""


class MenuLevelsPage(MenuPage):
    def render_extra(self, screen):
        print_text(screen, PLOT_TITLE, 250, 50, FONT_SIZE_FIFTY, font_type=FONT_ROB_THIN)
        print_text(screen, IGNORANCE_TITLE,
                   50, 100, FONT_FORTY_SIZE, font_type=FONT_ROB_THIN, font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ПЕРВОГО СЮЖЕТА
        btn_first_lvl1 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_first_lvl1.draw(50, 150, BTN_FIRST_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=11)

        btn_sec_lvl1 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_sec_lvl1.draw(110, 150, BTN_SECOND_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=12)

        btn_third_lvl1 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_third_lvl1.draw(170, 150, BTN_THIRD_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=13)

        btn_fourth_lvl1 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_fourth_lvl1.draw(50, 210, BTN_FOURTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=14)

        btn_five_lvl1 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_five_lvl1.draw(110, 210, BTN_FIFTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=15)

        btn_six_lvl1 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_six_lvl1.draw(170, 210, BTN_SIXTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=16)

        print_text(screen, DENIAL_TITLE, 50, 270, 40, font_type=FONT_ROB_THIN, font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ВТОРОГО СЮЖЕТА
        btn_first_lvl2 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_first_lvl2.draw(50, 320, BTN_FIRST_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=21)

        btn_sec_lvl2 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_sec_lvl2.draw(110, 320, BTN_SECOND_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=22)

        btn_third_lvl2 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_third_lvl2.draw(170, 320, BTN_THIRD_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=23)

        btn_fourth_lvl2 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_fourth_lvl2.draw(50, 370, BTN_FOURTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=14)

        btn_five_lvl2 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_five_lvl2.draw(110, 370, BTN_FIFTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=15)

        btn_six_lvl2 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_six_lvl2.draw(170, 370, BTN_SIXTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=16)

        print_text(screen, ANGER_TITLE, 50, 430, 40, font_type=FONT_ROB_THIN, font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ТРЕТЬЕГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_first_lvl3.draw(50, 480, BTN_FIRST_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=31)

        btn_sec_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_sec_lvl3.draw(110, 480, BTN_SECOND_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=32)

        btn_third_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_third_lvl3.draw(170, 480, BTN_THIRD_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=33)

        btn_fourth_lvl4 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_fourth_lvl4.draw(50, 530, BTN_FOURTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=34)

        btn_five_lvl5 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_five_lvl5.draw(110, 530, BTN_FIFTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=35)

        btn_six_lvl6 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_six_lvl6.draw(170, 530, BTN_SIXTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=36)

        print_text(screen, CONVERSATION_TITLE, 50, 590, 40, font_type=FONT_ROB_THIN, font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ЧЕТВЕРТОГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_X)
        btn_first_lvl3.draw(50, 640, BTN_FIRST_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=41)

        btn_sec_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_sec_lvl3.draw(110, 640, BTN_SECOND_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=42)

        btn_third_lvl3 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_third_lvl3.draw(170, 640, BTN_THIRD_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=43)

        btn_fourth_lvl4 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_fourth_lvl4.draw(50, 690, BTN_FOURTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=44)

        btn_five_lvl5 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_five_lvl5.draw(110, 690, BTN_FIFTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=45)

        btn_six_lvl6 = Button(screen, BTN_LEVELS_X, BTN_LEVELS_Y)
        btn_six_lvl6.draw(170, 690, BTN_SIXTH_LEVEL, game_cycle, FONT_SIZE_FIFTY, id=46)

