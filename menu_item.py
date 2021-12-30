from pygame.font import Font, match_font
from pygame.draw import lines
from parametres import *


class MenuItem:
    def __init__(self, label, onclick=None):
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

    def render_text(self, surface, screen_w, bottom_h):
        font = Font(match_font(self.font_name), self.font_size)
        text = font.render(self.label, True, self.text_color)
        rect = text.get_rect()
        left = (screen_w - rect.w) // 2 - self.padding
        top = bottom_h - rect.h - self.padding
        surface.blit(text, (left, top))
        return left, top, rect.w, rect.h

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

    def render(self, surface, screen_w, bottom_h):
        left, top, w, h = self.render_text(surface, screen_w, bottom_h)
        self.rect = (left - self.padding, top - self.padding, left + w + self.padding, bottom_h)
        self.render_border(surface, *self.rect)
        return top

    def hover(self, x, y):
        if self.rect is None:
            return
        (left, top, right, bottom) = self.rect
        self.active = left <= x <= right and top <= y <= bottom
