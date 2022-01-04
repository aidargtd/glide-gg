from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuShopPage(MenuPage):
    def render_extra(self, screen):
        x = 50
        print_text(screen, 'Магазин скинов', x, 50, FONT_FORTY_SIZE, font_type=FONT_ROB_THIN)