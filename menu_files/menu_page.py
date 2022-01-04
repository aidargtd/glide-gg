from pygame import Surface
from menu_files.menu_item import MenuItem
from general_functions import *
from load_m_bg import kosmo_imgs
from load_music import *

img_counter = 0


class MenuPage:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.items = []
        self.items_for_change = []

    # если числа в left_top отрицательные, то это отступы от правого и нижнего края экрана
    def add_item(self, message, left_top, onclick=None, color=WHITE_COLOR, font_size=FONT_FORTY_SIZE,
                 font_type=FONT_ROB_THIN):
        self.items.append(MenuItem(message, self.convert_coords(left_top), onclick, color, font_size, font_type))

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

    def render_background(self, screen):
        global img_counter
        screen.fill(BLACK_COLOR)
        if img_counter == 78:
            img_counter = 0
        screen.blit(kosmo_imgs[img_counter // 2], (0, 0))
        img_counter += 1

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
