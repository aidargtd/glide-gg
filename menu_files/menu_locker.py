from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuLockerPage(MenuPage):
    def render_background(self, screen, pos=False):
        screen.fill(BLACK_COLOR)

    def render_extra(self, screen):
        x = 150
        print_text(screen, 'Шкафчик', x, 50, FONT_SIZE_FIFTY, font_type=FONT_ROB_THIN)
