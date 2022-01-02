from menu_files.menu_page import MenuPage
from general_functions import *
from Button import Button
from GlideGame import game_cycle
from load_music import *

"""
    Здесь описываются кнопки, которые направляют вас на уровени
"""


class MenuLevelsPage(MenuPage):
    def render_extra(self, screen):
        print_text(screen, 'сюжет', 250, 50, 50, font_type='Roboto-Thin.ttf')
        print_text(screen, 'незнание', 50, 100, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
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

        print_text(screen, 'отрицание', 50, 270, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
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

        print_text(screen, 'гнев', 50, 430, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ТРЕТЬЕГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, 50, 50)
        btn_first_lvl3.draw(50, 480, ' I ', game_cycle, 50, id=31)

        btn_sec_lvl3 = Button(screen, 50, 50)
        btn_sec_lvl3.draw(110, 480, 'II', game_cycle, 50, id=32)

        btn_third_lvl3 = Button(screen, 50, 50)
        btn_third_lvl3.draw(170, 480, 'III', game_cycle, 50, id=33)

        btn_fourth_lvl4 = Button(screen, 50, 50)
        btn_fourth_lvl4.draw(50, 530, 'IV', game_cycle, 50, id=34)

        btn_five_lvl5 = Button(screen, 50, 50)
        btn_five_lvl5.draw(110, 530, 'V', game_cycle, 50, id=35)

        btn_six_lvl6 = Button(screen, 50, 50)
        btn_six_lvl6.draw(170, 530, 'VI', game_cycle, 50, id=36)

        print_text(screen, 'переговоры', 50, 590, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ЧЕТВЕРТОГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, 50, 50)
        btn_first_lvl3.draw(50, 640, ' I ', game_cycle, 50, id=41)

        btn_sec_lvl3 = Button(screen, 50, 50)
        btn_sec_lvl3.draw(110, 640, 'II', game_cycle, 50, id=42)

        btn_third_lvl3 = Button(screen, 50, 50)
        btn_third_lvl3.draw(170, 640, 'III', game_cycle, 50, id=43)

        btn_fourth_lvl4 = Button(screen, 50, 50)
        btn_fourth_lvl4.draw(50, 690, 'IV', game_cycle, 50, id=44)

        btn_five_lvl5 = Button(screen, 50, 50)
        btn_five_lvl5.draw(110, 690, 'V', game_cycle, 50, id=45)

        btn_six_lvl6 = Button(screen, 50, 50)
        btn_six_lvl6.draw(170, 690, 'VI', game_cycle, 50, id=46)

        print_text(screen, 'надежда', 50, 750, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ПЯТОГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, 50, 50)
        btn_first_lvl3.draw(50, 800, ' I ', game_cycle, 50, id=51)

        btn_sec_lvl3 = Button(screen, 50, 50)
        btn_sec_lvl3.draw(110, 800, 'II', game_cycle, 50, id=52)

        btn_third_lvl3 = Button(screen, 50, 50)
        btn_third_lvl3.draw(170, 800, 'III', game_cycle, 50, id=53)

        btn_fourth_lvl4 = Button(screen, 50, 50)
        btn_fourth_lvl4.draw(50, 850, 'IV', game_cycle, 50, id=54)

        btn_five_lvl5 = Button(screen, 50, 50)
        btn_five_lvl5.draw(110, 850, 'V', game_cycle, 50, id=55)

        btn_six_lvl6 = Button(screen, 50, 50)
        btn_six_lvl6.draw(170, 850, 'VI', game_cycle, 50, id=56)

        print_text(screen, 'принятие', 50, 910, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ШЕСТОГО СЮЖЕТА
        btn_first_lvl3 = Button(screen, 50, 50)
        btn_first_lvl3.draw(50, 960, ' I ', game_cycle, 50, id=61)

        btn_sec_lvl3 = Button(screen, 50, 50)
        btn_sec_lvl3.draw(110, 960, 'II', game_cycle, 50, id=62)

        btn_third_lvl3 = Button(screen, 50, 50)
        btn_third_lvl3.draw(170, 960, 'III', game_cycle, 50, id=63)

        btn_fourth_lvl4 = Button(screen, 50, 50)
        btn_fourth_lvl4.draw(50, 1010, 'IV', game_cycle, 50, id=64)

        btn_five_lvl5 = Button(screen, 50, 50)
        btn_five_lvl5.draw(110, 1010, 'V', game_cycle, 50, id=65)

        btn_six_lvl6 = Button(screen, 50, 50)
        btn_six_lvl6.draw(170, 1010, 'VI', game_cycle, 50, id=66)
