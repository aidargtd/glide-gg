from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuShopAndLockerPage(MenuPage):
    def render_extra(self, screen):
        x = 50
        print_text(screen, 'Вы можете посмотреть новые скины,', x, 50, FONT_THIRTY_SIZE, font_type=FONT_ROB_THIN)
        print_text(screen, 'либо выбрать в шкафчике', x, 90, FONT_THIRTY_SIZE, font_type=FONT_ROB_THIN)
