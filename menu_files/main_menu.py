from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuMainPage(MenuPage):
    def render_extra(self, screen):
        print_text(screen, 'GLADE', 150, 50, font_color=WHITE_COLOR, font_type='font/DroidSansFallback.ttf',
                   font_size=120)
