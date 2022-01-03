from menu_files.menu_page import MenuPage
from general_functions import *
from Button import Button
from GlideGame import game_cycle
from load_music import *

"""
    Здесь описываются кнопки, которые направляют вас на уровени
"""


class MenuNextLevelsPage(MenuPage):
    def render_extra(self, screen):
        print_text(screen, 'принятие', 50, 100, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ПЕРВОГО СЮЖЕТА
        btn_first_lvl1 = Button(screen, 50, 50)
        btn_first_lvl1.draw(50, 150, ' I ', game_cycle, 50, id=11)

        btn_sec_lvl1 = Button(screen, 50, 50)
        btn_sec_lvl1.draw(110, 150, 'II', game_cycle, 50, id=12)

        btn_third_lvl1 = Button(screen, 50, 50)
        btn_third_lvl1.draw(170, 150, 'III', game_cycle, 50, id=13)

        btn_fourth_lvl1 = Button(screen, 50, 50)
        btn_fourth_lvl1.draw(50, 210, 'IV', game_cycle, 50, id=14)

        btn_five_lvl1 = Button(screen, 50, 50)
        btn_five_lvl1.draw(110, 210, 'V', game_cycle, 50, id=15)

        btn_six_lvl1 = Button(screen, 50, 50)
        btn_six_lvl1.draw(170, 210, 'VI', game_cycle, 50, id=16)

        print_text(screen, 'надежда', 50, 270, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ВТОРОГО СЮЖЕТА
        btn_first_lvl2 = Button(screen, 50, 50)
        btn_first_lvl2.draw(50, 320, ' I ', game_cycle, 50, id=21)

        btn_sec_lvl2 = Button(screen, 50, 50)
        btn_sec_lvl2.draw(110, 320, 'II', game_cycle, 50, id=22)

        btn_third_lvl2 = Button(screen, 50, 50)
        btn_third_lvl2.draw(170, 320, 'III', game_cycle, 50, id=23)

        btn_fourth_lvl2 = Button(screen, 50, 50)
        btn_fourth_lvl2.draw(50, 370, 'IV', game_cycle, 50, id=14)

        btn_five_lvl2 = Button(screen, 50, 50)
        btn_five_lvl2.draw(110, 370, 'V', game_cycle, 50, id=15)

        btn_six_lvl2 = Button(screen, 50, 50)
        btn_six_lvl2.draw(170, 370, 'VI', game_cycle, 50, id=16)
