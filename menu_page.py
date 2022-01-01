from pygame import Surface
from menu_item import MenuItem
from general_functions import *


class MenuPage:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.items = []
        self.items_for_change = []

    # если числа в left_top отрицательные, то это отступы от правого и нижнего края экрана
    def add_item(self, label, left_top, onclick=None, color=WHITE_COLOR):
        self.items.append(MenuItem(label, self.convert_coords(left_top), onclick, color))

    def convert_coords(self, left_top):
        left, top = left_top
        screen_w, screen_h = self.screen_size()
        if left < 0:
            left = screen_w + left
        if top < 0:
            top = screen_h + top
        return left, top

    def screen_size(self):
        rect = self.screen.get_rect()
        return rect.w, rect.h

    def render(self):
        surface = Surface(self.screen_size())
        self.render_background(surface)
        self.render_items(surface)
        self.render_extra(surface)
        self.screen.blit(surface, (0, 0))

    def render_extra(self, surface):
        pass

    def render_background(self, surface):
        menu_background = load_image(MENU_IMG)
        surface.blit(menu_background, (0, 0))

    def render_items(self, surface):
        for item in self.items:
            item.render(surface)

    def hover(self, x, y):
        for item in self.items:
            item.hover(x, y)

    def click(self, x, y):
        for item in self.items:
            if item.active and item.onclick is not None:
                item.onclick()
                return
