from general_functions import print_text
from menu_files.menu_page import MenuPage


class MenuSettingsPage(MenuPage):
    def render_extra(self, surface):
        x = 50
        print_text(surface, 'управление', x, 50, 30, font_type='Roboto-Thin.ttf')
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
        print_text(surface, 'эффекты', x, 400, 30, font_type='Roboto-Thin.ttf')