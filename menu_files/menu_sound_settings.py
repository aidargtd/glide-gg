from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuSoundPage(MenuPage):
    def render_extra(self, screen):
        x = 10
        print_text(screen, 'музыка - ', x, 100, 30, font_type='Roboto-Thin.ttf')
        print_text(screen, 'речь - ', x, 200, 30, font_type='Roboto-Thin.ttf')
        print_text(screen, 'звуковые эффекты - ', x, 300, 30, font_type='Roboto-Thin.ttf')
