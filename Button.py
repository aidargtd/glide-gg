from general_functions import *
from pygame.draw import lines
from load_music import *
from load_music import *
import db_functions


class Button:
    def __init__(self, screen, width, height, inactive_col=BLACK_COLOR, active_col=DEEP_GRAY_COLOR_1):
        self.width = width
        self.height = height
        self.inactive_col = inactive_col
        self.active_col = active_col
        self.text_color = WHITE_COLOR
        self.border_color = WHITE_COLOR
        self.screen = screen

    def draw(self, x, y, message=None, action=None, font_size=30, id=None, font_type=FONT_ROB_LIGHT):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.active_col, (x, y, self.width, self.height))
            if click[0] == 1:
                sound_effects(SOUND_CLICK,
                              select_table(SETTINGS, SOUND_EFFECTS)[0][0])
                pygame.time.delay(DELAY_THREE_OO)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    elif id is not None:
                        action(id)
                    else:
                        action()
        else:
            if self.inactive_col:
                pygame.draw.rect(self.screen, self.inactive_col, (x, y, self.width, self.height))

        print_text(self.screen, message=message, x=x + 10, y=y + 10, font_size=font_size, font_type=font_type)
