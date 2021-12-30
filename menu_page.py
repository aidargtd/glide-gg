from pygame import Surface
from parametres import *
from general_functions import *


class MenuPage:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.items = []
        self.bottom_margin = 100  # расстояние от первого пункта меню до низа экрана
        self.between_items_margin = 50  # расстояние между пунктами меню

    def add_item(self, item):
        self.items.append(item)

    def screen_size(self):
        rect = self.screen.get_rect()
        return rect.w, rect.h

    def render(self):
        menu_background = load_image(MENU_IMG)
        surface = Surface(self.screen_size())
        surface.blit(menu_background, (0, 0))
        self.render_items(surface)
        self.screen.blit(surface, (0, 0))

    def render_items(self, surface):
        screen_w, screen_h = self.screen_size()
        item_h = screen_h - self.bottom_margin
        for item in self.items:
            item_h = item.render(surface, screen_w, item_h) - self.between_items_margin

    def hover(self, x, y):
        for item in self.items:
            item.hover(x, y)

    def click(self, x, y):
        for item in self.items:
            if item.active and item.onclick is not None:
                item.onclick()
                return
