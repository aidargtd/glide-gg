from menu_files.menu_page import MenuPage
from general_functions import *
from Button import Button
from GlideGame import game_cycle


class MenuLevelsPage(MenuPage):
    def render_extra(self, surface):
        print_text(surface, 'сюжет', 250, 50, 50, font_type='Roboto-Thin.ttf')
        print_text(surface, 'незнание', 50, 100, 40, font_type='Roboto-Thin.ttf', font_color=DEEP_GRAY)
        # КНОПКИ УРОВНЕЙ ПЕРВОГО СЮЖЕТА
        btn_first_lvl = Button(surface, 50, 50)
        btn_first_lvl.draw(50, 150, ' I ', game_cycle, 50, 1)

        btn_sec_lvl = Button(surface, 50, 50)
        btn_sec_lvl.draw(110, 150, 'II', game_cycle, 50, 2)

        btn_third_lvl = Button(surface, 50, 50)
        btn_third_lvl.draw(170, 150, 'III', game_cycle, 50, 3)

        btn_fourth_lvl = Button(surface, 50, 50)
        btn_fourth_lvl.draw(50, 210, 'IV', game_cycle, 50, 4)

        btn_five_lvl = Button(surface, 50, 50)
        btn_five_lvl.draw(110, 210, 'V', game_cycle, 50, 5)

        btn_six_lvl = Button(surface, 50, 50)
        btn_six_lvl.draw(170, 210, 'VI', game_cycle, 50, 6)
