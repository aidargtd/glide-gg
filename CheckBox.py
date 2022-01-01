import pygame
from parametres import *
pygame.font.init()


class Checkbox:
    def __init__(self, surface, x, y, idnum, color=(230, 230, 230),
                 caption="", outline_color=BLACK_COLOR, check_color=BLACK_COLOR,
                 font_size=30, font_color=BLACK_COLOR,
                 text_offset=(28, 1), font=FONT_ROB_LIGHT):
        self.surface = surface
        self.x = x
        self.y = y
        self.color = color
        self.caption = caption
        self.oc = outline_color
        self.cc = check_color
        self.fs = font_size
        self.fc = font_color
        self.to = text_offset
        self.ft = font

        # identification for removal and reorginazation
        self.idnum = idnum

        # checkbox object
        self.checkbox_obj = pygame.Rect(self.x, self.y, 12, 12)
        self.checkbox_outline = self.checkbox_obj.copy()

        # variables to test the different states of the checkbox
        self.checked = False

    def _draw_button_text(self):
        self.font = pygame.font.SysFont(self.ft, self.fs)
        self.font_surf = self.font.render(self.caption, True, self.fc)
        w, h = self.font.size(self.caption)
        self.font_pos = (self.x + self.to[0], self.y + 12 / 2 - h / 2 +
                         self.to[1])
        self.surface.blit(self.font_surf, self.font_pos)

    def render_checkbox(self):
        if self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
            pygame.draw.circle(self.surface, self.cc, (self.x + 6, self.y + 6), 4)

        elif not self.checked:
            pygame.draw.rect(self.surface, self.color, self.checkbox_obj)
            pygame.draw.rect(self.surface, self.oc, self.checkbox_outline, 1)
        self._draw_button_text()

    def _update(self, event_object):
        x, y = pygame.mouse.get_pos()
        px, py, w, h = self.checkbox_obj
        if px < x < px + w and py < y < py + w:
            if self.checked:
                self.checked = False
            else:
                self.checked = True

    def update_checkbox(self, event_object):
        if event_object.type == pygame.MOUSEBUTTONDOWN:
            self.click = True
            self._update(event_object)


if __name__ == '__main__':
    boxes = []
    screen = pygame.display.set_mode([800, 600])
    button = Checkbox(screen, 200, 200, 0, caption='музыка')
    button2 = Checkbox(screen, 200, 250, 1, caption='эффекты')
    boxes.append(button)
    boxes.append(button2)
    screen.fill((255, 255, 255))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for box in boxes:
                    box.update_checkbox(event)
                    if box.checked is True:
                        for b in boxes:
                            if b != box:
                                b.checked = False
        for box in boxes:
            box.render_checkbox()

        pygame.display.flip()

    pygame.time.wait(1000)
