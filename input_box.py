import pygame as pg
from parametres import *

pg.init()
COLOR_INACTIVE = pg.Color(COLOR_LIGHT_SKY)
COLOR_ACTIVE = pg.Color(COLOR_DODGER_BLUE)
FONT = pg.font.Font(None, FONT_THIRTY_TWO)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:CUT_LAST_FRAME]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(MAX_LEN_INPUT, self.txt_surface.get_width() + INCREASE_BOX)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + INCREASE_BOX_X, self.rect.y + INCREASE_BOX_Y))
        pg.draw.rect(screen, self.color, self.rect, 2)
