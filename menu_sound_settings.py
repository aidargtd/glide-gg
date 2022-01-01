from general_functions import print_text
from menu_page import MenuPage


class MenuSoundPage(MenuPage):
    def render_extra(self, surface):
        x = 10
        print_text(surface, 'музыка - ', x, 100, 30, font_type='Roboto-Thin.ttf')
        print_text(surface, 'речь - ', x, 200, 30, font_type='Roboto-Thin.ttf')
        print_text(surface, 'звуковые эффекты - ', x, 300, 30, font_type='Roboto-Thin.ttf')
