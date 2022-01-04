from general_functions import print_text
from menu_files.menu_page import MenuPage
from parametres import *


class MenuSoundPage(MenuPage):
    def render_extra(self, screen):
        x = 10
        print_text(screen, MUSIC_SETTINGS, x, 100, FONT_THIRTY_SIZE, font_type=FONT_ROB_THIN)
        print_text(screen, VOICE_SETTINGS, x, 200, FONT_THIRTY_SIZE, font_type=FONT_ROB_THIN)
        print_text(screen, SOUND_EFF_SETTINGS, x, 300, FONT_THIRTY_SIZE, font_type=FONT_ROB_THIN)
