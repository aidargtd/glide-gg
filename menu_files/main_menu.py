from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuMainPage(MenuPage):
    def render_extra(self, screen):
        print_text(screen, TITLE, x=150, y=50, font_color=WHITE_COLOR, font_type=FONT_DROID,
                   font_size=FONT_SIZE_ONE_H_TWENTY)
