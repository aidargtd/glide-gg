from general_functions import print_text
from menu_page import MenuPage


class MenuShopPage(MenuPage):
    def render_extra(self, surface):
        x = 50
        print_text(surface, 'Магазин скинов', x, 50, 40, font_type='Roboto-Thin.ttf')
        labels = ['влево', 'вправо']
        keys = ['LEFT', 'RIGHT']
        y = 150
        gap = 50
        x_label = 80
        x_key = 180
        for label, key in zip(labels, keys):
            print_text(surface, label, x_label, y)
            print_text(surface, key, x_key, y)
            y += gap
