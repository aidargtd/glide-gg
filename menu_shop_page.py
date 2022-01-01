from general_functions import print_text
from menu_page import MenuPage


class MenuShopPage(MenuPage):
    def render_extra(self, surface):
        x = 50
        print_text(surface, 'Магазин скинов', x, 50, 40, font_type='Roboto-Thin.ttf')