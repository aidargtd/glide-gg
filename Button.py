from general_functions import *
from pygame.draw import lines


class Button:
    def __init__(self, screen, width, height):
        self.width = width
        self.height = height
        self.inactive_col = BLACK_COLOR
        self.active_col = (25, 205, 60)
        self.text_color = WHITE_COLOR
        self.border_color = WHITE_COLOR
        self.screen = screen
        # self.border_width = 4
        # self.border_length = 8
        # self.active = False

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(self.screen, self.active_col, (x, y, self.width, self.height))
            if click[0] == 1:
                pass
                # pygame.mixer.Sound.play(button_sound)
                # pygame.time.delay(300)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
        else:
            pygame.draw.rect(self.screen, self.inactive_col, (x, y, self.width, self.height))

        print_text(self.screen, message=message, x=x + 10, y=y + 10, font_size=font_size)
