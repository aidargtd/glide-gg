from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuSettingsPage(MenuPage):
    def render_extra(self, screen):
        x = 50
        print_text(screen, MANAGEMENT_TITLE, x, 50, FONT_SIZE_FIFTY, DEEP_GRAY_COLOR_1, font_type=FONT_ROB_THIN)
        labels = [LEFT_TITLE, RIGHT_TITLE]
        keys = [LEFT_KEY_NAME, RIGHT_KEY_NAME]
        y = 150
        gap = 50
        x_label = 80
        x_key = 180
        for label, key in zip(labels, keys):
            print_text(screen, label, x_label, y)
            print_text(screen, key, x_key, y)
            y += gap
        print_text(screen, EFFECTS_TITLE, x, 280, 50, DEEP_GRAY_COLOR_1, font_type=FONT_ROB_THIN)
