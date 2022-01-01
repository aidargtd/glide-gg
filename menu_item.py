from pygame.font import Font, match_font
from pygame.draw import lines

from general_functions import print_text
from parametres import *


class MenuItem:
    def __init__(self, label, left_top, onclick=None):
        self.label = label
        self.padding = 20  # расстояние от текста до рамки
        self.font_name = FONT_ROB_LIGHT
        self.font_size = 50
        self.text_color = WHITE_COLOR
        self.border_color = WHITE_COLOR
        self.border_width = 4
        self.border_length = 8
        self.onclick = onclick
        self.active = False
        self.rect = None  # координаты углов, включая рамку
        self.left_top = left_top  # координаты (x, y) левого верхнего угла

    def render_border(self, surface, left, top, right, bottom):
        if not self.active:
            return
        # левый верхний
        lines(
            surface,
            self.border_color,
            False,
            [
                (left, top + self.border_length),
                (left, top),
                (left + self.border_length, top)
            ],
            self.border_width
        )
        # правый верхний
        lines(
            surface,
            self.border_color,
            False,
            [
                (right - self.border_length, top),
                (right, top),
                (right, top + self.border_length)
            ],
            self.border_width
        )
        # правый нижний
        lines(
            surface,
            self.border_color,
            False,
            [
                (right, bottom - self.border_length),
                (right, bottom),
                (right - self.border_length, bottom)
            ],
            self.border_width
        )
        # левый нижний
        lines(
            surface,
            self.border_color,
            False,
            [
                (left, bottom - self.border_length),
                (left, bottom),
                (left + self.border_length, bottom)
            ],
            self.border_width
        )

    def render(self, surface):
        text_rect = print_text(surface, self.label, *self.left_top)
        left, top = self.left_top
        self.rect = (
            left - self.padding,
            top - self.padding,
            left + text_rect.w + self.padding,
            top + text_rect.h + self.padding
        )
        self.render_border(surface, *self.rect)

    def hover(self, x, y):
        if self.rect is None:
            return
        (left, top, right, bottom) = self.rect
        self.active = left <= x <= right and top <= y <= bottom
